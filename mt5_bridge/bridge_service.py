from mt5_bridge.mt5_mock import MockMT5



class MT5BridgeService:



    def __init__(self):

        self.mt5=MockMT5()




    def start(self):

        return self.mt5.connect()




    def market_data(self):

        return self.mt5.get_tick()




    def execute_order(
        self,
        order
    ):

        return self.mt5.send_order(order)




    def positions(self):

        return self.mt5.get_positions()