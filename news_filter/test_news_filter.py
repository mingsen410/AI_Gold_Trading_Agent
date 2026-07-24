from news_filter.news_filter import NewsFilterEngine



engine = NewsFilterEngine()



event={


"event":"CPI",

"impact":"HIGH",

"minutes_to_event":20

}



result = engine.check(
    event
)



print(result)