from filters.trade_filter_pipeline import TradeFilterPipeline



pipeline = TradeFilterPipeline()



def session_filter(setup):


    if setup["session"] == "LONDON":


        return {


            "allowed":True

        }


    return {


        "allowed":False,


        "reason":"Wrong session"

    }





def confidence_filter(setup):


    if setup["confidence"] >= 80:


        return {


            "allowed":True

        }


    return {


        "allowed":False,


        "reason":"Low AI confidence"

    }





pipeline.add_filter(
    session_filter
)


pipeline.add_filter(
    confidence_filter
)




setup={

"session":"LONDON",

"confidence":85

}




result = pipeline.run(
    setup
)



print(result)