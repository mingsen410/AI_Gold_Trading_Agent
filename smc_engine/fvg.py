from core.logger import AgentLogger



class FVGDetector:


    def __init__(
        self,
        min_gap=0.1
    ):

        """
        minimum gap size

        黄金(XAUUSD)

        默认0.1美元

        """

        self.min_gap = min_gap



    def detect_bullish_fvg(
        self,
        candles
    ):


        bullish_fvg = []


        for i in range(
            1,
            len(candles)-1
        ):


            candle1 = candles[i-1]

            candle2 = candles[i]

            candle3 = candles[i+1]



            gap = (

                candle3["low"]

                -

                candle1["high"]

            )



            if gap >= self.min_gap:


                bullish_fvg.append({


                    "type":
                    "BULLISH_FVG",


                    "top":
                    candle3["low"],


                    "bottom":
                    candle1["high"],


                    "size":
                    gap,


                    "index":
                    i


                })



        AgentLogger.info(

            f"Bullish FVG detected: {len(bullish_fvg)}"

        )


        return bullish_fvg





    def detect_bearish_fvg(
        self,
        candles
    ):


        bearish_fvg = []



        for i in range(
            1,
            len(candles)-1
        ):


            candle1 = candles[i-1]

            candle2 = candles[i]

            candle3 = candles[i+1]



            gap = (

                candle1["low"]

                -

                candle3["high"]

            )



            if gap >= self.min_gap:



                bearish_fvg.append({


                    "type":
                    "BEARISH_FVG",


                    "top":
                    candle1["low"],


                    "bottom":
                    candle3["high"],


                    "size":
                    gap,


                    "index":
                    i


                })


        AgentLogger.info(

            f"Bearish FVG detected: {len(bearish_fvg)}"

        )


        return bearish_fvg





    def detect(
        self,
        candles
    ):


        result = {


            "bullish":

            self.detect_bullish_fvg(
                candles
            ),


            "bearish":

            self.detect_bearish_fvg(
                candles
            )

        }



        return result