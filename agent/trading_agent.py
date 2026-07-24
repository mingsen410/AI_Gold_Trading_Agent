import time



from core.logger import AgentLogger



from data_engine.market_feed import MarketFeed


from data_engine.data_pipeline import DataPipeline



from agent.decision_engine import DecisionEngine


from agent.learning_engine import LearningEngine




class TradingAgent:



    def __init__(self):


        AgentLogger.info(

            "Initializing AI Trading Agent"

        )



        # Data Layer


        self.market_feed = MarketFeed()


        self.data_pipeline = DataPipeline()



        # Brain


        self.decision_engine = DecisionEngine()


        self.learning_engine = LearningEngine()



        self.running = False





    def initialize(self):


        """

        初始化系统

        """



        self.market_feed.connect()



        AgentLogger.info(

            "All systems initialized"

        )





    def analyze_market(self):


        """

        一个完整分析周期

        """



        # =====================

        # 1. Get Market Data

        # =====================



        tick = self.market_feed.get_tick()



        AgentLogger.info(

            f"Market Tick: {tick}"

        )





        # =====================

        # 2. Build Candle

        # =====================



        candle = self.data_pipeline.process_tick(

            tick

        )



        AgentLogger.info(

            f"Current Candle: {candle}"

        )





        # =====================

        # 3. Strategy Analysis

        # =====================



        # 暂时模拟

        # 后续连接SMC + ICT



        setup = {



            "signal":

            "NONE"

        }





        # =====================

        # 4. Decision

        # =====================



        decision = self.decision_engine.evaluate(

            bias=None,


            setup=setup,


            risk=True

        )




        AgentLogger.info(

            f"Decision: {decision}"

        )





    def start(self):



        self.initialize()



        self.running = True



        AgentLogger.info(

            "Trading Agent Running"

        )




        while self.running:



            self.analyze_market()



            time.sleep(60)





    def stop(self):


        self.running = False



        AgentLogger.info(

            "Agent stopped"

        )