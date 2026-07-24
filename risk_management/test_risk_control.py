from risk_management.risk_control import RiskControl




engine = RiskControl()




result = engine.approve_trade(

    balance=10000,

    daily_loss=100,

    loss_count=0,

    positions=0,

    spread=20

)




print(result)