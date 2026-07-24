from execution.trade_monitor import TradeMonitor



position={


"symbol":"XAUUSD",

"direction":"BUY",

"entry":3380,

"sl":3370,

"tp":3400

}



monitor=TradeMonitor()



prices=[3385,3390,3400]



for p in prices:


    print(
        "\nPRICE:",
        p
    )


    result=monitor.update(
        position,
        p
    )


    print(result)