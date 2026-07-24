from datetime import datetime



class SystemState:


    def __init__(self):


        self.running = False


        self.start_time = None


        self.current_symbol = "XAUUSD"


        self.current_bias = None


        self.open_positions = 0


        self.daily_profit = 0


        self.daily_loss = 0



    def start(self):


        self.running = True


        self.start_time = datetime.now()



    def stop(self):


        self.running = False



    def get_status(self):


        return {


            "running":
            self.running,


            "symbol":
            self.current_symbol,


            "bias":
            self.current_bias,


            "positions":
            self.open_positions,


            "profit":
            self.daily_profit,


            "loss":
            self.daily_loss


        }