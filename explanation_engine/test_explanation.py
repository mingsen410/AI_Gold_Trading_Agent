from explanation_engine.explanation import TradeExplanationEngine



engine = TradeExplanationEngine()



decision={


"symbol":"XAUUSD",

"decision":"BUY",

"score":91,


"factors":

{

"bias":25,

"structure":22,

"liquidity":18,

"setup":15,

"session":8

}

}



result = engine.generate(
    decision
)


print(result)