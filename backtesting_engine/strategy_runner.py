from core.logger import AgentLogger



class BacktestStrategyRunner:



    def __init__(
        self,
        confluence_engine=None,
        risk_engine=None
    ):


        self.confluence_engine = confluence_engine

        self.risk_engine = risk_engine



    def analyze(
        self,
        market_state
    ):


        signals = market_state["signals"]



        result = self.confluence_engine.evaluate(
            signals
        )



        if result["decision"] != "ALLOW TRADE":


            AgentLogger.info(

                "Trade rejected by confluence"

            )


            return None




        risk = self.risk_engine.calculate(

            setup=result["setup"],

            regime=market_state["regime"],

            drawdown=market_state["drawdown"],

            news_status=market_state["news"]

        )



        if risk["status"]=="BLOCK":


            AgentLogger.info(

                "Trade rejected by risk"

            )


            return None




        trade_signal={


            "type":

            market_state["direction"],


            "entry":

            market_state["entry"],


            "stop_loss":

            market_state["stop_loss"],


            "take_profit":

            market_state["take_profit"],


            "risk":

            risk["risk_percent"]


        }



        AgentLogger.info(

            f"Trade signal generated: {trade_signal}"

        )


        return trade_signal