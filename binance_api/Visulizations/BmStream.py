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
import pprint

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)
pp = pprint.PrettyPrinter(indent=4)


options = get_symbol_base_asset_dict()


bm = BinanceSocketManager(client)
def process_message(msg):
    if msg['e'] == 'error':
        # close and restart the socket
        bm.close()
        bm.start()
    elif msg['m'] == 'Max reconnect retries reached':
        # process message normally
        bm.close()
        sys.exit()
    else:
        print(chr(27) + "[2J") # Clears screen 
        pp.pprint(msg)
    print(msg)
    bm.close()
# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('BNBBTC', process_message)
bm.start()
# conn_key = bm.start_multiplex_socket(['bnbbtc@aggTrade', 'neobtc@ticker'], process_m_message)
# then start the socket manager
# bm.start()
