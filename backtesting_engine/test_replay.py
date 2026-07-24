from backtesting_engine.data_loader import HistoricalDataLoader

from backtesting_engine.candle_replay import CandleReplayEngine



loader = HistoricalDataLoader(

"backtesting_engine/sample_gold.csv"

)



candles = loader.load()



replay = CandleReplayEngine(
    candles
)



for item in replay.replay():


    print(item)