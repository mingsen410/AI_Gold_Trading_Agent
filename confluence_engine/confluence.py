from core.logger import AgentLogger



class ICTConfluenceEngine:



    def __init__(self):


        self.weights = {


            "bias":25,

            "liquidity":20,

            "structure":20,

            "order_block":15,

            "fvg":10,

            "session":5,

            "risk":5

        }




    def calculate_score(
        self,
        signals
    ):


        score=0



        for key,value in signals.items():


            score += value



        return score




    def classify_setup(
        self,
        score
    ):


        if score >=90:


            return "A+"



        elif score >=80:


            return "A"



        elif score >=70:


            return "B"



        else:


            return "REJECT"




    def evaluate(
        self,
        signals
    ):


        score=self.calculate_score(
            signals
        )


        setup=self.classify_setup(
            score
        )



        decision = (
            "ALLOW TRADE"

            if setup!="REJECT"

            else

            "NO TRADE"

        )



        result={


            "score":

            score,


            "setup":

            setup,


            "decision":

            decision,


            "signals":

            signals

        }



        AgentLogger.info(

            f"ICT Confluence Result: {result}"

        )


        return result