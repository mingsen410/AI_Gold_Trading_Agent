from core.logger import AgentLogger


class SwingDetector:


    def __init__(
        self,
        lookback=1
    ):

        self.lookback = lookback



    def detect(
        self,
        candles
    ):


        swing_points=[]


        for i in range(
            1,
            len(candles)-1
        ):


            prev = candles[i-1]

            curr = candles[i]

            nxt = candles[i+1]



            # Swing High

            if (
                curr["high"] > prev["high"]
                and
                curr["high"] > nxt["high"]
            ):


                swing_points.append({

                    "type":"HIGH",

                    "price":curr["high"],

                    "index":i

                })



            # Swing Low

            if (
                curr["low"] < prev["low"]
                and
                curr["low"] < nxt["low"]
            ):


                swing_points.append({

                    "type":"LOW",

                    "price":curr["low"],

                    "index":i

                })



        AgentLogger.info(
            f"Detected {len(swing_points)} swing points"
        )


        return swing_points