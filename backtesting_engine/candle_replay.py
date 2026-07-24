from core.logger import AgentLogger



class CandleReplayEngine:



    def __init__(
        self,
        candles
    ):


        self.candles = candles



    def replay(self):


        AgentLogger.info(

            f"Starting candle replay: {len(self.candles)} candles"

        )



        for index,candle in enumerate(
            self.candles
        ):



            yield {


                "index":

                index,


                "candle":

                candle


            }



        AgentLogger.info(

            "Candle replay finished"

        )