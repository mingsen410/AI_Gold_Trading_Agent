from smc_engine.order_block import OrderBlockDetector



engine = OrderBlockDetector()



candles=[


{

"open":3300,

"high":3305,

"low":3290,

"close":3295

},


{

"open":3300,

"high":3340,

"low":3300,

"close":3335

},


{

"open":3335,

"high":3350,

"low":3330,

"close":3345

}


]



result = engine.detect(
    candles
)


print(result)