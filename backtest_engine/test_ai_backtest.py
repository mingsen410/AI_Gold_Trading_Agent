from backtest_engine.backtest_controller import BacktestController



candles=[


{

"time":"2026-01-01 09:00",

"open":3350,

"high":3360,

"low":3345,

"close":3358

},


{

"time":"2026-01-01 09:05",

"open":3358,

"high":3385,

"low":3355,

"close":3380

}


]



engine = BacktestController(
    candles
)


result = engine.run()



print("AI BACKTEST RESULT")


for trade in result:

    print(
        trade.__dict__
    )