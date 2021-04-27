from binance.client import Client
import plotly.graph_objects as go
import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)

def get_coin_names():
    ret_list = []
    with open('binance_api\coins_name.json', 'r') as fp:
        coin_names = json.load(fp)

    for coin in coin_names.keys(): 
        ret_list.append({'label': coin,'value': coin_names[coin]})
    return ret_list

def symbol_to_coin(symbol): 
    with open('binance_api\coins_name.json', 'r') as fp:
        coin_names = json.load(fp)
    return coin_names[symbol]