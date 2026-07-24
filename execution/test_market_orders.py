from execution.market_orders import MarketOrderEngine




engine = MarketOrderEngine()



order = engine.create_order_request(

    symbol="XAUUSD",

    direction="BUY",

    volume=0.10,

    entry=3350,

    stop_loss=3335,

    take_profit=3380

)



result = engine.execute_order(

    order

)



print(result)