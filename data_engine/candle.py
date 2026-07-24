from core.logger import AgentLogger



class Candle:


    def __init__(
        self,
        open_price,
        high,
        low,
        close,
        volume
    ):


        self.open = open_price

        self.high = high

        self.low = low

        self.close = close

        self.volume = volume



    def get_data(self):


        return {


            "open":
            self.open,


            "high":
            self.high,


            "low":
            self.low,


            "close":
            self.close,


            "volume":
            self.volume


        }