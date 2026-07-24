from replay_engine.market_replay import MarketReplayEngine



candles=[


{

"time":"2016-01-01 09:00",

"open":3300,

"high":3305,

"low":3298,

"close":3303

},


{

"time":"2016-01-01 09:05",

"open":3303,

"high":3310,

"low":3301,

"close":3308

}



]



engine = MarketReplayEngine(
    candles
)



while engine.has_next():


    candle = engine.next()


    print(candle)