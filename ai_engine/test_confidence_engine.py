from ai_engine.confidence_engine import ConfidenceEngine


engine = ConfidenceEngine()


setup = {


"setup_score":90,


"session":"LONDON",


"liquidity":"SSL_SWEEP",


"volatility":"NORMAL"


}



result = engine.calculate(
    setup
)


print(result)