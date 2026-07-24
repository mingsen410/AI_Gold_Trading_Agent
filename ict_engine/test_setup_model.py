from ict_engine.setup_model import ICTSetupModel



engine = ICTSetupModel()



bias = {


"bias":

"BULLISH"

}




liquidity = {


"BSL":[],

"SSL":[

{"price":3300}

]

}




fvg = {


"bullish":[

{

"top":3310,

"bottom":3300

}

],

"bearish":[]

}




killzone = {


"active":

True

}





result = engine.generate_signal(

bias,

liquidity,

fvg,

killzone

)



print(result)