from core.logger import AgentLogger



class MT5Connector:



    def __init__(self):

        self.connected = False

        self.account = None



    def connect(
        self,
        account=None
    ):


        self.connected = True

        self.account = account


        AgentLogger.info(

            "MT5 connection established"

        )


        return True



    def disconnect(self):


        self.connected = False


        AgentLogger.info(

            "MT5 disconnected"

        )



    def get_account_info(self):


        if not self.connected:


            return None



        return {


            "balance":10000,

            "equity":10000,

            "currency":"USD"

        }



    def get_price(
        self,
        symbol
    ):


        if not self.connected:

            return None



        return {


            "symbol":symbol,

            "bid":3350.5,

            "ask":3350.8

        }



    def send_order(
        self,
        order
    ):


        if not self.connected:


            return {


            "status":"FAILED",

            "reason":"Not connected"

            }



        AgentLogger.info(

            f"Order sent: {order}"

        )


        return {


            "status":"SUCCESS",

            "ticket":123456

        }