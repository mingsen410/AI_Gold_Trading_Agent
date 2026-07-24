import math



class PerformanceAnalyzer:


    def __init__(
        self,
        trades,
        equity_curve
    ):

        self.trades = trades
        self.equity_curve = equity_curve



    # ==========================
    # Average Win
    # ==========================

    def average_win(self):

        wins = [

            t["pnl"]

            for t in self.trades

            if t["pnl"] > 0

        ]


        if not wins:

            return 0


        return round(
            sum(wins) / len(wins),
            2
        )



    # ==========================
    # Average Loss
    # ==========================

    def average_loss(self):

        losses = [

            t["pnl"]

            for t in self.trades

            if t["pnl"] < 0

        ]


        if not losses:

            return 0


        return round(
            sum(losses) / len(losses),
            2
        )



    # ==========================
    # Profit Factor
    # ==========================

    def profit_factor(self):


        gross_profit = sum(

            t["pnl"]

            for t in self.trades

            if t["pnl"] > 0

        )


        gross_loss = abs(sum(

            t["pnl"]

            for t in self.trades

            if t["pnl"] < 0

        ))



        if gross_loss == 0:

            return "INF"



        return round(

            gross_profit / gross_loss,

            2

        )



    # ==========================
    # Maximum Drawdown
    # ==========================

    def max_drawdown(self):


        if not self.equity_curve:

            return 0



        peak = self.equity_curve[0]

        max_drawdown = 0



        for equity in self.equity_curve:


            if equity > peak:

                peak = equity



            drawdown = (

                peak - equity

            ) / peak * 100



            if drawdown > max_drawdown:

                max_drawdown = drawdown



        return round(
            max_drawdown,
            2
        )



    # ==========================
    # Sharpe Ratio
    # ==========================

    def sharpe_ratio(self):


        if len(self.equity_curve) < 2:

            return 0



        returns=[]


        for i in range(
            1,
            len(self.equity_curve)
        ):


            change = (

                self.equity_curve[i]

                -

                self.equity_curve[i-1]

            )


            returns.append(change)



        mean = sum(returns) / len(returns)



        variance = sum(

            (x-mean)**2

            for x in returns

        ) / len(returns)



        std = math.sqrt(
            variance
        )


        if std == 0:

            return 0



        return round(
            mean/std,
            2
        )



    # ==========================
    # Risk Reward
    # ==========================

    def risk_reward(self):


        avg_win = self.average_win()

        avg_loss = abs(
            self.average_loss()
        )


        if avg_loss == 0:

            return "INF"



        return round(

            avg_win / avg_loss,

            2

        )



    # ==========================
    # Strategy Rating
    # ==========================

    def rating(self):


        score = 0



        pf = self.profit_factor()


        if pf != "INF":


            if pf >= 2:

                score += 2


            elif pf >=1:

                score +=1




        dd = self.max_drawdown()



        if dd < 10:

            score +=2


        elif dd <20:

            score +=1




        rr = self.risk_reward()



        if rr != "INF":


            if rr >=2:

                score +=2



        if score >=5:

            return "A"


        elif score >=3:

            return "B"


        else:

            return "C"



    # ==========================
    # Final Report
    # ==========================

    def report(self):


        return {


            "average_win":

                self.average_win(),



            "average_loss":

                self.average_loss(),



            "risk_reward":

                self.risk_reward(),



            "profit_factor":

                self.profit_factor(),



            "max_drawdown_%":

                self.max_drawdown(),



            "sharpe_ratio":

                self.sharpe_ratio(),



            "strategy_rating":

                self.rating()

        }