from core.logger import AgentLogger



class SignalGenerator:



    def __init__(self):


        self.name = "AI Signal Generator"




    def generate(
        self,
        ict_result,
        smc_result,
        risk_result
    ):


        score = 0



        # =====================
        # ICT Evaluation
        # =====================

        if ict_result == "BULLISH":

            score += 1


        elif ict_result == "BEARISH":

            score -= 1




        # =====================
        # SMC Evaluation
        # =====================

        if smc_result == "BULLISH":

            score += 1


        elif smc_result == "BEARISH":

            score -= 1




        # =====================
        # Risk Filter
        # =====================

        if risk_result == "PASS":

            score += 1


        else:

            score -= 2





        # =====================
        # Final Decision
        # =====================


        if score >= 2:


            signal = "BUY"



        elif score <= -2:


            signal = "SELL"



        else:


            signal = "HOLD"




        confidence = abs(score) / 3



        result = {


            "signal":
            signal,


            "score":
            score,


            "confidence":
            round(
                confidence,
                2
            )

        }



        AgentLogger.info(

            f"Generated Signal: {result}"

        )


        return result