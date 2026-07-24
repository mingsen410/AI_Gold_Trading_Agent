from core.logger import AgentLogger



class HistoricalReplayEngine:


    def __init__(
        self,
        candles
    ):

        self.candles = candles

        self.index = 0




    def has_next(self):

        return (

            self.index < len(self.candles)

        )




    def next_candle(self):


        if not self.has_next():

            return None



        candle = self.candles[self.index]


        self.index += 1



        AgentLogger.info(

            f"Replay Candle {self.index}: {candle}"

        )


        return candle




    def reset(self):

        self.index = 0