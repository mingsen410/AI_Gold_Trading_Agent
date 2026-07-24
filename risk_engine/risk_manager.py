from core.logger import AgentLogger



class RiskManager:


    def __init__(
        self,
        default_risk_percent=1,
        sl_atr_multiplier=1.5,
        tp_atr_multiplier=3,
        minimum_rr=2
    ):


        self.default_risk_percent = default_risk_percent

        self.sl_atr_multiplier = sl_atr_multiplier

        self.tp_atr_multiplier = tp_atr_multiplier

        self.minimum_rr = minimum_rr





    def generate_trade_plan(
        self,
        balance,
        entry,
        direction,
        atr,
        risk_percent=None
    ):


        if risk_percent is None:

            risk_percent = self.default_risk_percent



        #
        # Dynamic SL / TP
        #

        if direction == "BUY":


            stop_loss = (

                entry

                -

                atr * self.sl_atr_multiplier

            )


            take_profit = (

                entry

                +

                atr * self.tp_atr_multiplier

            )



        elif direction == "SELL":


            stop_loss = (

                entry

                +

                atr * self.sl_atr_multiplier

            )


            take_profit = (

                entry

                -

                atr * self.tp_atr_multiplier

            )


        else:


            return {

                "error":
                "Invalid direction"

            }




        #
        # Risk Money
        #

        risk_amount = (

            balance

            *

            risk_percent

            /

            100

        )




        #
        # Distance
        #

        stop_distance = abs(

            entry - stop_loss

        )


        reward_distance = abs(

            take_profit - entry

        )



        if stop_distance == 0:


            return {

                "error":
                "Invalid SL"

            }




        #
        # RR
        #

        rr = round(

            reward_distance

            /

            stop_distance,

            2

        )




        #
        # RR Filter
        #

        if rr < self.minimum_rr:


            return {


                "status":

                "REJECTED",


                "reason":

                "Risk Reward below minimum",


                "rr":

                rr

            }




        #
        # XAUUSD Lot Size
        #

        contract_value = 100



        lot_size = round(

            risk_amount

            /

            (

                stop_distance

                *

                contract_value

            ),

            2

        )





        result = {


            "status":

            "APPROVED",


            "direction":

            direction,


            "entry":

            entry,


            "stop_loss":

            round(
                stop_loss,
                2
            ),


            "take_profit":

            round(
                take_profit,
                2
            ),


            "risk_amount":

            round(
                risk_amount,
                2
            ),


            "lot_size":

            lot_size,


            "risk_reward":

            rr

        }




        AgentLogger.info(

            f"Trade Plan Generated: {result}"

        )



        return result