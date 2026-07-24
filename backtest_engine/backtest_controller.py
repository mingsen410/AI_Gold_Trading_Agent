from historical_replay.replay_engine import HistoricalReplayEngine

from paper_trading.paper_account import PaperAccount

from backtest_engine.strategy_runner import StrategyRunner




class BacktestController:



    def __init__(
        self,
        candles,
        initial_balance=10000
    ):


        self.replay = HistoricalReplayEngine(
            candles
        )


        self.account = PaperAccount(
            initial_balance
        )


        self.strategy = StrategyRunner()


        self.pending_orders = []





    def execute_pending_orders(
        self,
        candle
    ):


        for order in self.pending_orders:


            self.account.open_trade(
                order
            )


        self.pending_orders.clear()





    def create_order(
        self,
        signal,
        candle
    ):


        if signal["signal"] == "BUY":


            return {


                "symbol":"XAUUSD",

                "action":"BUY",

                "entry":candle["close"],

                "volume":1,

                "sl":candle["close"]-10,

                "tp":candle["close"]+20

            }




        elif signal["signal"] == "SELL":


            return {


                "symbol":"XAUUSD",

                "action":"SELL",

                "entry":candle["close"],

                "volume":1,

                "sl":candle["close"]+10,

                "tp":candle["close"]-20

            }


        return None





    def run(self):


        results=[]


        while self.replay.has_next():


            candle = self.replay.next_candle()



            # ======================
            # 1. Execute old signals
            # ======================

            self.execute_pending_orders(
                candle
            )




            # ======================
            # 2. Manage positions
            # ======================

            closed = self.account.update_candle(
                candle
            )


            if closed:

                results.extend(
                    closed
                )





            # ======================
            # 3. Analyze market
            # ======================

            signal = self.strategy.get_signal(
                candle
            )




            # ======================
            # 4. Create next order
            # ======================

            order = self.create_order(

                signal,

                candle

            )


            if order:

                self.pending_orders.append(
                    order
                )



        return results