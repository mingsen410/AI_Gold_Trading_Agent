from trading_system.trading_controller import TradingController



candles = [


{
"time":"09:00",
"open":3300,
"high":3310,
"low":3290,
"close":3305
},


{
"time":"09:05",
"open":3305,
"high":3325,
"low":3300,
"close":3320
},


{
"time":"09:10",
"open":3320,
"high":3340,
"low":3315,
"close":3335
},


{
"time":"09:15",
"open":3335,
"high":3360,
"low":3330,
"close":3355
},


{
"time":"09:20",
"open":3355,
"high":3365,
"low":3340,
"close":3345
},


{
"time":"09:25",
"open":3345,
"high":3355,
"low":3325,
"close":3330
},


{
"time":"09:30",
"open":3330,
"high":3375,
"low":3328,
"close":3370
},


{
"time":"09:35",
"open":3370,
"high":3405,
"low":3365,
"close":3400
},


{
"time":"09:40",
"open":3400,
"high":3410,
"low":3350,
"close":3360
},


{
"time":"09:45",
"open":3360,
"high":3385,
"low":3355,
"close":3380
}


]



controller = TradingController()


result = controller.process(
    candles
)



print("\n===== FINAL PIPELINE RESULT =====\n")

print(result)