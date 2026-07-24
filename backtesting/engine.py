from analytics.performance import PerformanceAnalyzer



class BacktestEngine:


    def __init__(
        self,
        candles,
        entry_logic,
        risk_manager=None,
        initial_balance=10000
    ):

        self.candles = candles

        self.entry_logic = entry_logic

        self.risk_manager = risk_manager


        self.balance = initial_balance


        self.equity_curve = [

            initial_balance

        ]


        self.position = None


        self.trades = []





    # ==================================
    # Open Position
    # ==================================

    def open_position(
        self,
        candle,
        signal,
        atr=None
    ):


        entry = candle["close"]



        # default ATR
        if atr is None:

            atr = 10



        sl_distance = atr * 1.5

        tp_distance = atr * 3





        lot = 0.01



        if self.risk_manager:


            lot = self.risk_manager.calculate_lot(

                balance=self.balance,

                stop_loss_distance=sl_distance

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

                round(

                    entry-sl_distance,

                    2

                ),



            "tp":

                round(

                    entry+tp_distance,

                    2

                ),



            "atr":

                atr,



            "exit":

                None,



            "pnl":

                0,



            "signal_score":

                signal["score"],



            "confidence":

                signal["confidence"],



            "reason":

                signal["reason"]

        }





        print(

            "\n===== OPEN BUY ====="

        )


        print(

            self.position

        )








    # ==================================
    # Check Exit
    # ==================================

    def check_exit(
        self,
        candle
    ):


        if not self.position:

            return




        price = candle["close"]



        result=None





        if self.position["direction"]=="BUY":



            if price >= self.position["tp"]:


                result="WIN"



            elif price <= self.position["sl"]:


                result="LOSS"





        if result:



            self.close_trade(

                price,

                result

            )







    # ==================================
    # Close Trade
    # ==================================

    def close_trade(
        self,
        price,
        result
    ):


        trade=self.position



        trade["exit"]=price




        pnl=(

            price-trade["entry"]

        ) * trade["lot"] * 100





        trade["pnl"]=round(

            pnl,

            2

        )



        trade["result"]=result





        self.balance += pnl





        self.trades.append(

            trade.copy()

        )



        self.equity_curve.append(

            self.balance

        )




        print(

            "\n===== CLOSE ====="

        )


        print(

            trade

        )



        self.position=None







    # ==================================
    # Main Backtest
    # ==================================

    def run(self):


        print(

            "\n========== BACKTEST START =========="

        )




        window=[]




        for i,candle in enumerate(self.candles):



            print(

                f"\nCANDLE {i}"

            )



            window.append(

                candle

            )




            # maintain window size

            if len(window)>50:

                window.pop(0)





            # check existing position


            self.check_exit(

                candle

            )





            if self.position:

                continue





            context={


                "candles":

                    window



            }





            signal=self.entry_logic.generate_signal(

                context

            )





            print(

                "\n===== ICT SIGNAL ====="

            )


            print(

                signal

            )






            if signal["signal"]=="BUY":



                atr=self.calculate_atr(

                    window

                )



                self.open_position(

                    candle,

                    signal,

                    atr

                )






        # force close last position


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





        # Performance Analytics


        analyzer=PerformanceAnalyzer(

            self.trades,

            self.equity_curve

        )



        performance=analyzer.report()



        print(

            "\n========== PERFORMANCE =========="

        )


        print(

            performance

        )




        return result







    # ==================================
    # ATR Calculation
    # ==================================

    def calculate_atr(
        self,
        candles,
        period=14
    ):


        if len(candles)<period+1:

            return 10




        trs=[]



        for i in range(

            1,

            len(candles)

        ):


            high=candles[i]["high"]

            low=candles[i]["low"]


            previous=candles[i-1]["close"]




            tr=max(

                high-low,

                abs(high-previous),

                abs(low-previous)

            )


            trs.append(tr)





        atr=sum(

            trs[-period:]

        ) / period



        return round(

            atr,

            2

        )








    # ==================================
    # Report
    # ==================================

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





        win_rate=(

            wins/total*100

            if total

            else 0

        )




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