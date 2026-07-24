from confluence_engine.confluence import ICTConfluenceEngine



engine = ICTConfluenceEngine()



signals={


"bias":25,

"liquidity":20,

"structure":20,

"order_block":15,

"fvg":10,

"session":5,

"risk":5

}



result = engine.evaluate(
    signals
)



print(result)