from data_engine.candle_manager import CandleManager



manager = CandleManager()



manager.add_candle(

"M15",

{


"open":3350,


"high":3360,


"low":3345,


"close":3358


}

)



manager.add_candle(

"M15",

{


"open":3358,


"high":3365,


"low":3355,


"close":3362


}

)



print(

manager.get_candles(

"M15"

)

)



print(

manager.calculate_range(

"M15"

)

)