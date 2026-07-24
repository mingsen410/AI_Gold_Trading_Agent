from abc import ABC, abstractmethod


class BrokerInterface(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_tick(self, symbol):
        pass

    @abstractmethod
    def get_candles(self, symbol, timeframe, count):
        pass

    @abstractmethod
    def place_order(
        self,
        symbol,
        order_type,
        volume,
        sl,
        tp
    ):
        pass

    @abstractmethod
    def close_order(self, ticket):
        pass

    @abstractmethod
    def modify_order(
        self,
        ticket,
        sl,
        tp
    ):
        pass

    @abstractmethod
    def account_info(self):
        pass