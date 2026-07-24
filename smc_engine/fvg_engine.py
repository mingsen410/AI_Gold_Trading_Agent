from core.logger import AgentLogger





class FVGEngine:



    def __init__(self):


        self.fvg_zones=[]






    def detect(

        self,

        candles,

        minimum_gap=1.5

    ):



        """

        candles:

        最近K线数据



        返回FVG区域

        """



        fvgs=[]




        if len(candles)<3:


            return fvgs





        for i in range(len(candles)-2):



            c1=candles[i]


            c2=candles[i+1]


            c3=candles[i+2]





            # Bullish FVG


            if c3["low"] - c1["high"] >= minimum_gap:



                fvgs.append(



                    {


                    "type":

                    "BULLISH_FVG",



                    "top":

                    c3["low"],



                    "bottom":

                    c1["high"],



                    "size":

                    round(

                    c3["low"]-c1["high"],

                    2

                    )


                    }


                )






            # Bearish FVG


            elif c1["low"] - c3["high"] >= minimum_gap:



                fvgs.append(



                    {


                    "type":

                    "BEARISH_FVG",



                    "top":

                    c1["low"],



                    "bottom":

                    c3["high"],



                    "size":

                    round(

                    c1["low"]-c3["high"],

                    2

                    )


                    }


                )




        self.fvg_zones=fvgs



        return fvgs