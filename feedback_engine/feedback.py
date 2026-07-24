from core.logger import AgentLogger



class FeedbackEngine:



    def __init__(self):


        self.statistics = {}



    def record_trade(
        self,
        setup,
        result
    ):


        if setup not in self.statistics:


            self.statistics[setup]={


                "trades":0,

                "wins":0,

                "losses":0

            }



        self.statistics[setup]["trades"] += 1



        if result > 0:


            self.statistics[setup]["wins"] += 1


        else:


            self.statistics[setup]["losses"] += 1



    def calculate_win_rate(
        self,
        setup
    ):


        data=self.statistics.get(
            setup
        )


        if not data:


            return 0



        return round(

            data["wins"]

            /

            data["trades"]

            *

            100,

            2

        )



    def get_adjustment(
        self,
        setup
    ):


        win_rate=self.calculate_win_rate(
            setup
        )


        if win_rate >= 70:


            adjustment=10



        elif win_rate <50:


            adjustment=-10



        else:


            adjustment=0



        AgentLogger.info(

            f"{setup} adjustment {adjustment}%"

        )


        return adjustment