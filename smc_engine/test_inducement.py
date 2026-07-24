from smc_engine.inducement import InducementDetector



engine = InducementDetector()



swings=[


{

"type":"LOW",

"price":3300

},


{

"type":"LOW",

"price":3305

},


{

"type":"HIGH",

"price":3350

}


]



result = engine.detect(
    swings
)


print(result)