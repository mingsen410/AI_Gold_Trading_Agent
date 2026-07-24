from market_regime.regime_detector import MarketRegimeDetector



engine = MarketRegimeDetector()



data={


"ma20":3350,

"ma50":3320,

"atr":15,

"average_atr":10,

"bos":3,

"volume_increase":True

}



result = engine.detect(
    data
)



print(result)