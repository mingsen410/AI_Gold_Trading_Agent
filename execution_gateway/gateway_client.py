import requests


class GatewayClient:


    def __init__(
        self,
        url="http://127.0.0.1:8000"
    ):

        self.url = url



    def get_tick(self):

        response = requests.get(

            self.url + "/market/tick"

        )

        return response.json()



    def send_order(
        self,
        order
    ):

        response = requests.post(

            self.url + "/trade/order",

            json=order

        )

        return response.json()



    def account(self):

        response = requests.get(

            self.url + "/account"

        )

        return response.json()