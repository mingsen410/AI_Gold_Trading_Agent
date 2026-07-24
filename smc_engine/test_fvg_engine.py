from smc_engine.fvg_engine import FVGEngine





engine = FVGEngine()




candles=[


{

"high":3350,

"low":3340,

"close":3348

},


{

"high":3370,

"low":3360,

"close":3368

},


{

"high":3385,

"low":3380,

"close":3383

}


]





result = engine.detect(

candles

)



print(result)