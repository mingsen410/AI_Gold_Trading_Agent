from core.logger import AgentLogger




class CHoCHDetector:



    def __init__(self):


        self.last_signal = None





    def detect(

        self,

        structure,

        candles

    ):


        """

        检测市场结构变化


        structure:

        当前市场方向


        candles:

        最近K线数据


        """



        if len(candles) < 3:


            return {


                "choch":

                False

            }





        previous = candles[-3]


        current = candles[-1]





        # Bullish CHoCH



        if structure == "BEARISH":



            if current["close"] > previous["high"]:



                self.last_signal = "BULLISH_CHOCH"



                AgentLogger.info(

                    "Bullish CHoCH detected"

                )



                return {


                    "choch":

                    True,


                    "direction":

                    "BULLISH"

                }






        # Bearish CHoCH



        elif structure == "BULLISH":



            if current["close"] < previous["low"]:



                self.last_signal = "BEARISH_CHOCH"



                AgentLogger.info(

                    "Bearish CHoCH detected"

                )



                return {


                    "choch":

                    True,


                    "direction":

                    "BEARISH"

                }






        return {


            "choch":

            False

        }