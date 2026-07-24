from core.logger import AgentLogger

from collections import defaultdict

from backtesting_engine.performance import PerformanceAnalyzer



class YearlyReportGenerator:



    def __init__(
        self,
        starting_balance=10000
    ):


        self.starting_balance = starting_balance




    def group_by_year(
        self,
        trades
    ):


        yearly={}



        for trade in trades:


            year = trade["year"]



            if year not in yearly:


                yearly[year]=[]



            yearly[year].append(
                trade
            )


        return yearly





    def generate(
        self,
        trades
    ):


        yearly_data=self.group_by_year(
            trades
        )


        reports={}



        for year,year_trades in yearly_data.items():


            analyzer=PerformanceAnalyzer(

                self.starting_balance

            )


            reports[year]=analyzer.analyze(

                year_trades

            )



        total_analyzer=PerformanceAnalyzer(

            self.starting_balance

        )


        reports["TOTAL"]=total_analyzer.analyze(

            trades

        )



        AgentLogger.info(

            f"Yearly Report Generated: {reports}"

        )


        return reports