from core.logger import AgentLogger



class AdaptiveRiskEngine:



    def __init__(
        self,
        base_risk=1
    ):


        self.base_risk = base_risk




    def calculate(
        self,
        setup,
        regime,
        drawdown,
        news_status
    ):


        risk = self.base_risk



        # Setup Quality


        if setup == "A+":


            risk *= 1.2



        elif setup == "A":


            risk *= 1



        elif setup == "B":


            risk *= 0.5



        else:


            risk = 0




        # Market Regime


        if regime == "TRENDING":


            pass



        elif regime == "RANGING":


            risk *= 0.5



        else:


            risk = 0




        # Drawdown Protection


        if drawdown >=5:


            risk *=0.5



        if drawdown >=10:


            risk=0




        # News Filter


        if news_status=="BLOCK":


            risk=0




        result={


            "risk_percent":

            round(risk,2),


            "status":

            "ALLOW"

            if risk>0

            else

            "BLOCK"

        }



        AgentLogger.info(

            f"Adaptive Risk: {result}"

        )


        return result