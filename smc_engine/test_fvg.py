from smc_engine.fvg import FVGDetector



engine = FVGDetector()



candles = [


    {

        "open":3290,

        "high":3300,

        "low":3288,

        "close":3298

    },


    {


        "open":3305,

        "high":3320,

        "low":3305,

        "close":3318

    },


    {


        "open":3320,

        "high":3330,

        "low":3310,

        "close":3328

    }


]



result = engine.detect(
    candles
)


print(result)