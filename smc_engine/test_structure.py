from smc_engine.market_structure import MarketStructure



structure = MarketStructure()



test_swings = [


    {
        "type":"LOW",
        "price":3300
    },


    {
        "type":"HIGH",
        "price":3350
    },


    {
        "type":"LOW",
        "price":3320
    },


    {
        "type":"HIGH",
        "price":3380
    }


]



result = structure.analyze(
    test_swings
)


print(result)