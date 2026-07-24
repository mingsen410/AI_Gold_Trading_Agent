from risk_engine.risk_manager import RiskManager




engine = RiskManager()



result = engine.calculate(

    balance=10000,

    entry=3350,

    stop_loss=3340,

    take_profit=3370

)



print("\n========== RISK RESULT ==========\n")

print(result)