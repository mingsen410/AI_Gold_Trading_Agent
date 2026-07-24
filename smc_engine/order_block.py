from core.logger import AgentLogger



class OrderBlockDetector:



    def __init__(
        self,
        displacement_threshold=2
    ):

        """

        displacement_threshold:

        后续K线实体大小倍数

        判断是否有机构推动

        """

        self.threshold = displacement_threshold




    def is_bullish_candle(
        self,
        candle
    ):


        return (

            candle["close"]

            >

            candle["open"]

        )




    def is_bearish_candle(
        self,
        candle
    ):


        return (

            candle["close"]

            <

            candle["open"]

        )





    def candle_body(
        self,
        candle
    ):


        return abs(

            candle["close"]

            -

            candle["open"]

        )





    def detect_bullish_ob(
        self,
        candles
    ):


        bullish_obs = []



        for i in range(
            len(candles)-3
        ):


            candle = candles[i]


            next_candle = candles[i+1]



            if self.is_bearish_candle(
                candle
            ):



                current_body = self.candle_body(
                    candle
                )



                next_body = self.candle_body(
                    next_candle
                )



                if next_body >= current_body * self.threshold:



                    bullish_obs.append({


                        "type":
                        "BULLISH_OB",


                        "high":
                        candle["high"],


                        "low":
                        candle["low"],


                        "index":
                        i


                    })



        AgentLogger.info(

            f"Bullish OB detected: {len(bullish_obs)}"

        )


        return bullish_obs






    def detect_bearish_ob(
        self,
        candles
    ):


        bearish_obs = []



        for i in range(
            len(candles)-3
        ):



            candle = candles[i]


            next_candle = candles[i+1]



            if self.is_bullish_candle(
                candle
            ):



                current_body = self.candle_body(
                    candle
                )



                next_body = self.candle_body(
                    next_candle
                )



                if next_body >= current_body * self.threshold:



                    bearish_obs.append({


                        "type":
                        "BEARISH_OB",


                        "high":
                        candle["high"],


                        "low":
                        candle["low"],


                        "index":
                        i


                    })



        AgentLogger.info(

            f"Bearish OB detected: {len(bearish_obs)}"

        )


        return bearish_obs





    def detect(
        self,
        candles
    ):


        return {


            "bullish":

            self.detect_bullish_ob(
                candles
            ),



            "bearish":

            self.detect_bearish_ob(
                candles
            )

        }