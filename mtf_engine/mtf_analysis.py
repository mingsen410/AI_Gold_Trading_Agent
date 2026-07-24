from core.logger import AgentLogger



class MultiTimeframeAnalyzer:



    def __init__(self):

        pass



    def analyze(
        self,
        timeframe_data
    ):


        result={

            "daily":None,

            "h4":None,

            "h1":None,

            "m15":None,

            "m5":None

        }



        for tf,data in timeframe_data.items():


            result[tf]=self.analyze_structure(
                data
            )



        bias=self.calculate_bias(
            result
        )



        final={


            "timeframes":result,


            "overall_bias":bias

        }



        AgentLogger.info(

            f"MTF Analysis: {final}"

        )


        return final




    def analyze_structure(
        self,
        data
    ):


        if data["trend"]=="UP":


            return "BULLISH"



        elif data["trend"]=="DOWN":


            return "BEARISH"



        return "NEUTRAL"




    def calculate_bias(
        self,
        analysis
    ):


        bullish=0

        bearish=0



        for value in analysis.values():


            if value=="BULLISH":

                bullish+=1


            elif value=="BEARISH":

                bearish+=1



        if bullish > bearish:

            return "BUY BIAS"



        elif bearish > bullish:

            return "SELL BIAS"



        return "NEUTRAL"