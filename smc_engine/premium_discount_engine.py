from core.logger import AgentLogger


class PremiumDiscountEngine:


    def __init__(self):

        self.buffer = 0



    # =====================================
    # ICT Premium / Discount Calculation
    #
    # Uses latest swing high and swing low
    #
    # High
    # |
    # | PREMIUM
    # |
    # 50% Equilibrium
    # |
    # | DISCOUNT
    # |
    # Low
    #
    # =====================================

    def calculate(
        self,
        swing_points,
        current_price
    ):


        try:


            highs = [

                x for x in swing_points

                if isinstance(x, dict)

                and x.get("type") == "HIGH"

            ]


            lows = [

                x for x in swing_points

                if isinstance(x, dict)

                and x.get("type") == "LOW"

            ]



            if len(highs) == 0 or len(lows) == 0:


                return {

                    "zone":

                    "UNKNOWN",

                    "reason":

                    "Missing swing points"

                }



            latest_high = highs[-1]["price"]

            latest_low = lows[-1]["price"]



            if latest_high <= latest_low:


                return {

                    "zone":

                    "UNKNOWN",

                    "reason":

                    "Invalid swing range"

                }



            equilibrium = (

                latest_high

                +

                latest_low

            ) / 2



            if current_price < equilibrium:


                zone = "DISCOUNT"



            elif current_price > equilibrium:


                zone = "PREMIUM"



            else:


                zone = "EQUILIBRIUM"



            result = {


                "zone":

                zone,


                "swing_high":

                latest_high,


                "swing_low":

                latest_low,


                "equilibrium":

                equilibrium,


                "current_price":

                current_price


            }



            AgentLogger.info(

                f"Premium Discount Analysis: {result}"

            )


            return result



        except Exception as e:


            AgentLogger.warning(

                f"Premium Discount failed: {e}"

            )


            return {


                "zone":

                "UNKNOWN"

            }