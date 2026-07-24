from core.logger import AgentLogger



class MarketReplayEngine:


    def __init__(
        self,
        candles
    ):

        self.candles = candles

        self.index = 0

        self.current_candle = None



    def has_next(self):


        return self.index < len(
            self.candles
        )



    def next(self):


        if not self.has_next():

            return None



        self.current_candle = self.candles[
            self.index
        ]


        self.index += 1



        AgentLogger.info(

            f"Replay candle: {self.current_candle['time']}"

        )


        return self.current_candle



    def reset(self):


        self.index = 0

        self.current_candle = None