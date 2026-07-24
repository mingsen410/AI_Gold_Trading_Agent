from core.logger import AgentLogger


class ConfidenceEngine:


    def __init__(self):

        self.confidence = 0



    def calculate(
        self,
        setup
    ):


        score = 50



        if setup.get("setup_score",0) >= 80:

            score += 20



        if setup.get("session") in [
            "LONDON",
            "NEW_YORK"
        ]:

            score += 10



        if setup.get("liquidity") == "SSL_SWEEP":

            score += 10



        if setup.get("volatility") == "NORMAL":

            score += 10



        self.confidence = min(
            score,
            100
        )


        AgentLogger.info(

            f"AI Confidence: {self.confidence}%"

        )


        return {


            "confidence":
            self.confidence,


            "trade_allowed":

            self.confidence >= 80

        }