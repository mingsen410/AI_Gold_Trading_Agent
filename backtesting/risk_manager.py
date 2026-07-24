class RiskManager:


    def __init__(
        self,
        balance=10000,
        risk_percent=1
    ):

        self.balance=balance

        self.risk_percent=risk_percent



    def position_size(
        self,
        entry,
        sl
    ):


        risk_money=(

            self.balance *
            self.risk_percent /
            100

        )


        distance=abs(
            entry-sl
        )


        if distance==0:

            return 0



        return round(

            risk_money/distance,

            2

        )



    def calculate_sl_tp(
        self,
        entry,
        atr,
        direction
    ):


        if direction=="BUY":


            sl = entry - atr*1.5

            tp = entry + atr*3



        else:


            sl = entry + atr*1.5

            tp = entry - atr*3



        return (

            round(sl,2),

            round(tp,2)

        )