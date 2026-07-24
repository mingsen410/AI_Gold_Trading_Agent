from core.logger import AgentLogger



class CandleManager:



    def __init__(self):


        self.candles = {



            "M1":[],

            "M5":[],

            "M15":[],

            "H1":[],

            "H4":[]


        }





    def add_candle(

        self,

        timeframe,

        candle

    ):


        if timeframe not in self.candles:


            AgentLogger.warning(

                "Invalid timeframe"

            )


            return False




        self.candles[timeframe].append(

            candle

        )



        return True





    def get_candles(

        self,

        timeframe,

        limit=100

    ):



        data = self.candles.get(

            timeframe,

            []

        )



        return data[-limit:]





    def latest_candle(

        self,

        timeframe

    ):



        candles = self.get_candles(

            timeframe,

            1

        )



        if len(candles)==0:


            return None



        return candles[0]





    def calculate_range(

        self,

        timeframe

    ):



        candles = self.get_candles(

            timeframe

        )



        if not candles:


            return None




        highs = [

            c["high"]

            for c in candles

        ]



        lows = [

            c["low"]

            for c in candles

        ]



        return {


            "highest":

            max(highs),


            "lowest":

            min(lows)


        }