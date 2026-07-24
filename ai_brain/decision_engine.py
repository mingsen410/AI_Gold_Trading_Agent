from core.logger import AgentLogger



class DecisionEngine:



    def __init__(
        self,
        minimum_confidence=0.6
    ):

        self.minimum_confidence = minimum_confidence




    def decide(
        self,
        ict_signal,
        strategy_signal=None
    ):


        decision = "WAIT"

        reasons = []



        confidence = ict_signal.get(
            "confidence",
            0
        )


        signal = ict_signal.get(
            "signal",
            "WAIT"
        )


        score = ict_signal.get(
            "score",
            0
        )



        # =================================
        # CONFIDENCE FILTER
        # =================================


        if confidence < self.minimum_confidence:


            reasons.append(
                "Confidence too low"
            )


            result = {

                "decision":
                decision,


                "confidence":
                confidence,


                "setup_score":
                score,


                "reason":
                reasons

            }


            AgentLogger.info(

                f"AI Decision: {result}"

            )


            return result




        # =================================
        # ICT SIGNAL DECISION
        # =================================


        if signal == "BUY":


            decision = "EXECUTE_BUY"


            reasons.extend(

                ict_signal.get(
                    "reason",
                    []
                )

            )




        elif signal == "SELL":


            decision = "EXECUTE_SELL"


            reasons.extend(

                ict_signal.get(
                    "reason",
                    []
                )

            )




        else:


            decision = "WAIT"


            reasons.extend(

                ict_signal.get(
                    "reason",
                    []
                )

            )


            reasons.append(
                "No trading signal"
            )





        result = {


            "decision":
            decision,


            "confidence":
            confidence,


            "setup_score":
            score,


            "reason":
            reasons

        }



        AgentLogger.info(

            f"AI Decision: {result}"

        )



        return result