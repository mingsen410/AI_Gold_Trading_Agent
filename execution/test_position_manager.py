from execution.position_manager import PositionManager



manager = PositionManager()



position = {


"direction":

"BUY",


"entry":

3350,


"stop_loss":

3335,


"current_price":

3380


}




result = manager.manage_position(

    position

)



print(result)