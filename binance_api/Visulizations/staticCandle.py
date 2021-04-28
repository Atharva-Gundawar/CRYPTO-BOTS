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

load_dotenv()

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)

options = get_symbol_base_asset_dict()
app = dash.Dash(__name__)

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
    candles = client.get_klines(symbol=token_symbol, interval=Client.KLINE_INTERVAL_1MINUTE)
    print(token_symbol)
    print(token_symbol)
    df = pd.DataFrame(candles, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
    df.dateTime = pd.to_datetime(df.dateTime, unit='ms')
    df.closeTime = pd.to_datetime(df.closeTime, unit='ms')
    
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


if __name__ == '__main__':
    app.run_server(debug=True,port=8051)