import logging


logger = logging.getLogger(__name__)


class RiskManager:


    def __init__(
        self,
        risk_percent=1,
        atr_multiplier_sl=1.5,
        atr_multiplier_tp=3
    ):

        self.risk_percent = risk_percent

        self.atr_multiplier_sl = atr_multiplier_sl

        self.atr_multiplier_tp = atr_multiplier_tp



    # =========================
    # ATR Calculation
    # =========================

    def calculate_atr(
        self,
        candles,
        period=14
    ):


        if len(candles) <= period:

            return None



        true_ranges = []



        for i in range(1, len(candles)):


            high = candles[i]["high"]

            low = candles[i]["low"]

            previous_close = candles[i-1]["close"]



            tr = max(

                high - low,

                abs(high - previous_close),

                abs(low - previous_close)

            )


            true_ranges.append(tr)



        atr = sum(
            true_ranges[-period:]
        ) / period



        return atr




    # =========================
    # Dynamic SL / TP
    # =========================

    def calculate_sl_tp(
        self,
        entry,
        candles,
        direction="BUY"
    ):


        atr = self.calculate_atr(
            candles
        )



        if atr is None:

            atr = 10



        sl_distance = (

            atr *

            self.atr_multiplier_sl

        )



        tp_distance = (

            atr *

            self.atr_multiplier_tp

        )



        if direction == "BUY":


            sl = entry - sl_distance

            tp = entry + tp_distance



        else:


            sl = entry + sl_distance

            tp = entry - tp_distance




        return {


            "atr":
                round(
                    atr,
                    2
                ),



            "sl":
                round(
                    sl,
                    2
                ),



            "tp":
                round(
                    tp,
                    2
                ),



            "sl_distance":
                round(
                    sl_distance,
                    2
                )

        }




    # =========================
    # Position Size
    # =========================

    def calculate_position_size(
        self,
        balance,
        entry,
        sl
    ):


        # Account risk amount

        risk_amount = (

            balance *

            self.risk_percent /

            100

        )



        # Stop loss distance

        stop_distance = abs(

            entry - sl

        )



        if stop_distance <= 0:

            return 0.01



        # XAUUSD calculation
        #
        # 1 lot gold
        # approximately $100 per $1 move


        lot = (

            risk_amount /

            (
                stop_distance *

                100

            )

        )



        # MT5 minimum

        if lot < 0.01:

            lot = 0.01



        return round(
            lot,
            2
        )