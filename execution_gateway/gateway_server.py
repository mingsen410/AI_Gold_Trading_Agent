from fastapi import FastAPI

from core.logger import AgentLogger

from mt5_bridge.bridge_service import MT5BridgeService



app = FastAPI(
    title="AI Trading Execution Gateway"
)



# ==========================
# Initialize MT5 Bridge
# ==========================

bridge = MT5BridgeService()

bridge.start()



# ==========================
# Health Check
# ==========================

@app.get("/")
def home():

    return {

        "status":
        "Gateway Online",

        "service":
        "AI Trading Execution Gateway"

    }



# ==========================
# Market Data
# ==========================

@app.get("/market/tick")
def get_tick():


    tick = bridge.market_data()


    AgentLogger.info(

        f"Market Tick: {tick}"

    )


    return tick





# ==========================
# Account Information
# ==========================

@app.get("/account")
def account_info():


    return {


        "balance":
        10000,


        "equity":
        10000,


        "currency":
        "USD"

    }





# ==========================
# Execute Order
# ==========================

@app.post("/trade/order")
def place_order(order: dict):


    AgentLogger.info(

        f"Order Received: {order}"

    )


    result = bridge.execute_order(

        order

    )


    return result





# ==========================
# Open Positions
# ==========================

@app.get("/positions")
def positions():


    return bridge.positions()