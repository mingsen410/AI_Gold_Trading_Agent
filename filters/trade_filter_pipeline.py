from core.logger import AgentLogger


class TradeFilterPipeline:


    def __init__(self):

        self.filters = []



    def add_filter(
        self,
        filter_function
    ):

        self.filters.append(
            filter_function
        )



    def run(
        self,
        trade_setup
    ):


        for filter_function in self.filters:


            result = filter_function(
                trade_setup
            )


            if result["allowed"] == False:


                AgentLogger.info(

                    f"Trade rejected: {result['reason']}"

                )


                return {


                    "approved": False,


                    "reason": result["reason"]

                }



        AgentLogger.info(
            "All filters passed"
        )


        return {


            "approved": True,


            "reason": "All conditions passed"

        }