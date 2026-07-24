from core.logger import AgentLogger
from execution.position_manager import PositionManager



class TradeMonitor:


    def __init__(self):

        self.manager=PositionManager()



    def update(
        self,
        position,
        current_price
    ):


        position["current_price"]=current_price



        management=self.manager.manage_position(
            position
        )


        AgentLogger.info(
            f"Trade Update: {management}"
        )


        return management