from binance.client import Client
import plotly.graph_objects as go
import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html


api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
print(api_key)
client = Client(api_key, api_secret)
print(client.get_all_coins_info())
