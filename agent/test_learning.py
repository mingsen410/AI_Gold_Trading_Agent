from agent.learning_engine import LearningEngine




engine = LearningEngine()




engine.record_trade(

{

"setup":

"ICT_BULLISH",


"result":

"WIN",


"profit":

200

}

)




engine.record_trade(

{

"setup":

"ICT_BULLISH",


"result":

"LOSS",


"profit":

-100

}

)




print(

engine.calculate_statistics()

)




print(

engine.evaluate_setup(

"ICT_BULLISH"

)

)