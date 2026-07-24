from core.logger import AgentLogger

from market_context.context_builder import MarketContextBuilder

from ict_engine.entry_logic import ICTEntryLogic

from ai_brain.decision_engine import DecisionEngine

from risk_engine.risk_manager import RiskManager

from paper_trading.paper_account import PaperAccount

from paper_trading.trade_journal import TradeJournal




class TradingController:



    def __init__(self):


        self.context_builder = (

            MarketContextBuilder()

        )


        self.ict_engine = (

            ICTEntryLogic()

        )


        self.ai_engine = (

            DecisionEngine()

        )


        self.risk_engine = (

            RiskManager()

        )


        self.account = (

            PaperAccount()

        )


        self.journal = (

            TradeJournal()

        )






    def process(
        self,
        candles
    ):


        print(
            "\n===== MARKET ANALYSIS ====="
        )



        #
        # 1. Market Context
        #

        context = (

            self.context_builder.build(

                candles

            )

        )



        print(context)






        #
        # 2. ICT Signal
        #

        ict_signal = (

            self.ict_engine.analyze(

                context

            )

        )



        print(

            "\n===== ICT SIGNAL ====="

        )


        print(

            ict_signal

        )







        #
        # 3. AI Decision
        #

        decision = (

            self.ai_engine.decide(

                ict_signal

            )

        )



        print(

            "\n===== AI DECISION ====="

        )


        print(

            decision

        )







        #
        # 4. Execute Trade
        #

        if (

            decision["decision"]

            ==

            "EXECUTE_BUY"

            and

            not self.account.has_open_position()

        ):



            order = {



                "symbol":

                "XAUUSD",



                "action":

                "BUY",



                "entry":

                candles[-1]["close"],



                "volume":

                1,



                "sl":

                candles[-1]["close"] - 10,



                "tp":

                candles[-1]["close"] + 40

            }





            position = (

                self.account.open_trade(

                    order

                )

            )





            print(

                "\n===== POSITION OPEN ====="

            )



            print(

                position.__dict__

            )






        else:


            print(

                "\nNO TRADE"

            )







        return {



            "context":

            context,



            "ict_signal":

            ict_signal,



            "decision":

            decision

        }