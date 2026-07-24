from backtesting_engine.trade_simulator import TradeSimulator



engine = TradeSimulator()



signal={


"type":"BUY",


"entry":3300,


"stop_loss":3290,


"take_profit":3320

}



engine.open_trade(
    signal
)



candle={


"high":3325,


"low":3310,


"close":3320

}



result = engine.check_exit(
    candle
)



print(result)