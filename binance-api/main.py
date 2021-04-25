from binance.client import Client
# from dotenv import load_dotenv
import os
api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

prices = client.get_all_tickers()
# print(prices)
# for i in prices:
#     print(i['symbol'],"=>",i['price'])
# withdraw 100 ETH
# check docs for assumptions around withdrawals
def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)

from binance.websockets import BinanceSocketManager
bm = BinanceSocketManager(client)
bm.start_aggtrade_socket('ETHBTC', process_message)
bm.start()