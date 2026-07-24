from core.logger import AgentLogger



class BacktestOrchestrator:


    def __init__(

        self,

        data_loader,

        quality_engine,

        replay_engine,

        strategy_engine,

        confidence_engine,

        filter_pipeline,

        execution_engine

    ):


        self.data_loader = data_loader

        self.quality_engine = quality_engine

        self.replay_engine = replay_engine

        self.strategy_engine = strategy_engine

        self.confidence_engine = confidence_engine

        self.filter_pipeline = filter_pipeline

        self.execution_engine = execution_engine



        self.trades = []



    def run(self):


        AgentLogger.info(
            "Backtest Started"
        )



        candles = self.data_loader.load()



        quality = self.quality_engine.check_dataset(
            candles
        )



        if quality["valid"] != quality["total"]:

            AgentLogger.info(
                "Data quality issues detected"
            )



        while self.replay_engine.has_next():


            candle = self.replay_engine.next()



            # 后续这里连接 ICT Strategy

            # 当前先建立流程



        AgentLogger.info(

            "Backtest Finished"

        )


        return self.trades