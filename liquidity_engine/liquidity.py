from core.logger import AgentLogger



class LiquidityEngine:



    def __init__(
        self,
        tolerance=5
    ):

        self.tolerance = tolerance



    def detect_equal_highs(
        self,
        candles
    ):


        highs=[]



        for candle in candles:


            highs.append(
                candle["high"]
            )



        signals=[]



        for i in range(
            len(highs)-1
        ):


            if abs(
                highs[i]-highs[i+1]
            ) <= self.tolerance:


                signals.append(

                {

                "type":
                "EQUAL_HIGH",


                "level":
                highs[i]

                }

                )



        return signals




    def detect_equal_lows(
        self,
        candles
    ):


        lows=[]



        for candle in candles:


            lows.append(
                candle["low"]
            )



        signals=[]



        for i in range(
            len(lows)-1
        ):


            if abs(
                lows[i]-lows[i+1]
            ) <= self.tolerance:


                signals.append(

                {

                "type":
                "EQUAL_LOW",


                "level":
                lows[i]

                }

                )



        return signals




    def detect_sweep(
        self,
        candle,
        liquidity_level
    ):


        if candle["high"] > liquidity_level and candle["close"] < liquidity_level:


            result={


            "type":

            "BUY_SIDE_LIQUIDITY_SWEEP",


            "level":

            liquidity_level,


            "confidence":

            85


            }



            AgentLogger.info(result)


            return result



        if candle["low"] < liquidity_level and candle["close"] > liquidity_level:


            result={


            "type":

            "SELL_SIDE_LIQUIDITY_SWEEP",


            "level":

            liquidity_level,


            "confidence":

            85


            }



            AgentLogger.info(result)


            return result



        return None