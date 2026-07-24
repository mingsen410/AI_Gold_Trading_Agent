from data_engine.market_feed import MarketFeed


from data_engine.data_pipeline import DataPipeline





feed = MarketFeed()


pipeline = DataPipeline()



feed.connect()




for i in range(5):


    tick = feed.get_tick()



    print(

        "TICK:",

        tick

    )



    candle = pipeline.process_tick(

        tick

    )



    print(

        "CANDLE:",

        candle

    )




pipeline.close_candle()



print(

pipeline.candle_manager.get_candles(

"M1"

)

)