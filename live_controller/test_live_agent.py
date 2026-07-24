from live_controller.live_agent import LiveTradingAgent

from mt5_connector.mt5_interface import MT5Connector



mt5 = MT5Connector()


mt5.connect()



agent = LiveTradingAgent(

    mt5,

    None

)



agent.run_cycle()