def build_context(candles, index):

    context = {

        "structure": {},

        "liquidity": {},

        "fvg": [],

        "order_block": []

    }


    if index < 20:
        return context



    current = candles[index]

    previous = candles[index-1]



    # ==========================
    # Market Structure
    # ==========================

    if current["close"] > previous["high"]:

        context["structure"] = {

            "trend":"BULLISH",

            "BOS":True

        }

    else:

        context["structure"] = {

            "trend":"BEARISH",

            "BOS":False

        }



    # ==========================
    # Liquidity Sweep
    # ==========================


    recent_low = min(
        c["low"]
        for c in candles[index-10:index]
    )


    if current["low"] < recent_low:

        context["liquidity"]={

            "sweep":{

                "sweep":True

            }

        }



    # ==========================
    # Fair Value Gap
    # ==========================


    candle1 = candles[index-2]

    candle3 = candles[index]


    if candle1["high"] < candle3["low"]:

        context["fvg"].append({

            "type":"bullish"

        })



    # ==========================
    # Order Block
    # ==========================


    if (
        current["close"] >
        current["open"]
    ):

        context["order_block"].append({

            "type":"bullish"

        })



    return context