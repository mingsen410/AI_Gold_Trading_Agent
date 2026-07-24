from core.logger import AgentLogger



class ICTStrategyEngine:



    def __init__(
        self,
        bias_engine,
        setup_validator,
        confidence_engine,
        session_engine
    ):

        self.bias_engine = bias_engine
        self.setup_validator = setup_validator
        self.confidence_engine = confidence_engine
        self.session_engine = session_engine




    def analyze(
        self,
        market_data
    ):


        session = self.session_engine.get_session(
            market_data["time"]
        )



        bias = self.bias_engine.calculate(

            market_data["structure"],

            market_data["bos"],

            market_data["choch"]

        )



        setup = {


            "bias":

            bias["bias"],


            "liquidity":

            market_data["liquidity"],


            "choch":

            market_data["choch"],


            "fvg":

            market_data["fvg"],


            "order_block":

            market_data["order_block"],


            "zone":

            market_data["zone"]

        }



        validation = self.setup_validator.evaluate(
            setup
        )



        confidence = self.confidence_engine.calculate(

            {

            "setup_score":
            validation["score"],


            "session":
            session,


            "liquidity":
            market_data["liquidity"],


            "volatility":
            market_data["volatility"]

            }

        )



        result = {


            "session":

            session,


            "bias":

            bias,


            "setup":

            validation,


            "confidence":

            confidence

        }



        AgentLogger.info(
            "ICT Strategy Analysis Completed"
        )


        return result