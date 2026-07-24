from core.logger import AgentLogger



class ICTEntryLogic:


    def __init__(
        self,
        minimum_score=3
    ):

        self.minimum_score = minimum_score



    def analyze(
        self,
        context
    ):


        score = 0

        reasons = []

        signal = "WAIT"



        structure = context.get(
            "structure",
            {}
        )


        trend = structure.get(
            "trend",
            "UNKNOWN"
        )


        bos = structure.get(
            "BOS",
            False
        )


        zone = context.get(
            "zone",
            "UNKNOWN"
        )


        fvg = context.get(
            "fvg",
            []
        )


        order_blocks = context.get(
            "order_block",
            []
        )


        liquidity = context.get(
            "liquidity",
            {}
        )


        sweep = liquidity.get(
            "sweep",
            {}
        ).get(
            "sweep",
            False
        )



        AgentLogger.info(

            f"ICT INPUT trend={trend}, BOS={bos}, zone={zone}, FVG={len(fvg)}, OB={len(order_blocks)}"

        )



        # ==================================================
        # BULLISH
        # ==================================================

        if trend == "BULLISH":


            score += 1

            reasons.append(
                "Bullish structure"
            )



            if bos:

                score += 1

                reasons.append(
                    "BOS confirmed"
                )



            if len(fvg)>0:

                score += 1

                reasons.append(
                    "Bullish FVG detected"
                )



            if len(order_blocks)>0:

                score += 1

                reasons.append(
                    "Bullish Order Block detected"
                )



            if sweep:

                score += 1

                reasons.append(
                    "Liquidity sweep"
                )



            if zone == "DISCOUNT":

                score += 1

                reasons.append(
                    "Discount zone"
                )



            if score >= self.minimum_score:


                signal="BUY"




        # ==================================================
        # BEARISH
        # ==================================================

        elif trend == "BEARISH":


            score +=1


            reasons.append(
                "Bearish structure"
            )



            if bos:

                score+=1

                reasons.append(
                    "BOS confirmed"
                )



            if len(fvg)>0:

                score+=1

                reasons.append(
                    "Bearish FVG detected"
                )



            if len(order_blocks)>0:

                score+=1

                reasons.append(
                    "Bearish Order Block detected"
                )



            if sweep:

                score+=1

                reasons.append(
                    "Liquidity sweep"
                )



            if zone=="PREMIUM":

                score+=1

                reasons.append(
                    "Premium zone"
                )



            if score >= self.minimum_score:

                signal="SELL"




        # ==================================================
        # FALLBACK TEST MODE
        # ==================================================

        elif trend=="UNKNOWN":


            if len(fvg)>0 and len(order_blocks)>0:


                score=3


                signal="BUY"


                reasons.append(
                    "Fallback ICT setup: FVG + OB"
                )



        confidence = min(
            score / 5,
            1
        )



        result={


            "signal":signal,


            "score":score,


            "confidence":round(
                confidence,
                2
            ),


            "reason":reasons

        }



        AgentLogger.info(

            f"ICT Entry Decision: {result}"

        )


        return result