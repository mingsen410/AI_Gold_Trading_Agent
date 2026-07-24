from core.logger import AgentLogger



class DashboardDataProvider:



    def __init__(self):


        self.data={


            "agent_status":
            "STOPPED",


            "account":{},


            "performance":{},


            "positions":[]


        }



    def update_status(
        self,
        status
    ):


        self.data["agent_status"]=status



    def update_account(
        self,
        account
    ):


        self.data["account"]=account



    def update_performance(
        self,
        performance
    ):


        self.data["performance"]=performance



    def update_positions(
        self,
        positions
    ):


        self.data["positions"]=positions



    def get_dashboard_data(
        self
    ):


        AgentLogger.info(

            "Dashboard data requested"

        )


        return self.data