from core.logger import AgentLogger





class PremiumDiscountEngine:



    def __init__(self):


        self.zone=None






    def calculate_zone(

        self,

        swing_high,

        swing_low,

        current_price

    ):



        """

        计算当前价格区域



        swing_high:

        最近高点



        swing_low:

        最近低点

        """



        equilibrium = (

            swing_high +

            swing_low

        ) / 2





        if current_price > equilibrium:



            self.zone="PREMIUM"



        else:



            self.zone="DISCOUNT"





        return {



            "zone":

            self.zone,



            "equilibrium":

            round(

                equilibrium,

                2

            ),



            "current_price":

            current_price

        }