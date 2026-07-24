from core.logger import AgentLogger





class OrderBlockEngine:



    def __init__(self):


        self.blocks=[]






    def detect(

        self,

        candles,

        minimum_move=5

    ):



        """

        检测Order Block


        candles:

        OHLC数据



        minimum_move:

        最小推动幅度

        """



        blocks=[]



        if len(candles)<2:


            return blocks





        for i in range(len(candles)-1):


            previous=candles[i]


            current=candles[i+1]





            # Bullish OB



            if (


                previous["close"]

                <

                previous["open"]



                and



                current["close"]

                >

                previous["high"]



                and



                current["close"]

                -

                current["open"]

                >= minimum_move


            ):



                blocks.append(



                    {


                    "type":

                    "BULLISH_OB",



                    "high":

                    previous["high"],



                    "low":

                    previous["low"]


                    }


                )







            # Bearish OB



            elif (


                previous["close"]

                >

                previous["open"]



                and



                current["close"]

                <

                previous["low"]



                and



                previous["open"]

                -

                previous["close"]

                >= minimum_move


            ):



                blocks.append(



                    {


                    "type":

                    "BEARISH_OB",



                    "high":

                    previous["high"],



                    "low":

                    previous["low"]


                    }


                )




        self.blocks=blocks



        return blocks