from core.logger import AgentLogger

import random

import time




class MarketFeed:



    def __init__(self):


        self.symbol = "XAUUSD"


        self.connected = False




    def connect(self):


        """

        后续替换真实MT5连接

        """



        self.connected = True



        AgentLogger.info(

            "Market Feed Connected"

        )



        return True






    def get_tick(self):


        """

        当前价格


        测试阶段模拟黄金价格


        """



        price = round(

            3350 + random.uniform(-5,5),

            2

        )



        tick = {


            "symbol":

            self.symbol,


            "price":

            price,


            "time":

            time.time()

        }




        return tick