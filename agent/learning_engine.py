from core.logger import AgentLogger




class LearningEngine:



    def __init__(self):


        self.trade_history = []




    def record_trade(

        self,

        trade

    ):



        """

        保存交易结果

        """



        self.trade_history.append(

            trade

        )



        AgentLogger.info(

            "Trade recorded"

        )





    def calculate_statistics(self):



        total = len(

            self.trade_history

        )



        if total == 0:


            return {


                "trades":

                0

            }





        wins = 0


        losses = 0



        total_profit = 0





        for trade in self.trade_history:



            if trade["result"] == "WIN":


                wins += 1



            else:


                losses += 1



            total_profit += trade["profit"]





        win_rate = (

            wins / total

        ) * 100





        return {



            "total_trades":

            total,


            "wins":

            wins,


            "losses":

            losses,


            "win_rate":

            round(

                win_rate,

                2

            ),


            "profit":

            total_profit

        }





    def evaluate_setup(

        self,

        setup_name

    ):



        trades = [


            t for t in self.trade_history


            if t["setup"] == setup_name

        ]



        if len(trades) == 0:


            return None





        wins = len(

            [

            t for t in trades

            if t["result"]=="WIN"

            ]

        )



        return {



            "setup":

            setup_name,


            "sample":

            len(trades),


            "win_rate":

            round(

                wins /

                len(trades)

                *

                100,

                2

            )

        }