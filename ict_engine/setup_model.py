from core.logger import AgentLogger



class ICTSetupModel:



    def __init__(self):


        self.signal = None




    def check_liquidity_sweep(
        self,
        liquidity_data
    ):


        if liquidity_data is None:

            return False



        bsl = liquidity_data.get(
            "BSL"
        )


        ssl = liquidity_data.get(
            "SSL"
        )



        if len(bsl) > 0 or len(ssl) > 0:


            return True



        return False





    def check_fvg(
        self,
        fvg_data,
        direction
    ):



        if direction == "BUY":


            return len(

                fvg_data.get(
                    "bullish",
                    []

                )

            ) > 0




        if direction == "SELL":


            return len(

                fvg_data.get(
                    "bearish",
                    []

                )

            ) > 0




        return False





    def generate_signal(
        self,
        bias,
        liquidity,
        fvg,
        killzone
    ):



        # 时间过滤

        if not killzone.get(
            "active",
            False
        ):


            return {


                "signal":
                "NONE",


                "reason":
                "Outside Kill Zone"

            }




        current_bias = bias.get(
            "bias"
        )



        # BUY MODEL


        if current_bias == "BULLISH":



            liquidity_ok = self.check_liquidity_sweep(
                liquidity
            )


            fvg_ok = self.check_fvg(
                fvg,
                "BUY"
            )



            if liquidity_ok and fvg_ok:



                result = {


                    "signal":

                    "BUY",


                    "reason":

                    "ICT Bullish Model Confirmed"

                }



                AgentLogger.info(
                    result
                )


                return result






        # SELL MODEL


        if current_bias == "BEARISH":



            liquidity_ok = self.check_liquidity_sweep(
                liquidity
            )


            fvg_ok = self.check_fvg(
                fvg,
                "SELL"
            )



            if liquidity_ok and fvg_ok:



                result = {


                    "signal":

                    "SELL",


                    "reason":

                    "ICT Bearish Model Confirmed"

                }



                AgentLogger.info(
                    result
                )


                return result





        return {


            "signal":

            "NONE",


            "reason":

            "Conditions not satisfied"

        }