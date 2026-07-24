import logging


logger = logging.getLogger(__name__)


class MarketAnalyzer:


    def __init__(self, candles):

        self.candles = candles



    def analyze(self):


        context = {


            "structure":
            self.structure(),


            "bos":
            self.bos(),


            "choch":
            {
                "choch":False
            },


            "liquidity":
            self.liquidity(),


            "fvg":
            self.fvg(),


            "order_block":
            self.order_block(),


            "volatility":
            self.volatility()

        }


        logger.info(
            f"Market Context: {context}"
        )


        return context




    # ============================
    # Structure
    # ============================

    def structure(self):


        if len(self.candles)<3:

            return {

                "trend":"UNKNOWN"

            }



        a=self.candles[-3]
        b=self.candles[-2]
        c=self.candles[-1]



        if c["high"] > b["high"] > a["high"]:

            return {

                "trend":"BULLISH"

            }


        if c["low"] < b["low"] < a["low"]:

            return {

                "trend":"BEARISH"

            }


        return {

            "trend":"UNKNOWN"

        }





    # ============================
    # BOS
    # ============================

    def bos(self):


        if len(self.candles)<2:

            return False



        prev=self.candles[-2]

        now=self.candles[-1]


        return (

            now["high"] > prev["high"]

            or

            now["low"] < prev["low"]

        )






    # ============================
    # Liquidity Sweep
    # ============================

    def liquidity(self):


        if len(self.candles)<2:


            return {

                "buy_side_liquidity":[],

                "sell_side_liquidity":[],

                "sweep":
                {
                    "sweep":False
                }

            }



        prev=self.candles[-2]

        now=self.candles[-1]


        buy=[]

        sell=[]

        sweep=False



        if now["high"] > prev["high"]:


            buy.append({

                "type":
                "SWING_HIGH_LIQUIDITY",

                "price":
                prev["high"]

            })


            sweep=True




        if now["low"] < prev["low"]:


            sell.append({

                "type":
                "SWING_LOW_LIQUIDITY",

                "price":
                prev["low"]

            })


            sweep=True




        return {


            "buy_side_liquidity":buy,

            "sell_side_liquidity":sell,

            "sweep":
            {
                "sweep":sweep
            }

        }





    # ============================
    # FVG
    # ============================

    def fvg(self):


        result=[]


        if len(self.candles)<3:

            return result



        c1=self.candles[-3]

        c3=self.candles[-1]



        if c1["high"] < c3["low"]:


            result.append({

                "type":
                "BULLISH_FVG",

                "top":
                c3["low"],

                "bottom":
                c1["high"]

            })




        if c1["low"] > c3["high"]:


            result.append({

                "type":
                "BEARISH_FVG",

                "top":
                c1["low"],

                "bottom":
                c3["high"]

            })


        return result






    # ============================
    # Order Block
    # ============================

    def order_block(self):


        result=[]


        if len(self.candles)<2:

            return result



        prev=self.candles[-2]

        now=self.candles[-1]



        # Bullish OB


        if (

            prev["close"] < prev["open"]

            and

            now["close"] > now["open"]

        ):


            result.append({

                "type":
                "BULLISH_OB",

                "high":
                prev["high"],

                "low":
                prev["low"]

            })




        return result






    # ============================
    # Volatility
    # ============================

    def volatility(self):


        candle=self.candles[-1]


        return (

            candle["high"]

            -

            candle["low"]

        )