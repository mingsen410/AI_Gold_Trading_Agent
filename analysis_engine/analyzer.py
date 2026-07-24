from logger import log



class Analyzer:


    def analyze(self, market_data):


        price = market_data["price"]



        log(
            f"Analyzing XAUUSD price: {price}"
        )



        return {


            "trend":

            "UNKNOWN",


            "signal":

            "WAIT"


        }