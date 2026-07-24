from core.logger import AgentLogger

from execution.position_manager import PositionManager



class TradeMonitor:


    def __init__(self):


        self.position_manager = PositionManager(
            break_even_rr=1.0,
            partial_close_rr=2.0,
            trailing_distance=10
        )



    def update_position(
        self,
        position,
        current_price
    ):


        position["current_price"] = current_price



        result = self.position_manager.manage_position(
            position
        )



        AgentLogger.info(
            f"Trade Update: {result}"
        )



        #
        # Apply Action
        #

        if result["action"] == "MOVE_SL_TO_ENTRY":


            position["stop_loss"] = (
                position["entry"]
            )



        elif result["action"] == "PARTIAL_CLOSE":


            position["volume"] = (
                position["volume"] / 2
            )



        return result