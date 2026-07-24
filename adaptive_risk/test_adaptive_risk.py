from adaptive_risk.adaptive_risk import AdaptiveRiskEngine



engine = AdaptiveRiskEngine()



result = engine.calculate(

    setup="A+",

    regime="TRENDING",

    drawdown=2,

    news_status="ALLOW"

)



print(result)