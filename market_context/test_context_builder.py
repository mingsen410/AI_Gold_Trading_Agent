from market_context.context_builder import MarketContextBuilder
from smc_engine.swing_detector import SwingDetector



# =====================================
# Test Candles
# =====================================


candles = [

    {
        "time":"09:00",
        "open":3350,
        "high":3360,
        "low":3348,
        "close":3358
    },


    {
        "time":"09:05",
        "open":3358,
        "high":3375,
        "low":3355,
        "close":3372
    },


    {
        "time":"09:10",
        "open":3372,
        "high":3390,
        "low":3368,
        "close":3388
    },


    {
        "time":"09:15",
        "open":3388,
        "high":3389,
        "low":3360,
        "close":3365
    },


    {
        "time":"09:20",
        "open":3365,
        "high":3370,
        "low":3345,
        "close":3350
    },


    {
        "time":"09:25",
        "open":3350,
        "high":3370,
        "low":3348,
        "close":3368
    },


    {
        "time":"09:30",
        "open":3368,
        "high":3385,
        "low":3365,
        "close":3382
    },


    {
        "time":"09:35",
        "open":3382,
        "high":3400,
        "low":3378,
        "close":3398
    },


    {
        "time":"09:40",
        "open":3398,
        "high":3402,
        "low":3375,
        "close":3380
    },


    {
        "time":"09:45",
        "open":3380,
        "high":3385,
        "low":3368,
        "close":3372
    },


    {
        "time":"09:50",
        "open":3372,
        "high":3415,
        "low":3370,
        "close":3410
    },


    {
        "time":"09:55",
        "open":3410,
        "high":3430,
        "low":3405,
        "close":3428
    },


    # buffer candles
    # allow final swing confirmation

    {
        "time":"10:00",
        "open":3428,
        "high":3435,
        "low":3420,
        "close":3432
    },


    {
        "time":"10:05",
        "open":3432,
        "high":3438,
        "low":3425,
        "close":3430
    },


    {
        "time":"10:10",
        "open":3430,
        "high":3433,
        "low":3418,
        "close":3420
    }

]



# =====================================
# Test Swing Detector
# =====================================


detector = SwingDetector()


swings = detector.detect(
    candles
)



print("\n========== SWING POINTS ==========\n")

print(swings)



# =====================================
# Test Market Context
# =====================================


builder = MarketContextBuilder()



context = builder.build(
    candles
)



print("\n========== MARKET CONTEXT ==========\n")

print(context)



print("\n========== STRUCTURE ==========\n")

print(
    context["structure"]
)



print("\n========== CHOCH ==========\n")

print(
    context["choch"]
)



print("\n========== FVG ==========\n")

print(
    context["fvg"]
)



print("\n========== ORDER BLOCK ==========\n")

print(
    context["order_block"]
)