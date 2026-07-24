from mt5_connector.mt5_interface import MT5Connector



mt5 = MT5Connector()



print(
    mt5.connect()
)



print(
    mt5.get_account_info()
)



print(
    mt5.get_price(
        "XAUUSD"
    )
)



order={


"symbol":"XAUUSD",

"type":"BUY",

"volume":0.1,

"price":3350

}



print(
    mt5.send_order(
        order
    )
)