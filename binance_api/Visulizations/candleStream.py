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
# from ..utils.coinNamesList import get_coin_names_and_format,symbol_to_coin,get_symbol_base_asset_dict
import numpy as np
from .. import *
from datetime import datetime
from dash.dependencies import Input, Output

pp = pprint.PrettyPrinter(indent=4)
load_dotenv()

global df 
df = pd.DataFrame(columns = ['dateTime','open','high','low','close'])


api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)

options = get_symbol_base_asset_dict()
bm = BinanceSocketManager(client)




def get_process_message(coin):
    def process_message(msg):
        try:
            pp.pprint(msg)
            if msg['s'] == coin:
                df.append(client.get_server_time()['serverTime'],msg['o'],msg['h'],msg['l'],msg['c'])
                print(client.get_server_time()['serverTime'],msg['o'],msg['h'],msg['l'],msg['c'])
        except Exception:
            bm.close()
    return process_message

bm = BinanceSocketManager(client)
conn_key = bm.start_kline_socket('BNBBTC', get_process_message('BNBBTC'), interval=Client.KLINE_INTERVAL_30MINUTE)
bm.start()



app = dash.Dash(__name__)

interval = dcc.Interval(        # Update interval for grpah 
    id='interval-component',
    interval=5000, # in milliseconds
    n_intervals=0
)

app.layout = html.Div([
    html.H2("Choose a Crypo Symbol from below:"),
    dcc.Dropdown(
        id='my-dropdown',
        options=options,
        value='BNBBTC'
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input('my-dropdown', 'value')])

def display_candlestick(token_symbol='BNBBTC'):
    
    candles = client.get_recent_trades(symbol=token_symbol, interval=Client.KLINE_INTERVAL_1MINUTE)
    df = pd.DataFrame(candles, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
    df.dateTime = pd.to_datetime(df.dateTime, unit='ms')
    df.closeTime = pd.to_datetime(df.closeTime, unit='ms')
    data = [df['dateTime'],df['open'],df['high'],df['low'],df['close']]
    headers = ['dateTime','open','high','low','close']
    df = pd.concat(data, axis=1, keys=headers)
    
    fig = go.Figure(data=[go.Candlestick(
 
    x=df['dateTime'],
    open=df['open'], high=df['high'],
    low=df['low'], close=df['close'],
    increasing_line_color= 'cyan', decreasing_line_color= 'red'
    )])

    fig.update_layout(
        title=token_symbol,
        yaxis_title='Stock price',
        xaxis_rangeslider_visible=True
    )

    return fig

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_js:
    app.scripts.append_script({'external_url': js})


if __name__ == '__main__':
    app.run_server(debug=True,port=8051)



