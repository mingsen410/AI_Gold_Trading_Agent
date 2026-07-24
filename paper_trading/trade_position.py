class TradePosition:


    def __init__(
        self,
        symbol,
        direction,
        entry,
        volume,
        sl,
        tp
    ):


        self.symbol = symbol

        self.direction = direction


        # Entry
        self.entry = entry


        # Volume
        self.volume = volume

        self.initial_volume = volume



        # Risk
        self.initial_stop_loss = sl

        self.sl = sl

        self.tp = tp



        # State

        self.status = "OPEN"

        self.state = "OPEN"



        # Management flags

        self.breakeven_done = False

        self.partial_closed = False

        self.trailing_active = False



        # Exit

        self.exit_price = None

        self.pnl = 0




    def reduce_volume(
        self,
        amount
    ):


        self.volume -= amount


        if self.volume < 0:

            self.volume = 0





    def close(
        self,
        price
    ):


        self.exit_price = price


        if self.direction == "BUY":


            self.pnl = (

                price -

                self.entry

            ) * self.volume




        elif self.direction == "SELL":


            self.pnl = (

                self.entry -

                price

            ) * self.volume



        self.status = "CLOSED"

        self.state = "CLOSED"