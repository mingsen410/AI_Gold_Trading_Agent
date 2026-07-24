from core.logger import AgentLogger


from execution.market_orders import MarketOrderEngine


from execution.position_manager import PositionManager


from risk_management.position_sizing import PositionSizer


from risk_management.risk_control import RiskControl




class TradeExecutor:



    def __init__(self):


        self.order_engine = MarketOrderEngine()


        self.position_manager = PositionManager()


        self.position_sizer = PositionSizer(
            risk_percent=1
        )


        self.risk_control = RiskControl()



    def execute_trade(

        self,

        signal,

        account_data

    ):



        """

        signal:

        来自ICT Engine


        account_data:

        账户信息

        """



        # =====================

        # 1. Risk Check

        # =====================



        allowed = self.risk_control.approve_trade(

            balance=account_data["balance"],


            daily_loss=account_data["daily_loss"],


            loss_count=account_data["loss_count"],


            positions=account_data["positions"],


            spread=account_data["spread"]

        )



        if not allowed:


            return {


                "status":

                "REJECTED",


                "reason":

                "Risk Control"

            }




        # =====================

        # 2. Calculate Lot

        # =====================



        lot = self.position_sizer.calculate_lot_size(

            balance=account_data["balance"],


            entry=signal["entry"],


            stop_loss=signal["stop_loss"]

        )





        # =====================

        # 3. Create Order

        # =====================



        order = self.order_engine.create_order_request(

            symbol="XAUUSD",


            direction=signal["direction"],


            volume=lot,


            entry=signal["entry"],


            stop_loss=signal["stop_loss"],


            take_profit=signal["take_profit"]

        )





        # =====================

        # 4. Execute

        # =====================



        result = self.order_engine.execute_order(

            order

        )





        return result