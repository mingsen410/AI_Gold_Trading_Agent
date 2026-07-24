import json
import os

from core.logger import AgentLogger



class AgentMemory:



    def __init__(
        self,
        file_path="agent_memory.json"
    ):

        self.file_path = file_path


        self.memory = {


            "trades":[],

            "sessions":[],

            "performance":{}

        }


        self.load()



    def load(self):


        if os.path.exists(
            self.file_path
        ):


            with open(
                self.file_path,
                "r"
            ) as file:


                self.memory=json.load(
                    file
                )



    def save(self):


        with open(
            self.file_path,
            "w"
        ) as file:


            json.dump(

                self.memory,

                file,

                indent=4

            )



    def add_trade(
        self,
        trade
    ):


        self.memory["trades"].append(
            trade
        )


        self.save()



        AgentLogger.info(
            "Trade memory saved"
        )



    def add_session(
        self,
        session
    ):


        self.memory["sessions"].append(
            session
        )


        self.save()



    def update_performance(
        self,
        performance
    ):


        self.memory["performance"]=performance


        self.save()



    def get_memory(self):


        return self.memory