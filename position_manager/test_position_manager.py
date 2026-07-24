from position_manager.position_manager import PositionManager




position = {


    "symbol":

    "XAUUSD",


    "direction":

    "BUY",


    "entry":

    3350,


    "sl":

    3340,


    "tp":

    3390

}





manager = PositionManager()



print("\n===== INITIAL POSITION =====")

print(position)




result = manager.manage(

    position,

    current_price=3370

)



print("\n===== AFTER MANAGEMENT =====")

print(result)