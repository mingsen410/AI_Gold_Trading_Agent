from smc_engine.choch_detector import CHoCHDetector




engine = CHoCHDetector()




candles = [


{

"high":3400,

"low":3370,

"close":3380

},


{

"high":3390,

"low":3360,

"close":3370

},


{

"high":3410,

"low":3380,

"close":3405

}


]





result = engine.detect(

"BEARISH",

candles

)



print(result)