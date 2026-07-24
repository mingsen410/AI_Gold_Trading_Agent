from core.logger import AgentLogger



class TradeExecutionEngine:



    def __init__(

        self,

        risk_engine,

        position_manager

    ):


        self.risk_engine = risk_engine

        self.position_manager = position_manager



    def execute(

        self,

        signal,

        account_balance

    ):



        if not self.risk_engine.can_trade():


            AgentLogger.info(

                "Trade blocked by risk manager"

            )


            return None



        lot = self.risk_engine.calculate_position_size(

            account_balance,

            signal["stop_loss_distance"]

        )



        trade = {


            "symbol":

            signal["symbol"],


            "direction":

            signal["direction"],


            "entry":

            signal["entry"],


            "stop_loss":

            signal["stop_loss"],


            "take_profit":

            signal["take_profit"],


            "lot":

            lot

        }



        self.position_manager.open_position(
            trade
        )



        AgentLogger.info(

            f"Trade executed: {trade}"

        )


        return trade