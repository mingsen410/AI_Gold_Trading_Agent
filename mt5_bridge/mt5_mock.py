from core.logger import AgentLogger



class MockMT5:



    def __init__(self):

        self.connected=False

        self.positions=[]




    def connect(self):

        self.connected=True


        AgentLogger.info(

            "Mock MT5 Connected"

        )


        return True




    def get_tick(
        self,
        symbol="XAUUSD"
    ):


        return {


            "symbol":symbol,

            "bid":3350.20,

            "ask":3350.45

        }




    def send_order(
        self,
        order
    ):


        self.positions.append(order)


        AgentLogger.info(

            f"Mock Order Executed: {order}"

        )


        return {


            "status":
            "filled",

            "order":
            order

        }




    def get_positions(self):


        return self.positions