from agent_memory.memory import AgentMemory



memory = AgentMemory()



memory.add_trade(

{

"symbol":"XAUUSD",

"direction":"BUY",

"result":"+2R"

}

)



memory.add_session(

{

"date":"2026-07-24",

"market":"Bullish"

}

)



memory.update_performance(

{

"win_rate":70,

"profit_factor":2.1

}

)



print(
    memory.get_memory()
)