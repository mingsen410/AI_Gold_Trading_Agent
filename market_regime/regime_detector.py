from core.logger import AgentLogger



class MarketRegimeDetector:



    def __init__(self):

        pass



    def detect(
        self,
        market_data
    ):


        score = 0



        # 趋势判断

        if market_data["ma20"] > market_data["ma50"]:

            score += 30



        # 波动判断

        if market_data["atr"] > market_data["average_atr"]:

            score += 20



        # 结构判断

        if market_data["bos"] > 2:

            score += 30



        # 成交量

        if market_data["volume_increase"]:

            score += 20



        if score >=70:


            regime="TRENDING"

            recommendation="ALLOW"



        elif score >=40:


            regime="RANGING"

            recommendation="CAUTION"



        else:


            regime="LOW_QUALITY"

            recommendation="BLOCK"



        result={


            "regime":regime,


            "score":score,


            "recommendation":recommendation

        }



        AgentLogger.info(

            f"Market regime: {result}"

        )


        return result