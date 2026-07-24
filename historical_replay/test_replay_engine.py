from historical_replay.replay_engine import HistoricalReplayEngine



candles=[


{

"open":3350,

"high":3360,

"low":3345,

"close":3355

},


{

"open":3355,

"high":3370,

"low":3350,

"close":3365

}


]



engine = HistoricalReplayEngine(
    candles
)



while engine.has_next():


    candle = engine.next_candle()


    print(candle)