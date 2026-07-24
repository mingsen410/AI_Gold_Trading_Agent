import csv
from datetime import datetime

from core.logger import AgentLogger



class HistoricalDataLoader:



    def __init__(
        self,
        file_path
    ):

        self.file_path=file_path



    def load(self):

        candles=[]


        with open(
            self.file_path,
            "r"
        ) as file:


            reader=csv.DictReader(file)


            for row in reader:


                candle={


                    "time":

                    datetime.strptime(
                        row["time"],
                        "%Y-%m-%d %H:%M:%S"
                    ),


                    "open":

                    float(row["open"]),


                    "high":

                    float(row["high"]),


                    "low":

                    float(row["low"]),


                    "close":

                    float(row["close"]),


                    "volume":

                    float(row["volume"])

                }


                candles.append(
                    candle
                )



        AgentLogger.info(

            f"Historical candles loaded: {len(candles)}"

        )


        return candles