from analytics_backend.dashboard_data import DashboardDataProvider



dashboard = DashboardDataProvider()



dashboard.update_status(
    "RUNNING"
)



dashboard.update_account(

{

"balance":10000,

"equity":10200

}

)



dashboard.update_performance(

{

"win_rate":70,

"profit_factor":2.1,

"total_R":150

}

)



dashboard.update_positions(

[

{

"symbol":"XAUUSD",

"direction":"BUY"

}

]

)



print(

dashboard.get_dashboard_data()

)