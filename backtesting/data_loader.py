import pandas as pd



class DataLoader:


    def __init__(
        self,
        filename
    ):

        self.filename = filename



    def load(self):

        df = pd.read_csv(
            self.filename
        )


        df.columns = [
            c.lower()
            for c in df.columns
        ]


        if "time" in df.columns:

            df["time"] = pd.to_datetime(
                df["time"]
            )


        df = df.sort_values(
            "time"
        )


        df.reset_index(
            drop=True,
            inplace=True
        )


        return df