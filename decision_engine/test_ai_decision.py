from decision_engine.ai_decision import AIDecisionEngine



engine = AIDecisionEngine()



factors={


"bias":25,

"structure":22,

"liquidity":18,

"setup":15,

"session":8,

"risk":5

}



result = engine.decide(

    factors

)



print(result)