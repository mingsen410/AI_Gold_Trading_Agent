from liquidity_engine.liquidity import LiquidityEngine



engine = LiquidityEngine()



candles=[


{

"high":3350,

"low":3330,

"close":3340

},


{

"high":3352,

"low":3335,

"close":3345

}

]



print(

engine.detect_equal_highs(
    candles
)

)



candle={


"high":3355,

"low":3340,

"close":3348

}



print(

engine.detect_sweep(

candle,

3350

)

)