from reports.yearly_analyzer import YearlyAnalyzer



trades=[


{

"year":2016,

"result":"WIN",

"r_multiple":2

},


{

"year":2016,

"result":"LOSS",

"r_multiple":-1

},


{

"year":2017,

"result":"WIN",

"r_multiple":3

},


{

"year":2017,

"result":"WIN",

"r_multiple":2

},


{

"year":2020,

"result":"LOSS",

"r_multiple":-1

}


]



engine = YearlyAnalyzer(
    trades
)


report = engine.generate_report()


print(report)