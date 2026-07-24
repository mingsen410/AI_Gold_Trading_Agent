import random


def generate_xauusd_data(
        candles=1000,
        start_price=3350
):

    random.seed(42)

    data = []

    price = start_price


    for i in range(candles):

        # 每100根制造一次趋势
        cycle = i % 100


        if cycle < 40:
            # bullish trend
            change = random.uniform(
                0.5,
                3
            )

        elif cycle < 60:
            # retracement
            change = random.uniform(
                -3,
                -0.5
            )

        elif cycle < 70:
            # liquidity sweep
            change = random.uniform(
                -8,
                -5
            )

        else:
            # breakout
            change = random.uniform(
                2,
                6
            )


        open_price = price


        close_price = (
            price + change
        )


        high = max(
            open_price,
            close_price
        ) + random.uniform(
            0.5,
            2
        )


        low = min(
            open_price,
            close_price
        ) - random.uniform(
            0.5,
            2
        )


        candle = {

            "open": round(
                open_price,
                2
            ),

            "high": round(
                high,
                2
            ),

            "low": round(
                low,
                2
            ),

            "close": round(
                close_price,
                2
            )
        }


        data.append(candle)


        price = close_price


    return data