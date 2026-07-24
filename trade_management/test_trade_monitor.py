from trade_management.position_manager import PositionManager




manager = PositionManager()




position = {


    "symbol":

    "XAUUSD",



    "direction":

    "BUY",



    "entry":

    3380,



    "initial_stop_loss":

    3370,



    "stop_loss":

    3370,



    "take_profit":

    3420,



    "volume":

    1,



    "current_price":

    3380,



    "breakeven_done":

    False,



    "partial_closed":

    False,



    "trailing_active":

    False

}







prices = [

    3385,

    3390,

    3400,

    3410,

    3420

]







for price in prices:



    print(

        "\nPRICE:",

        price

    )



    position["current_price"] = price





    result = manager.manage_position(

        position

    )



    print(result)




    manager.update_position(

        position,

        result

    )



    print(position)