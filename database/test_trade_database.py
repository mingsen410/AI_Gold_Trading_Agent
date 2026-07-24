from database.trade_database import TradeDatabase



db = TradeDatabase()



trade = {


"symbol":"XAUUSD",

"direction":"BUY",

"session":"LONDON",

"bias":"BULLISH",

"confidence":88,

"entry":3350.5,

"exit":3360.5,

"result":"WIN",

"r_multiple":2

}



db.save_trade(
    trade
)



data = db.get_all_trades()


print(data)