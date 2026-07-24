from mt5_bridge.bridge_service import MT5BridgeService



bridge=MT5BridgeService()



print(

bridge.start()

)



print(

bridge.market_data()

)



order={


"symbol":"XAUUSD",

"action":"BUY",

"volume":0.1,

"sl":3340,

"tp":3370

}



print(

bridge.execute_order(order)

)



print(

bridge.positions()

)