import logging


logger=logging.getLogger(__name__)



class ICTEntryLogic:


    def generate_signal(
            self,
            context
    ):


        candles=context["candles"]


        if len(candles)<20:

            return {

                "signal":"WAIT",

                "score":0,

                "confidence":0,

                "reason":[]

            }




        score=0

        reason=[]




        closes=[

            c["close"]

            for c in candles

        ]



        current=closes[-1]


        previous=sum(
            closes[-10:-1]
        )/9




        # ===================
        # Trend
        # ===================


        if current > previous:


            score+=1

            reason.append(
                "Bullish momentum"
            )



        # ===================
        # Break structure
        # ===================


        if current > max(
            closes[-10:-1]
        ):


            score+=1


            reason.append(
                "Break of Structure"
            )




        # ===================
        # Liquidity sweep
        # ===================


        if candles[-1]["low"] < min(
            c["low"]
            for c in candles[-10:-1]
        ):


            score+=1


            reason.append(
                "Liquidity sweep"
            )




        # ===================
        # FVG simulation
        # ===================


        if candles[-1]["low"] > candles[-3]["high"]:


            score+=1


            reason.append(
                "FVG"
            )





        if score>=3:


            signal="BUY"


        else:


            signal="WAIT"




        return {


            "signal":
                signal,


            "score":
                score,


            "confidence":
                round(
                    score/4,
                    2
                ),


            "reason":
                reason


        }