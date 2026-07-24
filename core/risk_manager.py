import logging


logger = logging.getLogger(__name__)


class RiskManager:

    def __init__(
        self,
        risk_reward=3,
        sl_distance=10
    ):

        self.risk_reward = risk_reward
        self.sl_distance = sl_distance


    def calculate_levels(
        self,
        entry,
        direction
    ):

        if direction == "BUY":

            sl = entry - self.sl_distance

            tp = entry + (
                self.sl_distance *
                self.risk_reward
            )


        elif direction == "SELL":

            sl = entry + self.sl_distance

            tp = entry - (
                self.sl_distance *
                self.risk_reward
            )


        else:

            return None,None


        return sl,tp