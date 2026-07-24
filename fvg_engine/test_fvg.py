from fvg_engine.fvg_detector import FVGDetector



engine = FVGDetector()



candles=[


{

"high":3300,

"low":3280,

"close":3295

},


{

"high":3320,

"low":3310,

"close":3318

},


{

"high":3340,

"low":3310,

"close":3335

}

]



result = engine.detect(
    candles
)


print(result)