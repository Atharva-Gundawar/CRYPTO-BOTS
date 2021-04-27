from binance.client import Client

get_depth = lambda client,token_symbol: client.get_order_book(symbol=token_symbol)
get_recent_trades = lambda client,token_symbol: client.get_recent_trades(symbol=token_symbol)
get_historical_trades = lambda client,token_symbol: client.get_historical_trades(symbol=token_symbol)
get_aggregate_trades = lambda client,token_symbol: client.get_aggregate_trades(symbol=token_symbol)
get_agg_trades = lambda client,token_symbol,start_str : client.aggregate_trade_iter(symbol=token_symbol, start_str=start_str) 

candles = lambda client,token_symbol,interval: client.get_klines(symbol=token_symbol, interval=Client.interval)
klines = lambda client,token_symbol,interval,start_str: client.get_historical_klines(token_symbol, Client.interval,start_str) 

