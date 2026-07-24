from risk_management.risk_engine import RiskManagementEngine



engine = RiskManagementEngine()



risk = engine.calculate_risk_amount(
    10000
)


lot = engine.calculate_position_size(

    10000,

    500

)


print(
    "Risk Amount:",
    risk
)


print(
    "Lot Size:",
    lot
)



print(
    "Can Trade:",
    engine.can_trade()
)



engine.update_result(
    -1
)


engine.update_result(
    -1
)


engine.update_result(
    -1
)


print(
    "Can Trade After Losses:",
    engine.can_trade()
)