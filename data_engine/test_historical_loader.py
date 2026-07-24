from data_engine.historical_loader import HistoricalDataLoader



loader = HistoricalDataLoader(

    "data_engine/test_data.csv"

)



candles = loader.load()


print(candles)