from core.logger import AgentLogger



class MarketStructure:



    def analyze(
        self,
        swing_points
    ):


        if len(swing_points) < 2:


            return {


                "trend":"UNKNOWN",

                "BOS":False,

                "CHoCH":False,

                "reason":"Not enough structure"

            }



        highs=[]

        lows=[]



        for s in swing_points:


            if s["type"]=="HIGH":

                highs.append(
                    s["price"]
                )


            else:

                lows.append(
                    s["price"]
                )




        trend="UNKNOWN"

        bos=False




        # ==========================
        # Bullish Structure
        # ==========================

        if len(highs)>=1 and len(lows)>=1:


            if highs[-1] > highs[0]:

                trend="BULLISH"

                bos=True



        # ==========================
        # Bearish Structure
        # ==========================

            elif lows[-1] < lows[0]:

                trend="BEARISH"

                bos=True





        result={


            "trend":trend,


            "BOS":bos,


            "CHoCH":False,


            "reason":"Structure detected"

        }



        AgentLogger.info(

            f"Structure Result: {result}"

        )


        return result