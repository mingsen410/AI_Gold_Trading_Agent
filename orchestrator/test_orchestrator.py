from orchestrator.backtest_orchestrator import BacktestOrchestrator



class MockLoader:


    def load(self):

        return [

        {

        "time":"2016-01-01",

        "open":3300,

        "high":3310,

        "low":3290,

        "close":3305

        }

        ]




class MockQuality:


    def check_dataset(self,candles):

        return {


        "total":1,

        "valid":1

        }




class MockReplay:


    def __init__(self):

        self.done=False



    def has_next(self):

        return not self.done



    def next(self):

        self.done=True

        return {

        "close":3305

        }




engine = BacktestOrchestrator(

    MockLoader(),

    MockQuality(),

    MockReplay(),

    None,

    None,

    None,

    None

)



result = engine.run()


print(result)