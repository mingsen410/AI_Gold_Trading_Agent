import time

from core.logger import AgentLogger



class LiveTradingAgent:



    def __init__(

        self,

        mt5_connector,

        execution_engine

    ):


        self.mt5 = mt5_connector

        self.execution = execution_engine


        self.running = False



    def start(self):


        self.running = True


        AgentLogger.info(

            "Live Trading Agent Started"

        )


        while self.running:


            self.run_cycle()


            time.sleep(5)



    def run_cycle(self):


        price = self.mt5.get_price(
            "XAUUSD"
        )


        if price is None:


            AgentLogger.info(
                "No price data"
            )


            return



        AgentLogger.info(

            f"Current price: {price}"

        )


        # 后续连接：

        # Market Structure

        # ICT Setup

        # AI Confidence

        # Trade Filter



    def stop(self):


        self.running = False


        AgentLogger.info(

            "Agent stopped"

        )