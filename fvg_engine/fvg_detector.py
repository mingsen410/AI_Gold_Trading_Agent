from core.logger import AgentLogger



class FVGDetector:



    def __init__(
        self,
        min_size=1
    ):

        self.min_size = min_size



    def detect(
        self,
        candles
    ):


        fvgs=[]


        for i in range(
            len(candles)-2
        ):


            c1=candles[i]

            c2=candles[i+1]

            c3=candles[i+2]



            # Bullish FVG

            if c3["low"] > c1["high"]:


                size = (
                    c3["low"]
                    -
                    c1["high"]
                )



                if size >= self.min_size:


                    fvgs.append(

                    {

                    "type":
                    "BULLISH_FVG",


                    "high":
                    c3["low"],


                    "low":
                    c1["high"],


                    "size":
                    size,


                    "quality":
                    self.calculate_quality(size)

                    }

                    )



            # Bearish FVG

            if c3["high"] < c1["low"]:


                size = (

                    c1["low"]

                    -

                    c3["high"]

                )



                if size >= self.min_size:


                    fvgs.append(

                    {

                    "type":
                    "BEARISH_FVG",


                    "high":
                    c1["low"],


                    "low":
                    c3["high"],


                    "size":
                    size,


                    "quality":
                    self.calculate_quality(size)

                    }

                    )



        AgentLogger.info(

            f"FVG detected: {len(fvgs)}"

        )


        return fvgs




    def calculate_quality(
        self,
        size
    ):


        if size >=10:

            return 90


        elif size >=5:

            return 75


        else:

            return 60