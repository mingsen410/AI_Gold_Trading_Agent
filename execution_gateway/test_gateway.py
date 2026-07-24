from execution_gateway.gateway_client import GatewayClient



client=GatewayClient()



print(
    client.get_tick()
)



print(
    client.account()
)



order={


"symbol":
"XAUUSD",


"action":
"BUY",


"volume":
0.1,


"sl":
3340,


"tp":
3370

}



print(

client.send_order(order)

)