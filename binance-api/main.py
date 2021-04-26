from binance.client import Client
# import plotly.graph_objects as go
import os
import pandas as pd

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)

# candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
# for _ in candles:
#     print(_)

for kline in client.get_historical_klines_generator("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC"):
    print(kline)



# get market depth
# depth = client.get_order_book(symbol='BNBBTC')

# prices = client.get_all_tickers()
# print(prices)
# for i in prices:
#     print(i['symbol'],"=>",i['price'])
# withdraw 100 ETH
# check docs for assumptions around withdrawals
# def process_message(msg):
#     print("message type: {}".format(msg['e']))
#     print(msg)

# from binance.websockets import BinanceSocketManager
# bm = BinanceSocketManager(client)
# bm.start_aggtrade_socket('ETHBTC', process_message)
# bm.start()