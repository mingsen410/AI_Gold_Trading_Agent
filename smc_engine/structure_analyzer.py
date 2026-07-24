from core.logger import AgentLogger




class StructureAnalyzer:



    def __init__(self):


        self.last_structure = None






    def analyze(

        self,

        swings

    ):



        """

        根据Swing High / Low判断结构



        swings格式:

        [

        {

        type:"HIGH",

        price:3400

        },


        {

        type:"LOW",

        price:3350

        }

        ]

        """





        if len(swings)<4:


            return {


                "structure":

                "UNKNOWN"

            }





        last = swings[-4:]





        high1 = last[0]["price"]


        low1 = last[1]["price"]


        high2 = last[2]["price"]


        low2 = last[3]["price"]





        # Bullish Structure


        if high2 > high1 and low2 > low1:



            self.last_structure = "BULLISH"



            return {



                "structure":

                "BULLISH",


                "event":

                "BOS_UP"


            }





        # Bearish Structure


        elif high2 < high1 and low2 < low1:



            self.last_structure = "BEARISH"



            return {



                "structure":

                "BEARISH",


                "event":

                "BOS_DOWN"


            }






        return {



            "structure":

            "RANGE",


            "event":

            "NO_BREAK"

        }