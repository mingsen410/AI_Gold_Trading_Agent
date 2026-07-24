class Position:


    def __init__(
        self,
        symbol,
        direction,
        entry,
        sl,
        tp
    ):

        self.symbol = symbol
        self.direction = direction

        self.entry = entry
        self.sl = sl
        self.tp = tp

        self.exit = None

        self.status = "OPEN"

        self.pnl = 0

        self.break_even = False



    def update(self, price):


        # BUY management

        if self.direction == "BUY":


            # Take Profit

            if price >= self.tp:

                self.close(
                    self.tp,
                    "WIN"
                )


            # Stop Loss

            elif price <= self.sl:

                self.close(
                    self.sl,
                    "LOSS"
                )


            # Break Even

            elif price >= self.entry + 20:

                if not self.break_even:

                    self.sl = self.entry

                    self.break_even=True



        # SELL management

        else:


            if price <= self.tp:

                self.close(
                    self.tp,
                    "WIN"
                )


            elif price >= self.sl:

                self.close(
                    self.sl,
                    "LOSS"
                )


   


    def close(
        self,
        price,
        status
    ):

        self.exit = price

        self.status=status


        if self.direction=="BUY":

            self.pnl = price-self.entry


        else:

            self.pnl = self.entry-price