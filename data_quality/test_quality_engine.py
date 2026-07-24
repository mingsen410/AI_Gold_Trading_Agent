from data_quality.quality_engine import DataQualityEngine



engine = DataQualityEngine()



candles=[


{

"open":3300,

"high":3310,

"low":3295,

"close":3305

},



{

"open":3300,

"high":3290,

"low":3305,

"close":3302

}


]



result = engine.check_dataset(
    candles
)


print(result)