from smc_engine.swing_detector import SwingDetector
from smc_engine.market_structure import MarketStructure
from smc_engine.choch_detector import CHoCHDetector
from smc_engine.order_block_engine import OrderBlockEngine
from smc_engine.fvg_engine import FVGEngine
from smc_engine.liquidity_engine import LiquidityEngine
from smc_engine.premium_discount_engine import PremiumDiscountEngine

from core.logger import AgentLogger



class MarketContextBuilder:



    def __init__(self):


        self.swing_detector = SwingDetector()

        self.structure_engine = MarketStructure()

        self.choch_engine = CHoCHDetector()

        self.order_block_engine = OrderBlockEngine()

        self.fvg_engine = FVGEngine()

        self.liquidity_engine = LiquidityEngine()

        self.premium_discount_engine = PremiumDiscountEngine()



    # =====================================
    # Build Market Context
    # =====================================

    def build(
        self,
        candles
    ):


        latest = candles[-1]



        # =============================
        # Swing Points
        # =============================

        swing_points = (

            self.swing_detector.detect(
                candles
            )

        )



        AgentLogger.info(

            f"Detected {len(swing_points)} swing points"

        )



        # =============================
        # Market Structure
        # =============================

        structure = (

            self.structure_engine.analyze(

                swing_points

            )

        )


        if structure is None:


            structure = {


                "trend":

                "UNKNOWN",


                "BOS":

                False,


                "CHoCH":

                False,


                "reason":

                "Not enough structure"

            }



        AgentLogger.info(

            f"Market Structure: {structure}"

        )



        # =============================
        # CHoCH
        # =============================

        choch = (

            self.choch_engine.detect(

                structure.get(
                    "trend"
                ),

                candles

            )

        )



        # =============================
        # Liquidity
        # =============================

        liquidity = (

            self.liquidity_engine.analyze(

                swing_points,

                candles

            )

        )



        # =============================
        # FVG
        # =============================

        fvg = (

            self.fvg_engine.detect(

                candles

            )

        )



        # =============================
        # Order Block
        # =============================

        order_blocks = (

            self.order_block_engine.detect(

                candles

            )

        )



        # =============================
        # Premium Discount
        # =============================

        zone_result = (

            self.premium_discount_engine.calculate(

                swing_points,

                latest["close"]

            )

        )


        zone = zone_result.get(

            "zone",

            "UNKNOWN"

        )



        # =============================
        # Volatility
        # =============================

        volatility = (

            latest["high"]

            -

            latest["low"]

        )



        context = {



            "time":

            latest.get(
                "time",
                ""
            ),



            "structure":

            structure,



            "bos":

            structure.get(
                "BOS",
                False
            ),



            "choch":

            choch,



            "liquidity":

            liquidity,



            "fvg":

            fvg,



            "order_block":

            order_blocks,



            "zone":

            zone,



            "premium_discount":

            zone_result,



            "volatility":

            volatility



        }



        AgentLogger.info(

            f"Market Context: {context}"

        )



        return context