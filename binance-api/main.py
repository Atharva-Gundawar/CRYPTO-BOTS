from binance.client import Client
import plotly.graph_objects as go
import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dotenv import load_dotenv
import pprint

load_dotenv()

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)
coins = client.get_all_coins_info()
print(coins[0])
'''

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Checklist(
        id='toggle-rangeslider',
        options=[{'label': 'Include Rangeslider', 
                  'value': 'slider'}],
        value=['slider']
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Bitcoin', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("toggle-rangeslider", "value")])

def display_candlestick(value,token_symbol):
    candles = client.get_klines(symbol=token_symbol, interval=Client.KLINE_INTERVAL_1MINUTE)
    df = pd.DataFrame(candles, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
    df.dateTime = pd.to_datetime(df.dateTime, unit='ms')
    df.closeTime = pd.to_datetime(df.closeTime, unit='ms')
    
    fig = go.Figure(data=[go.Candlestick(
    title=token_symbol,
    yaxis_title='Stock price',
    x=df['dateTime'],
    open=df['open'], high=df['high'],
    low=df['low'], close=df['close'],
    increasing_line_color= 'cyan', decreasing_line_color= 'red'
    )])

    fig.update_layout(
        xaxis_rangeslider_visible='slider' in value
    )

    return fig

app.run_server(debug=True)

# def process_message(msg):
#     print("message type: {}".format(msg['e']))
#     print(msg)

# from binance.websockets import BinanceSocketManager
# bm = BinanceSocketManager(client)
# bm.start_aggtrade_socket('ETHBTC', process_message)
# bm.start()
'''