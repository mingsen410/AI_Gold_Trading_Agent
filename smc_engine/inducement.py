from core.logger import AgentLogger



class InducementDetector:



    def __init__(
        self,
        sensitivity=0.002
    ):


        """
        判断内部结构距离

        """

        self.sensitivity = sensitivity




    def detect_bullish_inducement(
        self,
        swing_points
    ):


        inducements = []



        lows = [

            x for x in swing_points

            if x["type"]=="LOW"

        ]



        for i in range(
            len(lows)-1
        ):



            main_low = lows[i]

            next_low = lows[i+1]



            difference = abs(

                main_low["price"]

                -

                next_low["price"]

            )



            average = (

                main_low["price"]

                +

                next_low["price"]

            ) / 2




            if average == 0:

                continue



            distance = difference / average




            if (

                distance <= self.sensitivity

            ):


                inducements.append({


                    "type":
                    "BULLISH_IDM",


                    "price":
                    next_low["price"],


                    "reference":
                    main_low


                })



        AgentLogger.info(

            f"Bullish IDM detected: {len(inducements)}"

        )


        return inducements





    def detect_bearish_inducement(
        self,
        swing_points
    ):


        inducements = []



        highs = [

            x for x in swing_points

            if x["type"]=="HIGH"

        ]



        for i in range(
            len(highs)-1
        ):



            main_high = highs[i]

            next_high = highs[i+1]



            difference = abs(

                main_high["price"]

                -

                next_high["price"]

            )



            average = (

                main_high["price"]

                +

                next_high["price"]

            ) / 2



            if average == 0:

                continue



            distance = difference / average




            if (

                distance <= self.sensitivity

            ):


                inducements.append({


                    "type":
                    "BEARISH_IDM",


                    "price":
                    next_high["price"],


                    "reference":
                    main_high


                })



        AgentLogger.info(

            f"Bearish IDM detected: {len(inducements)}"

        )


        return inducements





    def detect(
        self,
        swing_points
    ):


        return {


            "bullish":

            self.detect_bullish_inducement(
                swing_points
            ),



            "bearish":

            self.detect_bearish_inducement(
                swing_points
            )

        }