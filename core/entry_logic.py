import logging

logger = logging.getLogger(__name__)


class ICTEntryLogic:

    def __init__(self):
        pass


    def generate_signal(self, context):

        return self.evaluate(context)



    def evaluate(self, context):

        score = 0
        reasons = []


        # =====================
        # Market Structure
        # =====================

        structure = context.get(
            "structure",
            {}
        )

        trend = structure.get(
            "trend",
            "UNKNOWN"
        )


        if trend == "BULLISH":
            score += 1
            reasons.append(
                "Bullish structure"
            )


        # =====================
        # BOS
        # =====================

        if structure.get(
            "BOS",
            False
        ):

            score += 1

            reasons.append(
                "Break of Structure"
            )


        # =====================
        # Liquidity Sweep
        # =====================

        liquidity = context.get(
            "liquidity",
            {}
        )


        sweep = liquidity.get(
            "sweep",
            {}
        )


        if isinstance(sweep,dict):

            if sweep.get(
                "sweep",
                False
            ):

                score +=1

                reasons.append(
                    "Liquidity sweep"
                )


        # =====================
        # FVG
        # =====================

        fvg = context.get(
            "fvg",
            []
        )


        if isinstance(fvg,list):

            if len(fvg)>0:

                score+=1

                reasons.append(
                    "FVG detected"
                )


        # =====================
        # Order Block
        # =====================

        ob = context.get(
            "order_block",
            []
        )


        if isinstance(ob,list):

            if len(ob)>0:

                score+=1

                reasons.append(
                    "Order Block detected"
                )


        # =====================
        # Decision
        # =====================

        confidence = score / 5


        if score >=4:

            signal="BUY"


        else:

            signal="WAIT"



        result={

            "signal":signal,

            "score":score,

            "confidence":round(
                confidence,
                2
            ),

            "reason":reasons

        }


        logger.info(
            f"ICT Entry Decision: {result}"
        )


        return result