class Performance:


    def __init__(self):

        self.trades=[]



    def add_trade(
        self,
        trade
    ):

        self.trades.append(trade)



    def report(self):


        total=len(
            self.trades
        )


        wins=[
            x for x in self.trades
            if x["status"]=="WIN"
        ]


        losses=[
            x for x in self.trades
            if x["status"]=="LOSS"
        ]


        profit=sum(
            x["pnl"]
            for x in self.trades
        )


        win_rate=(
            len(wins)/total*100
            if total
            else 0
        )


        gross_profit=sum(
            x["pnl"]
            for x in wins
        )


        gross_loss=abs(
            sum(
                x["pnl"]
                for x in losses
            )
        )


        if gross_loss==0:

            profit_factor="INF"

        else:

            profit_factor=round(
                gross_profit/gross_loss,
                2
            )


        return {


            "total_trades":
                total,


            "wins":
                len(wins),


            "losses":
                len(losses),


            "win_rate":
                round(
                    win_rate,
                    2
                ),


            "profit":
                profit,


            "profit_factor":
                profit_factor

        }