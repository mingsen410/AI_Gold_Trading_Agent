from paper_trading.paper_account import PaperAccount

from paper_trading.trade_journal import TradeJournal



account = PaperAccount()

journal = TradeJournal()



order={

"symbol":"XAUUSD",

"action":"BUY",

"entry":3350,

"volume":1,

"sl":3340,

"tp":3370

}



position = account.open_trade(order)


print("OPEN")

print(position.__dict__)




candle={

"open":3350,

"high":3375,

"low":3348,

"close":3365

}



account.update_candle(candle)



print("\nAFTER CANDLE")

print(position.__dict__)



journal.record(position)



print("\nJOURNAL")

print(journal.show())