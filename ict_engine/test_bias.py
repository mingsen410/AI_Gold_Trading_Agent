from ict_engine.bias import BiasEngine



engine = BiasEngine()



structure = {


"trend":

"BULLISH",


"BOS":

True


}



result = engine.calculate(
    structure
)


print(result)