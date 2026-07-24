from core.logger import AgentLogger



class TradeSimulator:



    def __init__(
        self,
        balance=10000
    ):


        self.balance = balance

        self.trades=[]



    def open_trade(
        self,
        signal
    ):


        trade={


            "type":
            signal["type"],


            "entry":
            signal["entry"],


            "stop_loss":
            signal["stop_loss"],


            "take_profit":
            signal["take_profit"],


            "status":
            "OPEN"

        }


        self.current_trade=trade



        AgentLogger.info(

            f"Trade opened: {trade}"

        )



        return trade




    def check_exit(
        self,
        candle
    ):


        trade=self.current_trade



        if trade["type"]=="BUY":



            if candle["low"] <= trade["stop_loss"]:


                return self.close_trade(

                    trade["stop_loss"],

                    "LOSS"

                )



            if candle["high"] >= trade["take_profit"]:


                return self.close_trade(

                    trade["take_profit"],

                    "WIN"

                )





        if trade["type"]=="SELL":



            if candle["high"] >= trade["stop_loss"]:


                return self.close_trade(

                    trade["stop_loss"],

                    "LOSS"

                )



            if candle["low"] <= trade["take_profit"]:


                return self.close_trade(

                    trade["take_profit"],

                    "WIN"

                )



        return None




    def close_trade(
        self,
        price,
        result
    ):


        trade=self.current_trade


        trade["exit"]=price


        trade["result"]=result



        if trade["type"]=="BUY":


            profit = (

                price

                -

                trade["entry"]

            )

        else:


            profit = (

                trade["entry"]

                -

                price

            )



        trade["profit"]=profit


        trade["status"]="CLOSED"



        self.trades.append(
            trade
        )



        AgentLogger.info(

            f"Trade closed: {trade}"

        )


        self.current_trade=None



        return trade