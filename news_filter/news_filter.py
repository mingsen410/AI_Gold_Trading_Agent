from core.logger import AgentLogger



class NewsFilterEngine:



    def __init__(
        self,
        block_minutes=30
    ):


        self.block_minutes = block_minutes



    def check(
        self,
        event
    ):


        impact = event["impact"]

        minutes = event["minutes_to_event"]



        if impact == "HIGH":


            if minutes <= self.block_minutes:


                result={

                    "status":"BLOCK",

                    "reason":

                    "High impact news approaching"

                }


                AgentLogger.info(
                    result
                )


                return result



        if impact == "MEDIUM":


            if minutes <=15:


                result={


                    "status":"REDUCE_RISK",


                    "reason":

                    "Medium impact event approaching"

                }


                AgentLogger.info(
                    result
                )


                return result



        result={


            "status":"ALLOW",


            "reason":

            "No restricted event"

        }


        AgentLogger.info(
            result
        )


        return result