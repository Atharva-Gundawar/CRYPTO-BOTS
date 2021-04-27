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
from utils.coinNamesList import get_coin_names_and_format,symbol_to_coin

load_dotenv()

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)

with open('binance_api\coins_name.json', 'r') as fp:
    coin_names = json.load(fp)

options = get_coin_names_and_format()
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    # dcc.Checklist(
    #     id='toggle-rangeslider',
    #     options=[{'label': 'Include Rangeslider', 
    #               'value': 'slider'}],
    #     value=['slider']
    # ),
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
    # [Input("toggle-rangeslider", "value"),Input('my-dropdown', 'value')])

# def display_candlestick(n,value,token_symbol='BNBBTC'):
def display_candlestick(token_symbol='BNBBTC'):
    candles = client.get_klines(symbol='ETHBTC', interval=Client.KLINE_INTERVAL_1MINUTE)
    for i in candles:
        print(i)
        break
    # candles = client.get_klines(symbol=token_symbol, interval=Client.KLINE_INTERVAL_1MINUTE)
    print(token_symbol)
    df = pd.DataFrame(candles, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
    df.dateTime = pd.to_datetime(df.dateTime, unit='ms')
    df.closeTime = pd.to_datetime(df.closeTime, unit='ms')
    
    fig = go.Figure(data=[go.Candlestick(
    # title=symbol_to_coin(token_symbol),
    # title='Ye lo',
    # yaxis_title='Stock price',
    x=df['dateTime'],
    open=df['open'], high=df['high'],
    low=df['low'], close=df['close'],
    increasing_line_color= 'cyan', decreasing_line_color= 'red'
    )])

    fig.update_layout(
        xaxis_rangeslider_visible=True
    )

    return fig

app.run_server(debug=True,port=8051)

# def process_message(msg):
#     print("message type: {}".format(msg['e']))
#     print(msg)

# from binance.websockets import BinanceSocketManager
# bm = BinanceSocketManager(client)
# bm.start_aggtrade_socket('ETHBTC', process_message)
# bm.start()