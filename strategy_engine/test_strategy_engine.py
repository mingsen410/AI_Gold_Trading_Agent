from strategy_engine.strategy_controller import StrategyController



controller = StrategyController()



candles=[


{

"time":"2026-01-01 09:00",

"open":3350,

"high":3360,

"low":3345,

"close":3358

}


]



result = controller.analyze(
    candles
)



print(result)