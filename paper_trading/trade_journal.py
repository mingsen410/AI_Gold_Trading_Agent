class TradeJournal:


    def __init__(self):

        self.trades=[]




    def record(
        self,
        position
    ):

        self.trades.append({

            "symbol":
            position.symbol,


            "direction":
            position.direction,


            "entry":
            position.entry,


            "exit":
            position.exit_price,


            "pnl":
            position.pnl,


            "status":
            position.status

        })




    def show(self):

        return self.trades