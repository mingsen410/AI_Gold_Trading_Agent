from core.logger import AgentLogger


class LiquidityEngine:


    def __init__(self):

        self.equal_threshold = 3



    # =====================================
    # Equal High Liquidity
    # =====================================

    def detect_equal_highs(
        self,
        swing_points
    ):


        highs = [

            x for x in swing_points

            if isinstance(x,dict)
            and x.get("type")=="HIGH"

        ]


        liquidity=[]



        for i in range(len(highs)-1):


            current=highs[i]

            nxt=highs[i+1]



            if abs(
                current["price"]
                -
                nxt["price"]
            ) <= self.equal_threshold:


                liquidity.append({

                    "type":
                    "BUY_SIDE_LIQUIDITY",


                    "price":
                    max(
                        current["price"],
                        nxt["price"]
                    )

                })


        return liquidity





    # =====================================
    # Equal Low Liquidity
    # =====================================

    def detect_equal_lows(
        self,
        swing_points
    ):


        lows=[

            x for x in swing_points

            if isinstance(x,dict)
            and x.get("type")=="LOW"

        ]


        liquidity=[]



        for i in range(len(lows)-1):


            current=lows[i]

            nxt=lows[i+1]



            if abs(
                current["price"]
                -
                nxt["price"]
            ) <= self.equal_threshold:


                liquidity.append({

                    "type":
                    "SELL_SIDE_LIQUIDITY",


                    "price":
                    min(
                        current["price"],
                        nxt["price"]
                    )

                })


        return liquidity





    # =====================================
    # Add Swing Liquidity
    # =====================================

    def add_swing_liquidity(
        self,
        swing_points,
        buy_side,
        sell_side
    ):


        highs=[

            x for x in swing_points

            if x.get("type")=="HIGH"

        ]


        lows=[

            x for x in swing_points

            if x.get("type")=="LOW"

        ]



        # latest swing high

        if highs:


            latest_high=highs[-1]


            exists=any(

                abs(
                    x["price"]
                    -
                    latest_high["price"]
                ) <= self.equal_threshold

                for x in buy_side

            )


            if not exists:


                buy_side.append({

                    "type":
                    "SWING_HIGH_LIQUIDITY",


                    "price":
                    latest_high["price"]

                })





        # latest swing low

        if lows:


            latest_low=lows[-1]


            exists=any(

                abs(
                    x["price"]
                    -
                    latest_low["price"]
                ) <= self.equal_threshold

                for x in sell_side

            )



            if not exists:


                sell_side.append({

                    "type":
                    "SWING_LOW_LIQUIDITY",


                    "price":
                    latest_low["price"]

                })



        return buy_side,sell_side





    # =====================================
    # Liquidity Sweep
    # =====================================

    def detect_sweep(
        self,
        candles,
        buy_side,
        sell_side
    ):


        result={

            "sweep":
            False

        }



        if len(candles)<2:

            return result



        latest=candles[-1]




        # ===============================
        # Buy-side sweep
        # ===============================


        for liq in buy_side:


            if (

                latest["high"] >
                liq["price"]

                and

                latest["close"] <
                liq["price"]

            ):


                return {


                    "sweep":
                    True,


                    "direction":
                    "BEARISH",


                    "taken":
                    liq

                }




        # ===============================
        # Sell-side sweep
        # ===============================


        for liq in sell_side:


            if (

                latest["low"] <
                liq["price"]

                and

                latest["close"] >
                liq["price"]

            ):


                return {


                    "sweep":
                    True,


                    "direction":
                    "BULLISH",


                    "taken":
                    liq

                }




        return result





    # =====================================
    # Main Analysis
    # =====================================

    def analyze(
        self,
        swing_points,
        candles
    ):


        try:


            buy_side = self.detect_equal_highs(
                swing_points
            )


            sell_side = self.detect_equal_lows(
                swing_points
            )



            buy_side,sell_side = self.add_swing_liquidity(
                swing_points,
                buy_side,
                sell_side
            )



            sweep=self.detect_sweep(
                candles,
                buy_side,
                sell_side
            )



            result={


                "buy_side_liquidity":
                buy_side,


                "sell_side_liquidity":
                sell_side,


                "sweep":
                sweep

            }



            AgentLogger.info(
                f"Liquidity Analysis: {result}"
            )



            return result



        except Exception as e:


            AgentLogger.warning(
                f"Liquidity failed: {e}"
            )


            return {


                "buy_side_liquidity":
                [],


                "sell_side_liquidity":
                [],


                "sweep":
                {
                    "sweep":
                    False
                }

            }