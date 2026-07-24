import json
import os
from datetime import datetime



class TradeJournal:


    def __init__(
        self,
        file_path="trade_journal/trades.json"
    ):

        self.file_path = file_path


        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



        if not os.path.exists(
            self.file_path
        ):

            with open(
                self.file_path,
                "w"
            ) as f:

                json.dump(
                    [],
                    f,
                    indent=4
                )



    def record_trade(
        self,
        trade
    ):


        trade_record = trade.copy()


        trade_record["time"] = str(
            datetime.now()
        )



        with open(
            self.file_path,
            "r"
        ) as f:

            trades = json.load(f)



        trades.append(
            trade_record
        )



        with open(
            self.file_path,
            "w"
        ) as f:

            json.dump(
                trades,
                f,
                indent=4
            )



        print(
            "Trade saved to journal"
        )



    def get_all_trades(
        self
    ):


        with open(
            self.file_path,
            "r"
        ) as f:

            return json.load(f)