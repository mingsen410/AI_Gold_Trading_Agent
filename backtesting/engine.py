import logging


class BacktestEngine:

    def __init__(
        self,
        candles,
        entry_logic,
        initial_balance=10000
    ):

        self.candles = candles
        self.entry_logic = entry_logic

        self.balance = initial_balance
        self.equity_curve = [
            initial_balance
        ]

        self.position = None
        self.trades = []


    def open_position(
        self,
        candle,
        signal
    ):

        entry = candle["close"]

        if signal["signal"]=="BUY":

            self.position = {

                "symbol":"XAUUSD",

                "direction":"BUY",

                "entry":entry,

                "sl":entry-10,

                "tp":entry+40,

                "status":"OPEN",

                "exit":None,

                "pnl":0
            }


            print(
                "\n===== POSITION OPEN ====="
            )

            print(
                self.position
            )


    def check_exit(
        self,
        candle
    ):

        if not self.position:
            return


        price=candle["close"]


        # BUY

        if self.position["direction"]=="BUY":


            # TP

            if price >= self.position["tp"]:


                self.close_trade(
                    price,
                    "WIN"
                )


            # SL

            elif price <= self.position["sl"]:


                self.close_trade(
                    price,
                    "LOSS"
                )



    def close_trade(
        self,
        price,
        status
    ):


        trade=self.position


        trade["exit"]=price


        if trade["direction"]=="BUY":

            pnl = price - trade["entry"]


        trade["pnl"]=pnl


        trade["status"]=status



        self.balance += pnl


        self.trades.append(
            trade
        )


        self.equity_curve.append(
            self.balance
        )


        print(
            "\n===== TRADE CLOSED ====="
        )

        print(
            trade
        )


        self.position=None



    def run(self):


        print(
            "\n========== BACKTEST START =========="
        )


        for i,candle in enumerate(self.candles):


            print(
                f"\nCANDLE {i}"
            )


            # check existing position

            self.check_exit(
                candle
            )



            if self.position:
                continue



            context = candle.get(
                "context",
                {}
            )


            signal = self.entry_logic.generate_signal(
                context
            )


            print(
                "\n===== ICT SIGNAL ====="
            )

            print(
                signal
            )


            if signal["signal"]=="BUY":


                self.open_position(
                    candle,
                    signal
                )



        result=self.report()


        print(
            "\n========== BACKTEST END =========="
        )

        print(
            result
        )


        return result




    def report(self):


        total=len(
            self.trades
        )


        wins=len(
            [
                x for x in self.trades
                if x["status"]=="WIN"
            ]
        )


        losses=len(
            [
                x for x in self.trades
                if x["status"]=="LOSS"
            ]
        )



        profit=sum(
            x["pnl"]
            for x in self.trades
        )


        loss_amount=sum(
            x["pnl"]
            for x in self.trades
            if x["pnl"]<0
        )



        if loss_amount==0:

            pf="INF"

        else:

            pf=round(
                profit /
                abs(loss_amount),
                2
            )


        win_rate=(
            wins/total*100
            if total>0
            else 0
        )



        return {


            "total_trades":total,

            "wins":wins,

            "losses":losses,

            "win_rate":round(
                win_rate,
                2
            ),

            "profit":profit,

            "profit_factor":pf,

            "final_balance":
                self.balance

        }