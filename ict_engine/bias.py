from core.logger import AgentLogger


class BiasEngine:


    def __init__(self):

        self.current_bias = "NEUTRAL"



    def calculate(
        self,
        market_structure
    ):


        if market_structure is None:


            return {


                "bias": "NEUTRAL",

                "strength": 0,

                "reason": "No structure data"

            }



        trend = market_structure.get(
            "trend"
        )


        bos = market_structure.get(
            "BOS"
        )



        if trend == "BULLISH" and bos:


            self.current_bias = "BULLISH"


            result = {


                "bias":

                "BULLISH",


                "strength":

                80,


                "reason":

                "Bullish BOS confirmed"

            }




        elif trend == "BEARISH" and bos:



            self.current_bias = "BEARISH"


            result = {


                "bias":

                "BEARISH",


                "strength":

                80,


                "reason":

                "Bearish BOS confirmed"

            }




        else:


            self.current_bias = "NEUTRAL"


            result = {


                "bias":

                "NEUTRAL",


                "strength":

                30,


                "reason":

                "No clear market direction"

            }



        AgentLogger.info(

            f"HTF Bias: {result}"

        )



        return result