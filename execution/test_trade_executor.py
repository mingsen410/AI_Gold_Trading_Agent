from execution.trade_executor import TradeExecutor




executor = TradeExecutor()




signal = {


"direction":

"BUY",


"entry":

3350,


"stop_loss":

3335,


"take_profit":

3380

}




account = {


"balance":

10000,


"daily_loss":

100,


"loss_count":

0,


"positions":

0,


"spread":

20

}




result = executor.execute_trade(

signal,

account

)



print(result)