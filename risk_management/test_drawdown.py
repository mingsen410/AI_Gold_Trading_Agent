from risk_management.drawdown import DrawdownMonitor



engine = DrawdownMonitor()



print(

engine.check_status(

10000

)

)



print(

engine.check_status(

9000

)

)



print(

engine.check_status(

7500

)

)