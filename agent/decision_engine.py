from core.logger import AgentLogger




class DecisionEngine:



    def __init__(self):

        self.last_decision = None




    def evaluate(

        self,

        bias,

        setup,

        risk

    ):



        """

        综合决策层



        bias:

        HTF方向



        setup:

        ICT模型结果



        risk:

        风险状态

        """





        if not risk:


            AgentLogger.warning(

                "Risk rejected decision"

            )


            return "NO TRADE"





        if setup["signal"] == "BUY":



            self.last_decision = "BUY"


            return "BUY"





        elif setup["signal"] == "SELL":



            self.last_decision = "SELL"


            return "SELL"





        else:



            self.last_decision = "NO TRADE"


            return "NO TRADE"