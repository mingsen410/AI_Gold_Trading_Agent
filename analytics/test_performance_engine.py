from analytics.performance_engine import PerformanceEngine



trades=[


{

"result":"WIN",

"r_multiple":2

},


{

"result":"WIN",

"r_multiple":1.5

},


{

"result":"LOSS",

"r_multiple":-1

},


{

"result":"WIN",

"r_multiple":3

}


]



engine = PerformanceEngine(
    trades
)



report = engine.generate_report()


print(report)