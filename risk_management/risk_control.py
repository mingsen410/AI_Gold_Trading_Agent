from core.logger import AgentLogger




class RiskControl:



    def __init__(

        self,

        daily_loss_limit=3,

        max_consecutive_losses=3,

        max_positions=1

    ):



        """

        daily_loss_limit:

        每日最大亏损百分比



        max_consecutive_losses:

        最大连续亏损次数



        max_positions:

        最大同时持仓

        """



        self.daily_loss_limit = daily_loss_limit


        self.max_consecutive_losses = max_consecutive_losses


        self.max_positions = max_positions




    def check_daily_loss(

        self,

        balance,

        daily_loss

    ):


        """

        检查当天亏损

        """



        loss_percent = (

            daily_loss

            /

            balance

            *

            100

        )



        if loss_percent >= self.daily_loss_limit:


            AgentLogger.warning(

                "Daily loss limit reached"

            )


            return False



        return True





    def check_consecutive_loss(

        self,

        loss_count

    ):



        if loss_count >= self.max_consecutive_losses:


            AgentLogger.warning(

                "Maximum consecutive losses reached"

            )


            return False



        return True





    def check_open_positions(

        self,

        current_positions

    ):



        if current_positions >= self.max_positions:


            AgentLogger.warning(

                "Maximum positions reached"

            )


            return False



        return True





    def check_spread(

        self,

        spread,

        max_spread=40

    ):



        """

        黄金默认最大点差

        40 points


        可调整

        """



        if spread > max_spread:



            AgentLogger.warning(

                "Spread too high"

            )


            return False



        return True





    def approve_trade(

        self,

        balance,

        daily_loss,

        loss_count,

        positions,

        spread

    ):



        checks = [


            self.check_daily_loss(

                balance,

                daily_loss

            ),



            self.check_consecutive_loss(

                loss_count

            ),



            self.check_open_positions(

                positions

            ),



            self.check_spread(

                spread

            )

        ]



        approved = all(
            checks
        )



        if approved:


            AgentLogger.info(

                "Risk check passed"

            )


        else:


            AgentLogger.warning(

                "Trade rejected by Risk System"

            )



        return approved