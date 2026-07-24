from core.logger import AgentLogger



class PositionSizer:



    def __init__(
        self,
        risk_percent=1.0
    ):


        """

        单笔风险百分比

        默认:

        1%

        """

        self.risk_percent = risk_percent





    def calculate_lot_size(
        self,
        balance,
        entry,
        stop_loss,
        contract_value=100
    ):


        """

        XAUUSD计算


        balance:

        账户余额


        entry:

        入场价


        stop_loss:

        止损价


        contract_value:

        黄金合约参数


        """



        risk_money = (

            balance

            *

            self.risk_percent

            /

            100

        )



        stop_distance = abs(

            entry

            -

            stop_loss

        )



        if stop_distance == 0:


            return 0




        lot_size = (

            risk_money

            /

            (

                stop_distance

                *

                contract_value

            )

        )



        lot_size = round(

            lot_size,

            2

        )



        AgentLogger.info(

            f"Calculated lot size: {lot_size}"

        )



        return lot_size