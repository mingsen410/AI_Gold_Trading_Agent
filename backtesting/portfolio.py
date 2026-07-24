class Portfolio:


    def __init__(self):

        self.position=None



    def open(
        self,
        trade
    ):

        self.position=trade



    def close(self):

        trade=self.position

        self.position=None

        return trade



    def has_position(self):

        return (
            self.position
            is not None
        )