from execution_engine.execution import TradeExecutionEngine

from risk_management.risk_engine import RiskManagementEngine

from position_management.position_manager import PositionManager



risk = RiskManagementEngine()


position = PositionManager()



executor = TradeExecutionEngine(

    risk,

    position

)



signal={


"symbol":"XAUUSD",

"direction":"BUY",

"entry":3350,

"stop_loss":3340,

"take_profit":3370,

"stop_loss_distance":10

}



trade = executor.execute(

    signal,

    10000

)



print(trade)


print(
    position.positions
)