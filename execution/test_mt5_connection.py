from execution.mt5_connection import MT5Connection



mt5 = MT5Connection()



result = mt5.connect()



print(result)



print(
    mt5.status()
)