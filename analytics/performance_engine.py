from core.logger import AgentLogger



class PerformanceEngine:


    def __init__(
        self,
        trades
    ):

        self.trades = trades



    def total_trades(self):

        return len(
            self.trades
        )



    def win_rate(self):

        if len(self.trades)==0:

            return 0


        wins = [

            t for t in self.trades

            if t["result"]=="WIN"

        ]


        return round(

            len(wins)
            /
            len(self.trades)
            *
            100,

            2

        )



    def total_R(self):


        total = sum(

            t["r_multiple"]

            for t in self.trades

        )


        return round(
            total,
            2
        )



    def profit_factor(self):


        profits = sum(

            t["r_multiple"]

            for t in self.trades

            if t["r_multiple"] > 0

        )


        losses = abs(sum(

            t["r_multiple"]

            for t in self.trades

            if t["r_multiple"] < 0

        ))


        if losses == 0:

            return None


        return round(

            profits / losses,

            2

        )



    def generate_report(self):


        report={


            "total_trades":

            self.total_trades(),


            "win_rate":

            self.win_rate(),


            "total_R":

            self.total_R(),


            "profit_factor":

            self.profit_factor()

        }


        AgentLogger.info(
            "Performance Report Generated"
        )


        return report