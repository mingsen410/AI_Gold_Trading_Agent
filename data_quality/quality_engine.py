from core.logger import AgentLogger


class DataQualityEngine:


    def __init__(self):

        self.errors = []



    def check_candle(
        self,
        candle
    ):


        valid = True


        if candle["high"] < max(
            candle["open"],
            candle["close"]
        ):

            self.errors.append(
                "Invalid High price"
            )

            valid = False



        if candle["low"] > min(
            candle["open"],
            candle["close"]
        ):

            self.errors.append(
                "Invalid Low price"
            )

            valid = False



        return valid



    def check_dataset(
        self,
        candles
    ):


        self.errors = []


        valid_count = 0


        for candle in candles:


            if self.check_candle(
                candle
            ):

                valid_count += 1



        result = {


            "total":

            len(candles),


            "valid":

            valid_count,


            "errors":

            self.errors

        }



        AgentLogger.info(
            f"Data Quality Checked: {result}"
        )


        return result