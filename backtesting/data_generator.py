import random



def generate_xauusd_data(
        candles=1000,
        start_price=3350
):


    data=[]


    price=start_price



    for i in range(candles):


        move=random.uniform(
            -8,
            8
        )


        open_price=price


        close_price=price+move


        high=max(
            open_price,
            close_price
        )+random.uniform(
            0,
            5
        )


        low=min(
            open_price,
            close_price
        )-random.uniform(
            0,
            5
        )


        context={}



        # 模拟 ICT setup


        chance=random.random()



        if chance>0.92:


            context={


            "structure":{

                "trend":"BULLISH",

                "BOS":True

            },


            "liquidity":{

                "sweep":{

                    "sweep":True

                }

            },


            "fvg":[1],


            "order_block":[1]


            }



        data.append({

            "open":open_price,

            "high":high,

            "low":low,

            "close":close_price,

            "context":context


        })



        price=close_price



    return data