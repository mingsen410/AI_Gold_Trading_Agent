from core.logger import AgentLogger



class LiquidityEngine:


    def __init__(
        self,
        tolerance=0.001
    ):

        """
        tolerance:

        判断两个价格是否接近

        0.001 = 0.1%

        """

        self.tolerance = tolerance



    def is_equal_price(
        self,
        price1,
        price2
    ):


        difference = abs(
            price1 - price2
        )


        average = (
            price1 + price2
        ) / 2



        if average == 0:

            return False



        return (

            difference / average

        ) <= self.tolerance




    def detect_equal_highs(
        self,
        swing_points
    ):


        equal_highs = []



        highs = [

            x for x in swing_points

            if x["type"] == "HIGH"

        ]



        for i in range(
            len(highs)-1
        ):


            current = highs[i]

            next_high = highs[i+1]



            if self.is_equal_price(

                current["price"],

                next_high["price"]

            ):


                equal_highs.append({


                    "type":
                    "EQH",


                    "price":

                    (
                        current["price"]

                        +

                        next_high["price"]

                    )

                    /2,


                    "points":

                    [
                        current,
                        next_high
                    ]


                })



        AgentLogger.info(

            f"Detected EQH: {len(equal_highs)}"

        )


        return equal_highs




    def detect_equal_lows(
        self,
        swing_points
    ):


        equal_lows = []



        lows = [

            x for x in swing_points

            if x["type"] == "LOW"

        ]



        for i in range(
            len(lows)-1
        ):


            current = lows[i]

            next_low = lows[i+1]



            if self.is_equal_price(

                current["price"],

                next_low["price"]

            ):


                equal_lows.append({


                    "type":
                    "EQL",


                    "price":

                    (
                        current["price"]

                        +

                        next_low["price"]

                    )

                    /2,


                    "points":

                    [
                        current,
                        next_low
                    ]


                })



        AgentLogger.info(

            f"Detected EQL: {len(equal_lows)}"

        )


        return equal_lows




    def detect_liquidity(
        self,
        swing_points
    ):


        liquidity = {


            "BSL":

            self.detect_equal_highs(
                swing_points
            ),


            "SSL":

            self.detect_equal_lows(
                swing_points
            )

        }



        AgentLogger.info(

            f"Liquidity detected: {liquidity}"

        )


        return liquidity