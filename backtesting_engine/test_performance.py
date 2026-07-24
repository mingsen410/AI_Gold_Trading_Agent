from backtesting_engine.performance import PerformanceAnalyzer



trades=[


{

"profit":200

},


{

"profit":-100

},


{

"profit":300

},


{

"profit":-50

}

]



engine=PerformanceAnalyzer()



result=engine.analyze(
    trades
)



print(result)