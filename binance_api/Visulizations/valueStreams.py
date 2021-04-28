from binance.websockets import BinanceSocketManager
from dotenv import load_dotenv
import os
from binance.client import Client
import pprint
from binance.client import Client
import plotly.graph_objects as go
import os,sys
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dotenv import load_dotenv
import json



pp = pprint.PrettyPrinter(indent=4)
load_dotenv()

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)

bm = BinanceSocketManager(client)

def process_message(msg):
    # if msg['e'] == 'error':
    #     # close and restart the socket
    #     bm.close()
    #     bm.start()
    # elif msg['m'] == 'Max reconnect retries reached':
    #     # process message normally
    #     bm.close()
    #     sys.exit()
    # else:
    #     print(chr(27) + "[2J") # Clears screen 
    #     pp.pprint(msg)
    print(msg)
    bm.close()
bm = BinanceSocketManager(client)
# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('BNBBTC', process_message)
bm.start()
# conn_key = bm.start_multiplex_socket(['bnbbtc@aggTrade', 'neobtc@ticker'], process_m_message)
# bm.start()
conn_key = bm.start_miniticker_socket(process_message)



# Example Payload for Kline
# {
#   "e": "kline",     // Event type
#   "E": 123456789,   // Event time
#   "s": "BNBBTC",    // Symbol
#   "k": {
#     "t": 123400000, // Kline start time
#     "T": 123460000, // Kline close time
#     "s": "BNBBTC",  // Symbol
#     "i": "1m",      // Interval
#     "f": 100,       // First trade ID
#     "L": 200,       // Last trade ID
#     "o": "0.0010",  // Open price
#     "c": "0.0020",  // Close price
#     "h": "0.0025",  // High price
#     "l": "0.0015",  // Low price
#     "v": "1000",    // Base asset volume
#     "n": 100,       // Number of trades
#     "x": false,     // Is this kline closed?
#     "q": "1.0000",  // Quote asset volume
#     "V": "500",     // Taker buy base asset volume
#     "Q": "0.500",   // Taker buy quote asset volume
#     "B": "123456"   // Ignore
#   }
# }

# Example Payload for Mini Ticker Stream
# {
#     "e": "24hrMiniTicker",  // Event type
#     "E": 123456789,         // Event time
#     "s": "BNBBTC",          // Symbol
#     "c": "0.0025",          // Close price
#     "o": "0.0010",          // Open price
#     "h": "0.0025",          // High price
#     "l": "0.0010",          // Low price
#     "v": "10000",           // Total traded base asset volume
#     "q": "18"               // Total traded quote asset volume
#   }