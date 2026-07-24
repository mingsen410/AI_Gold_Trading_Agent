from mtf_engine.mtf_analysis import MultiTimeframeAnalyzer



engine = MultiTimeframeAnalyzer()



data={


"daily":
{
"trend":"UP"
},


"h4":
{
"trend":"UP"
},


"h1":
{
"trend":"UP"
},


"m15":
{
"trend":"DOWN"
},


"m5":
{
"trend":"UP"
}

}



result = engine.analyze(
    data
)



print(result)