from core.logger import AgentLogger




class BacktestEngine:



    def __init__(
        self,
        controller,
        account
    ):


        self.controller = controller

        self.account = account

        self.trades=[]





    def run(
        self,
        candles
    ):


        print(
            "\n========== BACKTEST START =========="
        )



        for index,candle in enumerate(candles):


            print(
                f"\nCANDLE {index}"
            )



            # ==========================
            # Update Existing Trade
            # ==========================


            closed_positions = (

                self.account.update_candle(

                    candle

                )

            )



            for position in closed_positions:


                self.trades.append(
                    position
                )


                print(
                    "TRADE CLOSED:",
                    position.__dict__
                )





            # ==========================
            # Need enough history
            # ==========================


            if index < 5:

                continue





            history = candles[
                max(0,index-5):index+1
            ]



            print(
                "\n===== MARKET ANALYSIS ====="
            )



            analysis = (

                self.controller.process(

                    history

                )

            )



            print(
                "\n===== AI RESULT ====="
            )


            print(
                analysis
            )




            decision = analysis.get(
                "decision",
                "WAIT"
            )



            # ==========================
            # OPEN BUY
            # ==========================


            if decision=="BUY":


                print(
                    "OPEN BUY"
                )


                self.account.open_position(

                    symbol="XAUUSD",

                    direction="BUY",

                    entry=candle["close"],

                    stop_loss=candle["close"]-20,

                    take_profit=candle["close"]+40,

                    volume=1

                )





            # ==========================
            # OPEN SELL
            # ==========================


            elif decision=="SELL":


                print(
                    "OPEN SELL"
                )



                self.account.open_position(

                    symbol="XAUUSD",

                    direction="SELL",

                    entry=candle["close"],

                    stop_loss=candle["close"]+20,

                    take_profit=candle["close"]-40,

                    volume=1

                )





            else:


                print(
                    "NO TRADE"
                )





        print(
            "\n========== BACKTEST END =========="
        )



        return self.generate_report()







    def generate_report(
        self
    ):


        total=len(
            self.trades
        )


        wins=0

        losses=0

        profit=0



        for trade in self.trades:


            profit += trade.pnl


            if trade.pnl>0:

                wins+=1

            else:

                losses+=1





        win_rate=0



        if total>0:

            win_rate=(

                wins /

                total *

                100

            )





        report={


            "total_trades":total,


            "wins":wins,


            "losses":losses,


            "win_rate":round(
                win_rate,
                2
            ),


            "profit":round(
                profit,
                2
            )

        }



        AgentLogger.info(

            f"Backtest Report: {report}"

        )


        return report