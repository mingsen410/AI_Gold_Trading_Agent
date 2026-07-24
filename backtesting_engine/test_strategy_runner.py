from backtesting_engine.strategy_runner import BacktestStrategyRunner


from confluence_engine.confluence import ICTConfluenceEngine


from adaptive_risk.adaptive_risk import AdaptiveRiskEngine




confluence = ICTConfluenceEngine()


risk = AdaptiveRiskEngine()



runner = BacktestStrategyRunner(

    confluence,

    risk

)



market_state={


"signals":{


"bias":25,

"liquidity":20,

"structure":20,

"order_block":15,

"fvg":10,

"session":5,

"risk":5

},



"regime":"TRENDING",


"drawdown":2,


"news":"ALLOW",


"direction":"BUY",


"entry":3300,


"stop_loss":3290,


"take_profit":3320

}



result = runner.analyze(
    market_state
)



print(result)