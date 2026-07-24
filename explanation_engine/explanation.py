from core.logger import AgentLogger



class TradeExplanationEngine:



    def __init__(self):

        pass



    def generate(
        self,
        decision_data
    ):


        factors = decision_data["factors"]


        reasons=[]



        if factors.get("bias",0) >=20:

            reasons.append(
                "Strong higher timeframe market bias"
            )



        if factors.get("structure",0) >=20:

            reasons.append(
                "Market structure confirmation detected"
            )



        if factors.get("liquidity",0) >=15:

            reasons.append(
                "Liquidity event confirmed"
            )



        if factors.get("setup",0) >=10:

            reasons.append(
                "ICT setup confirmation"
            )



        if factors.get("session",0) >=5:

            reasons.append(
                "Trading session condition favorable"
            )



        explanation={


            "symbol":
            decision_data.get(
                "symbol",
                "XAUUSD"
            ),


            "direction":
            decision_data["decision"],


            "confidence":
            decision_data["score"],


            "reasons":
            reasons

        }



        AgentLogger.info(

            f"Trade Explanation Generated: {explanation}"

        )


        return explanation