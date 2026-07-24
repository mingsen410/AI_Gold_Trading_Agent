import csv
import os


class TradeLogger:


    def __init__(
        self,
        filename="trades.csv"
    ):

        self.filename = filename


        if not os.path.exists(filename):

            with open(
                filename,
                "w",
                newline=""
            ) as f:

                writer = csv.writer(f)

                writer.writerow(
                    [
                        "symbol",
                        "direction",
                        "entry",
                        "exit",
                        "status",
                        "pnl"
                    ]
                )


    def log(self,trade):


        with open(
            self.filename,
            "a",
            newline=""
        ) as f:


            writer = csv.writer(f)


            writer.writerow(
                [
                    trade.get("symbol"),
                    trade.get("direction"),
                    trade.get("entry"),
                    trade.get("exit"),
                    trade.get("status"),
                    trade.get("pnl")
                ]
            )