from core.logger import AgentLogger




class PositionManager:



    def __init__(

        self,

        break_even_trigger=15,

        trailing_distance=10,

        partial_close_ratio=0.5

    ):


        self.break_even_trigger = break_even_trigger

        self.trailing_distance = trailing_distance

        self.partial_close_ratio = partial_close_ratio





    def manage(

        self,

        position,

        current_price

    ):


        action = []



        entry = position["entry"]

        sl = position["sl"]

        tp = position["tp"]

        direction = position["direction"]




        #
        # BUY POSITION
        #

        if direction == "BUY":


            profit = current_price - entry




            #
            # Break Even
            #

            if profit >= self.break_even_trigger:


                if sl < entry:


                    position["sl"] = entry


                    action.append(

                        "MOVE_SL_TO_BREAK_EVEN"

                    )





            #
            # Trailing Stop
            #

            new_sl = current_price - self.trailing_distance



            if new_sl > position["sl"]:


                position["sl"] = new_sl


                action.append(

                    "TRAILING_STOP_UPDATED"

                )





        #
        # SELL POSITION
        #

        elif direction == "SELL":


            profit = entry - current_price




            if profit >= self.break_even_trigger:


                if sl > entry:


                    position["sl"] = entry


                    action.append(

                        "MOVE_SL_TO_BREAK_EVEN"

                    )





            new_sl = current_price + self.trailing_distance



            if new_sl < position["sl"]:


                position["sl"] = new_sl


                action.append(

                    "TRAILING_STOP_UPDATED"

                )





        #
        # Partial Close
        #

        if profit > 0:


            action.append(

                f"PARTIAL_CLOSE_{self.partial_close_ratio*100}%"

            )





        result = {


            "position":

            position,


            "actions":

            action

        }



        AgentLogger.info(

            f"Position Management: {result}"

        )


        return result