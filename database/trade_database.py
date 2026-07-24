import sqlite3
from datetime import datetime

from core.logger import AgentLogger



class TradeDatabase:


    def __init__(
        self,
        db_name="trade_history.db"
    ):

        self.connection = sqlite3.connect(
            db_name
        )

        self.create_table()



    def create_table(self):


        cursor = self.connection.cursor()


        cursor.execute(
            """

            CREATE TABLE IF NOT EXISTS trades (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            symbol TEXT,

            direction TEXT,

            session TEXT,

            bias TEXT,

            confidence INTEGER,

            entry REAL,

            exit REAL,

            result TEXT,

            r_multiple REAL

            )

            """
        )


        self.connection.commit()



    def save_trade(
        self,
        trade
    ):


        cursor = self.connection.cursor()


        cursor.execute(

            """

            INSERT INTO trades

            (

            timestamp,

            symbol,

            direction,

            session,

            bias,

            confidence,

            entry,

            exit,

            result,

            r_multiple

            )


            VALUES (?,?,?,?,?,?,?,?,?,?)

            """,

            (

            datetime.now().isoformat(),

            trade["symbol"],

            trade["direction"],

            trade["session"],

            trade["bias"],

            trade["confidence"],

            trade["entry"],

            trade["exit"],

            trade["result"],

            trade["r_multiple"]

            )

        )


        self.connection.commit()


        AgentLogger.info(
            "Trade saved into database"
        )



    def get_all_trades(self):


        cursor = self.connection.cursor()


        cursor.execute(
            "SELECT * FROM trades"
        )


        return cursor.fetchall()