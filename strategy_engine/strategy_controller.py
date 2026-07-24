from strategy_engine.signal_generator import SignalGenerator

from market_context.context_builder import MarketContextBuilder



class StrategyController:



    def __init__(self):


        self.signal_engine = SignalGenerator()

        self.context_builder = MarketContextBuilder()




    def analyze(
        self,
        candles
    ):


        market_data = self.context_builder.build(
            candles
        )



        # temporary ICT/SMC output


        ict_result = "BULLISH"


        smc_result = "BULLISH"



        risk_result = "PASS"



        signal = self.signal_engine.generate(

            ict_result,

            smc_result,

            risk_result

        )



        signal["market_data"] = market_data


        return signal