from core.logger import AgentLogger



class PositionManager:



    def __init__(self):

        self.positions = []



    def open_position(
        self,
        trade
    ):


        position = {


            "symbol":

            trade["symbol"],


            "direction":

            trade["direction"],


            "entry":

            trade["entry"],


            "stop_loss":

            trade["stop_loss"],


            "take_profit":

            trade["take_profit"],


            "status":

            "OPEN"

        }


        self.positions.append(
            position
        )


        AgentLogger.info(

            f"Position opened: {position}"

        )


        return position




    def update_price(
        self,
        current_price
    ):


        for position in self.positions:


            if position["status"] != "OPEN":

                continue



            if position["direction"]=="BUY":


                if current_price <= position["stop_loss"]:


                    position["status"]="STOPPED"


                elif current_price >= position["take_profit"]:


                    position["status"]="TAKE_PROFIT"




            else:


                if current_price >= position["stop_loss"]:


                    position["status"]="STOPPED"


                elif current_price <= position["take_profit"]:


                    position["status"]="TAKE_PROFIT"



        return self.positions




    def get_open_positions(self):


        return [

            p for p in self.positions

            if p["status"]=="OPEN"

        ]