from core.logger import AgentLogger



class PerformanceAnalyzer:



    def __init__(
        self,
        starting_balance=10000
    ):


        self.starting_balance = starting_balance



    def analyze(
        self,
        trades
    ):


        total_trades=len(trades)



        wins=[]

        losses=[]



        balance=self.starting_balance


        peak=balance


        max_drawdown=0



        for trade in trades:



            profit=trade["profit"]



            balance += profit



            if profit >0:


                wins.append(
                    profit
                )

            else:


                losses.append(
                    profit
                )



            if balance > peak:


                peak=balance



            drawdown=(

                peak-balance

            )/peak*100



            if drawdown > max_drawdown:


                max_drawdown=drawdown





        win_rate=(

            len(wins)

            /

            total_trades

            *

            100

        ) if total_trades else 0




        gross_profit=sum(
            wins
        )



        gross_loss=abs(
            sum(losses)
        )



        profit_factor=(

            gross_profit

            /

            gross_loss

        ) if gross_loss else 0




        net_profit=(

            balance

            -

            self.starting_balance

        )



        result={


            "total_trades":

            total_trades,


            "win_rate":

            round(win_rate,2),


            "net_profit":

            round(net_profit,2),


            "profit_factor":

            round(profit_factor,2),


            "max_drawdown":

            round(max_drawdown,2),


            "ending_balance":

            round(balance,2)

        }



        AgentLogger.info(

            f"Performance Report: {result}"

        )



        return result