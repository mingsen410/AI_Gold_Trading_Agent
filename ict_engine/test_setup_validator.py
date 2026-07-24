from ict_engine.setup_validator import SetupValidator

validator = SetupValidator()

setup = {
    "bias": "BULLISH",
    "liquidity": "SSL_SWEEP",
    "choch": "BULLISH",
    "fvg": True,
    "order_block": True,
    "zone": "DISCOUNT"
}

result = validator.evaluate(setup)

print(result)