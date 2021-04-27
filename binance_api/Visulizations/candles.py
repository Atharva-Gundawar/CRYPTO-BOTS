from utils import marketData

def show_candles(client,token_symbol,interval): 
    return marketData.candles(client,token_symbol,interval)