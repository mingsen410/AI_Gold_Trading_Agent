from smc_engine.structure_analyzer import StructureAnalyzer



engine = StructureAnalyzer()




swings = [


{

"type":"HIGH",

"price":3300

},


{

"type":"LOW",

"price":3250

},


{

"type":"HIGH",

"price":3350

},


{

"type":"LOW",

"price":3320

}


]





result = engine.analyze(

swings

)



print(result)