from core.logger import AgentLogger


class SetupValidator:

    def __init__(self):
        self.score = 0

    def evaluate(self, setup):

        score = 0

        # Bias
        if setup.get("bias") == "BULLISH":
            score += 20

        # Liquidity
        if setup.get("liquidity") == "SSL_SWEEP":
            score += 20

        # CHoCH
        if setup.get("choch") == "BULLISH":
            score += 20

        # FVG
        if setup.get("fvg"):
            score += 15

        # Order Block
        if setup.get("order_block"):
            score += 15

        # Premium / Discount
        if setup.get("zone") == "DISCOUNT":
            score += 10

        self.score = score

        AgentLogger.info(
            f"Setup Score: {score}"
        )

        return {
            "score": score,
            "valid": score >= 80
        }