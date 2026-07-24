from core.logger import AgentLogger


from data_engine.candle_manager import CandleManager




class DataPipeline:



    def __init__(self):


        self.candle_manager = CandleManager()


        self.current_candle = {}





    def process_tick(

        self,

        tick,

        timeframe="M1"

    ):



        price = tick["price"]



        """

        简化版本：

        将tick转换为K线



        后续升级:

        根据真实时间生成M1/M5/H1

        """



        if not self.current_candle:



            self.current_candle = {


                "open":

                price,


                "high":

                price,


                "low":

                price,


                "close":

                price


            }



        else:



            self.current_candle["high"] = max(

                self.current_candle["high"],

                price

            )



            self.current_candle["low"] = min(

                self.current_candle["low"],

                price

            )



            self.current_candle["close"] = price





        return self.current_candle





    def close_candle(

        self,

        timeframe="M1"

    ):



        if self.current_candle:



            self.candle_manager.add_candle(

                timeframe,

                self.current_candle

            )



            AgentLogger.info(

                f"{timeframe} candle created"

            )



            self.current_candle = {}



            return True




        return False