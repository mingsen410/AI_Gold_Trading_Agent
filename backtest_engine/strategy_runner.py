from strategy_engine.strategy_controller import StrategyController



class StrategyRunner:



    def __init__(self):

        self.strategy = StrategyController()



    def get_signal(
        self,
        candle
    ):

        return self.strategy.analyze(
            candle
        )