from core.logger import AgentLogger


class MarketBiasEngine:

    def __init__(self):
        self.bias = "NEUTRAL"
        self.score = 50

    def calculate(
        self,
        structure,
        bos,
        choch
    ):

        score = 50

        if structure == "BULLISH":
            score += 20

        if bos:
            score += 15

        if choch == "BULLISH":
            score += 15

        if structure == "BEARISH":
            score -= 20

        if choch == "BEARISH":
            score -= 15

        self.score = max(0, min(score, 100))

        if self.score >= 65:
            self.bias = "BULLISH"

        elif self.score <= 35:
            self.bias = "BEARISH"

        else:
            self.bias = "NEUTRAL"

        AgentLogger.info(
            f"Market Bias: {self.bias} ({self.score})"
        )

        return {
            "bias": self.bias,
            "score": self.score
        }