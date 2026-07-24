from core.logger import AgentLogger


class YearlyAnalyzer:


    def __init__(
        self,
        trades
    ):

        self.trades = trades



    def group_by_year(self):


        yearly={}


        for trade in self.trades:


            year = trade["year"]


            if year not in yearly:

                yearly[year]=[]


            yearly[year].append(
                trade
            )


        return yearly



    def analyze_year(
        self,
        trades
    ):


        total = len(trades)


        wins = [

            t for t in trades

            if t["result"]=="WIN"

        ]


        total_R = sum(

            t["r_multiple"]

            for t in trades

        )


        win_rate = 0


        if total > 0:


            win_rate = (

                len(wins)

                /

                total

                *

                100

            )


        return {


            "trades":

            total,


            "win_rate":

            round(win_rate,2),


            "total_R":

            round(total_R,2)

        }



    def generate_report(self):


        grouped = self.group_by_year()


        report={}



        for year,trades in grouped.items():


            report[year]=self.analyze_year(
                trades
            )



        AgentLogger.info(

            "Yearly Backtest Report Generated"

        )


        return report