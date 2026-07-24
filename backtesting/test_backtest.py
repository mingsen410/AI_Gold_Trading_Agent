from backtesting.engine import BacktestEngine
from core.entry_logic import ICTEntryLogic
from backtesting.data_generator import generate_xauusd_data



candles = generate_xauusd_data(

    candles=1000,

    start_price=3350

)



engine = BacktestEngine(

    candles,

    ICTEntryLogic()

)



result = engine.run()



print(
"\n========== RESULT =========="
)


print(
result
)