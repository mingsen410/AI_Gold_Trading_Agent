from data_engine.market_feed import MarketFeed



feed = MarketFeed()



feed.connect()



for i in range(5):


    print(

        feed.get_tick()

    )