from core.logger import AgentLogger



class RiskManagementEngine:



    def __init__(
        self,
        risk_percent=1,
        daily_loss_limit=3,
        max_consecutive_losses=3
    ):


        self.risk_percent = risk_percent

        self.daily_loss_limit = daily_loss_limit

        self.max_consecutive_losses = max_consecutive_losses


        self.daily_loss = 0

        self.consecutive_losses = 0



    def calculate_risk_amount(
        self,
        balance
    ):


        return (

            balance

            *

            self.risk_percent

            /

            100

        )



    def calculate_position_size(
        self,
        balance,
        stop_loss_distance,
        value_per_point=1
    ):


        risk_amount = self.calculate_risk_amount(
            balance
        )


        lot_size = (

            risk_amount

            /

            (

            stop_loss_distance

            *

            value_per_point

            )

        )


        return round(
            lot_size,
            2
        )



    def can_trade(self):


        if self.daily_loss >= self.daily_loss_limit:


            AgentLogger.info(
                "Daily loss limit reached"
            )


            return False



        if self.consecutive_losses >= self.max_consecutive_losses:


            AgentLogger.info(
                "Maximum consecutive losses reached"
            )


            return False



        return True



    def update_result(
        self,
        result
    ):


        if result < 0:


            self.consecutive_losses += 1


            self.daily_loss += abs(result)



        else:


            self.consecutive_losses = 0



        AgentLogger.info(

            f"Risk updated: loss={self.daily_loss}"

        )