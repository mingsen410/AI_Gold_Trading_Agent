from core.logger import AgentLogger




class MarketOrderEngine:



    def __init__(

        self,

        magic_number=20260723

    ):


        self.magic_number = magic_number


        self.orders = []





    def create_order_request(

        self,

        symbol,

        direction,

        volume,

        entry,

        stop_loss,

        take_profit

    ):



        order = {



            "symbol":

            symbol,



            "direction":

            direction,



            "volume":

            volume,



            "entry":

            entry,



            "stop_loss":

            stop_loss,



            "take_profit":

            take_profit,



            "magic":

            self.magic_number,



            "comment":

            "ICT_SMC_AGENT"

        }



        AgentLogger.info(

            f"Order Created: {order}"

        )



        return order





    def execute_order(

        self,

        order

    ):



        """

        目前模拟执行


        后续连接MT5:

        mt5.order_send()

        """



        try:



            self.orders.append(

                order

            )



            AgentLogger.info(

                "Order Executed Successfully"

            )



            return {



                "status":

                "SUCCESS",



                "order":

                order

            }




        except Exception as e:



            AgentLogger.error(

                f"Order Failed: {e}"

            )



            return {


                "status":

                "FAILED"

            }