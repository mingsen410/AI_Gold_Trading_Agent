from smc_engine.liquidity_engine import LiquidityEngine



candles = [


    {
        "time":"09:00",
        "open":3380,
        "high":3400,
        "low":3375,
        "close":3395
    },


    {
        "time":"09:05",
        "open":3395,
        "high":3402,
        "low":3385,
        "close":3388
    },


    {
        "time":"09:10",
        "open":3388,
        "high":3405,
        "low":3380,
        "close":3398
    }

]



swing_points = [


    {
        "type":"HIGH",
        "price":3400,
        "index":1
    },


    {
        "type":"HIGH",
        "price":3402,
        "index":2
    },


    {
        "type":"LOW",
        "price":3380,
        "index":3
    },


    {
        "type":"LOW",
        "price":3381,
        "index":4
    }


]



engine = LiquidityEngine()



result = engine.analyze(

    candles,

    swing_points

)



print("\n========== LIQUIDITY ==========\n")

print(result)