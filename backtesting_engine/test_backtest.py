from backtesting_engine.data_loader import HistoricalDataLoader



loader = HistoricalDataLoader(

    "backtesting_engine/sample_gold.csv"

)


data = loader.load()


print(data)