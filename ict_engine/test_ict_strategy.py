from datetime import time


from ict_engine.ict_strategy import ICTStrategyEngine

from ict_engine.market_bias import MarketBiasEngine

from ict_engine.setup_validator import SetupValidator

from ict_engine.session_engine import SessionEngine

from ai_engine.confidence_engine import ConfidenceEngine



strategy = ICTStrategyEngine(

    MarketBiasEngine(),

    SetupValidator(),

    ConfidenceEngine(),

    SessionEngine()

)



market_data = {


"time":

time(16,0),


"structure":

"BULLISH",


"bos":

True,


"choch":

"BULLISH",


"liquidity":

"SSL_SWEEP",


"fvg":

True,


"order_block":

True,


"zone":

"DISCOUNT",


"volatility":

"NORMAL"

}



result = strategy.analyze(
    market_data
)


print(result)