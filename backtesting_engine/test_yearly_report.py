from backtesting_engine.yearly_report import YearlyReportGenerator



trades=[


{

"year":2016,

"profit":200

},


{

"year":2016,

"profit":-100

},


{

"year":2017,

"profit":500

},


{

"year":2026,

"profit":300

}

]



engine=YearlyReportGenerator()



result=engine.generate(
    trades
)



print(result)