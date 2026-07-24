from core.logger import AgentLogger



class TradeManager:


    def __init__(
        self,
        position_manager
    ):

        self.position_manager = position_manager





    def update_position(
        self,
        position,
        current_price
    ):


        position.current_price = current_price




        result = self.position_manager.manage_position(

            {

                "entry":
                position.entry,


                "stop_loss":
                position.sl,


                "initial_stop_loss":
                position.initial_stop_loss,


                "current_price":
                current_price,


                "direction":
                position.direction,


                "volume":
                position.volume,


                "take_profit":
                position.tp,


                "partial_closed":
                position.partial_closed,


                "breakeven_done":
                position.breakeven_done,


                "trailing_active":
                position.trailing_active

            }

        )




        #
        # Compatibility
        # 如果旧 PositionManager 没返回 state
        #

        state = result.get(

            "state",

            "OPEN"

        )




        #
        # Update Stop Loss
        #

        if "new_sl" in result:


            position.sl = result["new_sl"]





        #
        # Update flags
        #

        if result["action"] == "MOVE_SL_TO_ENTRY":


            position.breakeven_done = True

            position.state = "BREAKEVEN"




        elif result["action"] == "PARTIAL_CLOSE":


            position.partial_closed = True

            position.state = "PARTIAL_PROFIT"




        elif result["action"] == "TRAILING_STOP":


            position.trailing_active = True

            position.state = "RUNNER"




        else:


            position.state = state






        #
        # Partial close
        #

        if result["action"] == "PARTIAL_CLOSE":



            close_volume = (

                position.volume * 0.5

            )



            position.volume -= close_volume



            if position.volume < 0:


                position.volume = 0



            result["close_volume"] = close_volume


            result["remaining_volume"] = position.volume





        else:


            result["close_volume"] = 0

            result["remaining_volume"] = position.volume





        #
        # Logging
        #

        AgentLogger.info(

            f"Trade Update: {result}"

        )



        return result