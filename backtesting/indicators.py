import pandas as pd



def ATR(
    df,
    period=14
):


    high=df["high"]

    low=df["low"]

    close=df["close"]



    tr=pd.concat(

        [

        high-low,

        abs(high-close.shift()),

        abs(low-close.shift())

        ],

        axis=1

    ).max(axis=1)



    atr = tr.rolling(
        period
    ).mean()



    return atr