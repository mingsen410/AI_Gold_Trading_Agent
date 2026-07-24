from ict_engine.entry_logic import ICTEntryLogic



context = {


"structure":

{

"trend":"BULLISH",

"BOS":True

},


"liquidity":

{

"sweep":

{

"sweep":True,

"direction":"BULLISH"

}

},


"zone":

"DISCOUNT",


"fvg":

[

{

"type":

"BULLISH_FVG"

}

],


"order_block":

[

{

"type":

"BULLISH_OB"

}

]


}



engine = ICTEntryLogic()



result = engine.analyze(

context

)


print("\n========== ICT ENTRY ==========\n")

print(result)