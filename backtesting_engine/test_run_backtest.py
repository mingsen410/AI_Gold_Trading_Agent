from backtesting_engine.run_backtest import BacktestRunner



runner=BacktestRunner()



result = runner.run(

"backtesting_engine/sample_gold.csv"

)



print(result)