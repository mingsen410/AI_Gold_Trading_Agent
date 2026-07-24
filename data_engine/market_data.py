from datetime import datetime
from core.logger import AgentLogger



class MarketData:


    def __init__(self):


        self.symbol = "XAUUSD"


        self.timeframe = "M5"



    def get_price(self):


        """
        获取当前价格
        """

        price = {


            "symbol":
            self.symbol,


            "bid":
            0,


            "ask":
            0,


            "time":
            datetime.now()


        }



        AgentLogger.info(
            f"Market data updated: {price}"
        )


        return price