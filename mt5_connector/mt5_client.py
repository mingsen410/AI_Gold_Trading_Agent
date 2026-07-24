class MT5Client:


    def __init__(self):

        self.connected=False



    def connect(self):

        print(
            "MT5 connection placeholder"
        )

        self.connected=True

        return True



    def get_price(
        self,
        symbol="XAUUSD"
    ):

        return {

            "symbol":symbol,

            "bid":0,

            "ask":0

        }



    def get_candles(
        self,
        symbol="XAUUSD",
        timeframe="M5",
        count=100
    ):


        return []



    def send_order(
        self,
        order
    ):


        print(
            "Order placeholder:",
            order
        )


        return {

            "status":
                "simulation"

        }