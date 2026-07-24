import logging

from risk_engine.risk_manager import RiskManager



logger = logging.getLogger(__name__)





class BacktestEngine:


    def __init__(
        self,
        candles,
        entry_logic,
        initial_balance=10000
    ):


        self.candles = candles

        self.entry_logic = entry_logic


        self.risk_manager = RiskManager()



        self.balance = initial_balance


        self.position = None


        self.trades = []


        self.current_history = []





    # =========================
    # Open Position
    # =========================

    def open_position(
        self,
        candle,
        signal
    ):


        entry = candle["close"]



        risk = self.risk_manager.calculate_sl_tp(

            entry,

            self.current_history,

            "BUY"

        )



        lot = self.risk_manager.calculate_position_size(

            self.balance,

            entry,

            risk["sl"]

        )



        self.position = {


            "symbol":
                "XAUUSD",



            "direction":
                "BUY",



            "lot":
                lot,



            "entry":
                entry,



            "sl":
                risk["sl"],



            "tp":
                risk["tp"],



            "atr":
                risk["atr"],



            "exit":
                None,



            "pnl":
                0

        }



        print(
            "\n===== OPEN BUY ====="
        )


        print(
            self.position
        )






    # =========================
    # Check Exit
    # =========================

    def check_exit(
        self,
        candle
    ):


        if not self.position:

            return



        price = candle["close"]



        if price >= self.position["tp"]:


            self.close_trade(
                price,
                "WIN"
            )



        elif price <= self.position["sl"]:


            self.close_trade(
                price,
                "LOSS"
            )






    # =========================
    # Close Trade
    # =========================

    def close_trade(
        self,
        price,
        result
    ):


        trade = self.position



        trade["exit"] = price



        movement = (

            price -

            trade["entry"]

        )



        # Gold PnL

        pnl = (

            movement *

            trade["lot"] *

            100

        )



        trade["pnl"] = round(
            pnl,
            2
        )


        trade["result"] = result



        self.balance += pnl



        self.trades.append(
            trade
        )



        print(
            "\n===== CLOSE ====="
        )


        print(
            trade
        )



        self.position = None






    # =========================
    # Run
    # =========================

    def run(self):


        print(
            "\n========== BACKTEST START =========="
        )



        for i,candle in enumerate(
            self.candles
        ):


            print(
                f"\nCANDLE {i}"
            )



            self.current_history = (

                self.candles[:i+1]

            )



            self.check_exit(
                candle
            )



            if self.position:

                continue



            context = candle.get(
                "context",
                {}
            )



            context["candles"] = self.current_history



            signal = self.entry_logic.generate_signal(

                context

            )



            print(
                "\n===== ICT SIGNAL ====="
            )


            print(
                signal
            )



            if signal["signal"] == "BUY":


                self.open_position(

                    candle,

                    signal

                )





        if self.position:


            self.close_trade(

                self.candles[-1]["close"],

                "FORCED CLOSE"

            )



        result=self.report()



        print(
            "\n========== BACKTEST END =========="
        )


        print(
            result
        )



        return result





    # =========================
    # Report
    # =========================

    def report(self):


        total=len(
            self.trades
        )



        wins=len(

            [

                t for t in self.trades

                if t["result"]=="WIN"

            ]

        )



        losses=len(

            [

                t for t in self.trades

                if t["result"]=="LOSS"

            ]

        )



        profit=sum(

            t["pnl"]

            for t in self.trades

        )



        win_rate=(

            wins /

            total *

            100

            if total

            else 0

        )



        return {


            "total_trades":

                total,


            "wins":

                wins,


            "losses":

                losses,


            "win_rate":

                round(

                    win_rate,

                    2

                ),


            "profit":

                round(

                    profit,

                    2

                ),


            "final_balance":

                round(

                    self.balance,

                    2

                )

        }