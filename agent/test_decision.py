from agent.decision_engine import DecisionEngine



engine = DecisionEngine()



decision = engine.evaluate(

    {

        "bias":

        "BULLISH"

    },


    {

        "signal":

        "BUY"

    },


    True

)



print(decision)