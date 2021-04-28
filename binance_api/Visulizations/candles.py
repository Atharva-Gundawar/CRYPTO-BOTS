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
load_dotenv()

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)
raw_server_time = client.get_server_time()['serverTime']
candles = client.get_klines(symbol="BNBBTC", interval=Client.KLINE_INTERVAL_1MINUTE)
print(candles[0])