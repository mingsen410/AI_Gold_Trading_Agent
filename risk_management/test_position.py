from risk_management.position_sizing import PositionSizer



engine = PositionSizer(
    risk_percent=1
)



lot = engine.calculate_lot_size(

    balance=10000,

    entry=3350,

    stop_loss=3340

)



print(
    lot
)