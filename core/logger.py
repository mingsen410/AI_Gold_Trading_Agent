import logging
import os
from datetime import datetime


LOG_FOLDER = "logs"


if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)


log_file = (
    f"{LOG_FOLDER}/"
    f"agent_{datetime.now().strftime('%Y%m%d')}.log"
)


logging.basicConfig(

    level=logging.INFO,

    format=
    "%(asctime)s | %(levelname)s | %(message)s",

    handlers=[

        logging.FileHandler(
            log_file
        ),

        logging.StreamHandler()

    ]

)


class AgentLogger:


    @staticmethod
    def info(message):

        logging.info(message)



    @staticmethod
    def warning(message):

        logging.warning(message)



    @staticmethod
    def error(message):

        logging.error(message)