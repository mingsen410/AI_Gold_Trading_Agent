from smc_engine.premium_discount_engine import PremiumDiscountEngine




swing_points = [


    {
        "type":"HIGH",
        "price":3400,
        "index":1
    },


    {
        "type":"LOW",
        "price":3300,
        "index":2
    }


]



current_price = 3350



engine = PremiumDiscountEngine()



result = engine.analyze(

    swing_points,

    current_price

)



print("\n========== PREMIUM DISCOUNT ==========\n")

print(result)