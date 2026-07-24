from core.logger import AgentLogger



class PositionManager:


    def __init__(
        self,
        break_even_rr=1.0,
        partial_close_rr=2.0,
        trailing_rr=3.0,
        trailing_distance=10,
        partial_close_percent=0.5
    ):


        self.break_even_rr = break_even_rr

        self.partial_close_rr = partial_close_rr

        self.trailing_rr = trailing_rr

        self.trailing_distance = trailing_distance

        self.partial_close_percent = partial_close_percent





    def calculate_profit_rr(
        self,
        entry,
        initial_stop_loss,
        current_price,
        direction
    ):


        """
        使用最初风险计算RR

        不受移动止损影响
        """



        risk = abs(

            entry -

            initial_stop_loss

        )



        if risk == 0:

            return 0





        if direction == "BUY":


            profit = (

                current_price -

                entry

            )


        else:


            profit = (

                entry -

                current_price

            )




        return round(

            profit / risk,

            2

        )







    def manage_position(
        self,
        position
    ):



        entry = position["entry"]


        current_sl = position["stop_loss"]


        initial_sl = position["initial_stop_loss"]


        price = position["current_price"]


        direction = position["direction"]


        volume = position["volume"]





        rr = self.calculate_profit_rr(

            entry,

            initial_sl,

            price,

            direction

        )






        result = {


            "RR":

            rr,


            "action":

            "HOLD",



            "new_sl":

            current_sl,



            "close_volume":

            0,



            "remaining_volume":

            volume,



            "state":

            "OPEN"

        }







        #
        # 1. Break Even
        #

        if rr >= self.break_even_rr:


            if not position.get(
                "breakeven_done",
                False
            ):



                result["action"] = (

                    "MOVE_SL_TO_ENTRY"

                )



                result["new_sl"] = entry



                result["state"] = (

                    "BREAKEVEN"

                )



                position["breakeven_done"] = True






        #
        # 2. Partial Close
        #

        if rr >= self.partial_close_rr:


            if not position.get(
                "partial_closed",
                False
            ):



                close_volume = round(

                    volume *

                    self.partial_close_percent,

                    2

                )



                remaining_volume = round(

                    volume -

                    close_volume,

                    2

                )



                result["action"] = (

                    "PARTIAL_CLOSE"

                )


                result["close_volume"] = (

                    close_volume

                )


                result["remaining_volume"] = (

                    remaining_volume

                )


                result["state"] = (

                    "PARTIAL_PROFIT"

                )



                position["partial_closed"] = True







        #
        # 3. Trailing Stop
        #

        if rr >= self.trailing_rr:



            if direction == "BUY":



                trailing_sl = (

                    price -

                    self.trailing_distance

                )



                if trailing_sl > result["new_sl"]:


                    result["new_sl"] = trailing_sl




            else:



                trailing_sl = (

                    price +

                    self.trailing_distance

                )



                if trailing_sl < result["new_sl"]:


                    result["new_sl"] = trailing_sl






            result["action"] = (

                "TRAILING_STOP"

            )


            result["state"] = (

                "RUNNER"

            )


            position["trailing_active"] = True






        AgentLogger.info(

            f"Position Management: {result}"

        )



        return result







    def update_position(
        self,
        position,
        result
    ):



        #
        # 更新止损
        #

        if result["new_sl"] != position["stop_loss"]:


            position["stop_loss"] = (

                result["new_sl"]

            )







        #
        # 更新仓位
        #

        if result["action"] == "PARTIAL_CLOSE":



            position["volume"] = (

                result["remaining_volume"]

            )







        #
        # 更新状态
        #

        if result["action"] == "MOVE_SL_TO_ENTRY":


            position["breakeven_done"] = True





        if result["action"] == "PARTIAL_CLOSE":


            position["partial_closed"] = True





        if result["action"] == "TRAILING_STOP":


            position["trailing_active"] = True





        return position