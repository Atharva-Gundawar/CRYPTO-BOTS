from binance.websockets import BinanceSocketManager
from dotenv import load_dotenv
import os
from binance.client import Client
import pprint
from binance.client import Client
import plotly.graph_objects as go
import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dotenv import load_dotenv
import json
from binance_api.utils.coinNamesList import get_coin_names_and_format,symbol_to_coin,get_symbol_base_asset_dict
import dash
import dash_html_components as html
import dash_core_components as dcc
import numpy as np
from datetime import datetime
from dash.dependencies import Input, Output

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)

options = get_symbol_base_asset_dict()
bm = BinanceSocketManager(client)

# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('BNBBTC', process_message)
bm.start()
# conn_key = bm.start_multiplex_socket(['bnbbtc@aggTrade', 'neobtc@ticker'], process_m_message)
# then start the socket manager
# bm.start()
