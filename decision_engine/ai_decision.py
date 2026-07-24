from core.logger import AgentLogger



class AIDecisionEngine:



    def __init__(self):

        self.weights = {


            "bias":25,

            "structure":25,

            "liquidity":20,

            "setup":15,

            "session":10,

            "risk":5

        }



    def calculate_score(
        self,
        factors
    ):


        score = 0



        for key,value in factors.items():


            score += value



        return score



    def decide(
        self,
        factors
    ):


        score = self.calculate_score(
            factors
        )



        if score >= 80:


            decision="BUY"



        elif score <=40:


            decision="SELL"



        else:


            decision="NO TRADE"



        result={


            "score":

            score,


            "decision":

            decision,


            "factors":

            factors

        }



        AgentLogger.info(

            f"AI Decision: {result}"

        )


        return result