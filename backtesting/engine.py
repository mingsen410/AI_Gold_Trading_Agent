import logging


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

        self.balance = initial_balance

        self.position = None

        self.trades = []



    # ===============================
    # OPEN POSITION
    # ===============================

    def open_position(
            self,
            candle,
            signal
    ):


        entry = candle["close"]


        self.position = {


            "symbol":"XAUUSD",

            "direction":"BUY",

            "entry":entry,


            "sl":
                entry - 15,


            "tp":
                entry + 45,


            "exit":None,


            "pnl":0


        }



        print("\n===== OPEN BUY =====")

        print(self.position)




    # ===============================
    # CHECK EXIT
    # ===============================

    def check_exit(
            self,
            candle
    ):


        if self.position is None:
            return



        price=candle["close"]



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




    # ===============================
    # CLOSE TRADE
    # ===============================

    def close_trade(
            self,
            price,
            result
    ):


        trade=self.position


        trade["exit"]=price


        trade["pnl"]=(
            price-
            trade["entry"]
        )


        trade["result"]=result



        self.balance += trade["pnl"]



        self.trades.append(
            trade
        )


        print("\n===== CLOSE =====")

        print(trade)



        self.position=None





    # ===============================
    # MAIN LOOP
    # ===============================

    def run(self):


        print(
            "\n========== BACKTEST START =========="
        )


        for i in range(
            len(self.candles)
        ):


            candle=self.candles[i]


            print(
                f"\nCANDLE {i}"
            )



            # existing position

            self.check_exit(
                candle
            )



            if self.position:
                continue




            # =========================
            # Build Context
            # =========================


            context={


                "candles":
                    self.candles[
                        max(0,i-50):
                        i+1
                    ],


                "current":
                    candle



            }




            signal = self.entry_logic.generate_signal(
                context
            )



            print(
                "\n===== ICT SIGNAL ====="
            )

            print(signal)




            if signal["signal"]=="BUY":


                self.open_position(
                    candle,
                    signal
                )




        result=self.report()



        print(
            "\n========== BACKTEST END =========="
        )

        print(result)



        return result






    # ===============================
    # REPORT
    # ===============================


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


        losses=total-wins



        profit=sum(
            t["pnl"]
            for t in self.trades
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
                    wins/total*100,
                    2
                )
                if total else 0,



            "profit":
                round(
                    profit,
                    2
                ),



            "final_balance":
                round(
                    10000+profit,
                    2
                )

        }