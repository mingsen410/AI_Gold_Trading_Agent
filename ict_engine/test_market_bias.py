from ict_engine.market_bias import MarketBiasEngine

engine = MarketBiasEngine()

result = engine.calculate(
    structure="BULLISH",
    bos=True,
    choch="BULLISH"
)

print(result)