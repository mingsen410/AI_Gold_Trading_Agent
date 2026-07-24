from core.logger import AgentLogger




class DrawdownMonitor:



    def __init__(

        self,

        warning_level=10,

        emergency_level=20

    ):



        """

        warning_level:

        回撤警告


        emergency_level:

        停止交易

        """



        self.warning_level = warning_level


        self.emergency_level = emergency_level



        self.highest_equity = 0




    def update_equity(

        self,

        equity

    ):



        if equity > self.highest_equity:


            self.highest_equity = equity




    def calculate_drawdown(

        self,

        equity

    ):



        if self.highest_equity == 0:


            return 0




        drawdown = (

            (

                self.highest_equity

                -

                equity

            )

            /

            self.highest_equity

        ) * 100




        return round(

            drawdown,

            2

        )





    def check_status(

        self,

        equity

    ):



        self.update_equity(

            equity

        )



        dd = self.calculate_drawdown(

            equity

        )



        status = {



            "drawdown":

            dd,


            "allow_trade":

            True,


            "level":

            "NORMAL"


        }




        if dd >= self.emergency_level:



            status["allow_trade"] = False


            status["level"] = "EMERGENCY_STOP"



            AgentLogger.warning(

                "Emergency Drawdown Stop Activated"

            )





        elif dd >= self.warning_level:



            status["level"] = "WARNING"



            AgentLogger.warning(

                "Drawdown Warning"

            )




        return status