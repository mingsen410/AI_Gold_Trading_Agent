from backtest_engine.backtest_controller import BacktestController



candles=[


{

"time":"2026-01-01 09:00",

"open":3350,

"high":3360,

"low":3345,

"close":3355

},


{

"time":"2026-01-01 09:05",

"open":3355,

"high":3375,

"low":3350,

"close":3370

}


]



engine = BacktestController(
    candles
)



# 模拟AI之前产生BUY信号

engine.account.open_trade(

{

"symbol":"XAUUSD",

"action":"BUY",

"entry":3350,

"volume":1,

"sl":3340,

"tp":3370

}

)



result = engine.run()



print("BACKTEST RESULT")



for trade in result:

    print(trade.__dict__)