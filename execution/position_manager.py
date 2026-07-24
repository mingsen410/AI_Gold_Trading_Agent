from core.logger import AgentLogger



class PositionManager:


    def __init__(

        self,

        break_even_rr=1.0,

        partial_close_rr=2.0,

        trailing_rr=3.0,

        trailing_distance=10

    ):


        """

        Position Management Logic


        break_even_rr:

        达到多少R移动保本


        partial_close_rr:

        达到多少R部分止盈


        trailing_rr:

        达到多少R启动移动止损


        trailing_distance:

        移动止损距离

        """


        self.break_even_rr = break_even_rr

        self.partial_close_rr = partial_close_rr

        self.trailing_rr = trailing_rr

        self.trailing_distance = trailing_distance






    def calculate_profit_rr(

        self,

        entry,

        initial_stop_loss,

        current_price,

        direction

    ):



        risk = abs(

            entry - initial_stop_loss

        )



        if risk == 0:

            return 0





        if direction == "BUY":


            profit = (

                current_price - entry

            )



        else:


            profit = (

                entry - current_price

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


        initial_sl = position.get(

            "initial_stop_loss",

            current_sl

        )


        current_price = position["current_price"]


        direction = position["direction"]



        partial_closed = position.get(

            "partial_closed",

            False

        )



        breakeven_done = position.get(

            "breakeven_done",

            False

        )



        trailing_active = position.get(

            "trailing_active",

            False

        )





        rr = self.calculate_profit_rr(

            entry,

            initial_sl,

            current_price,

            direction

        )






        action = {


            "RR":

            rr,


            "action":

            "HOLD",


            "new_sl":

            current_sl


        }






        #
        # 1. Break Even
        #

        if (

            rr >= self.break_even_rr

            and not breakeven_done

        ):



            action["action"] = (

                "MOVE_SL_TO_ENTRY"

            )


            action["new_sl"] = entry





        #
        # 2. Partial Close
        #

        elif (

            rr >= self.partial_close_rr

            and not partial_closed

        ):



            action["action"] = (

                "PARTIAL_CLOSE"

            )


            action["new_sl"] = current_sl






        #
        # 3. Trailing Stop
        #

        elif (

            rr >= self.trailing_rr

            and partial_closed

        ):



            action["action"] = (

                "TRAILING_STOP"

            )



            if direction == "BUY":


                new_sl = (

                    current_price

                    -

                    self.trailing_distance

                )


            else:


                new_sl = (

                    current_price

                    +

                    self.trailing_distance

                )



            action["new_sl"] = new_sl




            trailing_active = True





        AgentLogger.info(

            f"Position Management: {action}"

        )



        return action