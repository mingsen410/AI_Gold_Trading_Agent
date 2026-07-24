from smc_engine.liquidity import LiquidityEngine



engine = LiquidityEngine()



test_swings = [


    {
        "type":"HIGH",
        "price":3400
    },


    {
        "type":"LOW",
        "price":3350
    },


    {
        "type":"HIGH",
        "price":3402
    },


    {
        "type":"LOW",
        "price":3348
    }

]



result = engine.detect_liquidity(
    test_swings
)



print(result)