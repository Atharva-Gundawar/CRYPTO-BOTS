from binance.websockets import BinanceSocketManager
from dotenv import load_dotenv
import os
from binance.client import Client
import pprint
from binance.enums import *
pp = pprint.PrettyPrinter(indent=4)
load_dotenv()

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)


def process_message(msg):
    print(chr(27) + "[2J")
    pp.pprint(msg)

bm = BinanceSocketManager(client)
conn_key = bm.start_kline_socket('BNBBTC', process_message, interval=KLINE_INTERVAL_30MINUTE)
bm.start()
