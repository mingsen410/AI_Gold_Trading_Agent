from position_management.position_manager import PositionManager



manager = PositionManager()



trade={


"symbol":"XAUUSD",

"direction":"BUY",

"entry":3350,

"stop_loss":3340,

"take_profit":3370

}



manager.open_position(
    trade
)



print(
    manager.get_open_positions()
)



manager.update_price(
    3375
)



print(
    manager.positions
)