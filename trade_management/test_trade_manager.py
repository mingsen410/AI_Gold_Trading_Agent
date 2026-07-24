from paper_trading.paper_account import PaperAccount

from execution.position_manager import PositionManager

from trade_management.trade_manager import TradeManager




account = PaperAccount()


pm = PositionManager()


manager = TradeManager(
    pm
)



order = {


    "symbol":
    "XAUUSD",


    "action":
    "BUY",


    "entry":
    3380,


    "volume":
    1,


    "sl":
    3370,


    "tp":
    3420

}



position = account.open_trade(order)



prices=[

3385,

3390,

3400,

3410,

3420

]



for price in prices:


    print("\nPRICE:",price)


    result = manager.update_position(

        position,

        price

    )


    print(result)


    print(position.__dict__)