from paper_trading.trade_position import TradePosition



class PaperAccount:


    def __init__(
        self,
        balance=10000
    ):

        self.balance = balance

        self.positions = []

        self.history = []




    # =========================
    # Check Existing Position
    # =========================

    def has_open_position(
        self
    ):


        for position in self.positions:


            if position.status == "OPEN":

                return True



        return False





    # =========================
    # Open Trade
    # =========================

    def open_trade(
        self,
        order
    ):


        position = TradePosition(

            order["symbol"],

            order["action"],

            order["entry"],

            order["volume"],

            order["sl"],

            order["tp"]

        )


        self.positions.append(position)


        return position





    # =========================
    # Update Candle
    # =========================

    def update_candle(
        self,
        candle
    ):


        closed = []



        for position in self.positions:



            if position.status != "OPEN":

                continue





            # ==================
            # BUY
            # ==================

            if position.direction == "BUY":



                if candle["low"] <= position.sl:


                    position.close(

                        position.sl

                    )



                elif candle["high"] >= position.tp:


                    position.close(

                        position.tp

                    )






            # ==================
            # SELL
            # ==================

            elif position.direction == "SELL":



                if candle["high"] >= position.sl:


                    position.close(

                        position.sl

                    )



                elif candle["low"] <= position.tp:


                    position.close(

                        position.tp

                    )







            if position.status == "CLOSED":


                self.history.append(position)


                closed.append(position)





        return closed