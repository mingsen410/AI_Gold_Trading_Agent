from backtesting_engine.data_loader import HistoricalDataLoader

from backtesting_engine.candle_replay import CandleReplayEngine

from backtesting_engine.trade_simulator import TradeSimulator

from backtesting_engine.yearly_report import YearlyReportGenerator

from core.logger import AgentLogger



class BacktestRunner:



    def __init__(self):


        self.trades=[]



    def run(
        self,
        file_path
    ):


        AgentLogger.info(

            "Starting Backtest Engine"

        )



        loader = HistoricalDataLoader(

            file_path

        )


        candles = loader.load()



        replay = CandleReplayEngine(

            candles

        )



        simulator = TradeSimulator()



        for item in replay.replay():


            candle=item["candle"]


            # 这里未来连接真正 Strategy Engine


            signal=self.mock_strategy(
                candle
            )



            if signal:


                simulator.open_trade(
                    signal
                )


            if hasattr(
                simulator,
                "current_trade"
            ) and simulator.current_trade:


                result=simulator.check_exit(
                    candle
                )


                if result:

                    self.trades.append(
                        result
                    )



        report = YearlyReportGenerator().generate(

            self.trades

        )


        AgentLogger.info(

            "Backtest Finished"

        )


        return report




    def mock_strategy(
        self,
        candle
    ):


        return None