from ai_brain.decision_engine import DecisionEngine




ict_signal = {


    "signal":

    "BUY",


    "confidence":

    0.85,


    "reason":

    [

        "Bullish structure",

        "BOS confirmed",

        "Liquidity sweep",

        "Discount entry"

    ]



}




engine = DecisionEngine()



result = engine.decide(

    ict_signal

)



print("\n========== AI DECISION ==========\n")

print(result)