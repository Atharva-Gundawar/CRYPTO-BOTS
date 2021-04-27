from binance.client import Client
import plotly.graph_objects as go
import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dotenv import load_dotenv
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

load_dotenv()

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)

def get_coin_names_and_format():
    ret_list = []
    with open('binance_api\coins_name.json', 'r') as fp:
        coin_names = json.load(fp)

    for coin in coin_names.keys(): 
        ret_list.append({'label': coin,'value': coin_names[coin]})
    return ret_list

def get_coin_names():
    ret_dict = {}
    with open('binance_api\coins_name.json', 'r') as fp:
        coin_names = json.load(fp)

    for coin in coin_names.keys(): 
        ret_dict[coin] = coin_names[coin]
    return ret_dict

def symbol_to_coin(symbol): 
    with open('binance_api\coins_name.json', 'r') as fp:
        coin_names = json.load(fp)
    return coin_names[symbol]

def get_base_asset_symbol_dict(): 
    exchange_info = client.get_exchange_info()
    ret_list = {}
    for s in exchange_info['symbols']:
        if s['baseAsset'] not in ret_list.keys():
            ret_list[s['baseAsset']] = s['symbol']
    return ret_list

def get_symbol_base_asset_dict(): 
    exchange_info = client.get_exchange_info()
    ret_list = {}
    for s in exchange_info['symbols']:
        ret_list[s['symbol']] = s['baseAsset']
    ret_dict = []
    for coin in ret_list.keys(): 
        if coin == 'BTC':
            print(coin)
        ret_dict.append({'label': coin,'value': ret_list[coin]})
    return ret_dict
get_symbol_base_asset_dict()