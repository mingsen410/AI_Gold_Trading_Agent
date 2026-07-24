from datetime import datetime, timezone

from core.logger import AgentLogger



class KillZone:



    def __init__(self):


        self.sessions = {


            "LONDON":

            (

                7,

                10

            ),


            "NEW_YORK":

            (

                12,

                15

            )

        }




    def is_active(self):


        now = datetime.now(
            timezone.utc
        )


        hour = now.hour



        for name, time_range in self.sessions.items():


            start, end = time_range



            if start <= hour < end:


                AgentLogger.info(

                    f"Active Kill Zone: {name}"

                )


                return {


                    "active":
                    True,


                    "session":
                    name


                }



        return {


            "active":
            False,


            "session":
            None


        }