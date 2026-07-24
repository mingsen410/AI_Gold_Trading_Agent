from feedback_engine.feedback import FeedbackEngine



engine = FeedbackEngine()



for i in range(8):

    engine.record_trade(

        "OB_FVG_LIQUIDITY",

        1

    )



for i in range(2):

    engine.record_trade(

        "OB_FVG_LIQUIDITY",

        -1

    )



print(

engine.calculate_win_rate(

"OB_FVG_LIQUIDITY"

)

)



print(

engine.get_adjustment(

"OB_FVG_LIQUIDITY"

)

)