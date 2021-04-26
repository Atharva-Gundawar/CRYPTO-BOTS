import binance

getPing = lambda client : client.ping()
get_server_time = lambda client : client.get_server_time()
get_exchange_info = lambda client : client.get_exchange_info()
get_symbol_info = lambda client,symbol : client.get_symbol_info(symbol)
get_all_tickers = lambda client : client.get_all_tickers()
get_account_snapshot = lambda client,sanp_type : client.get_account_snapshot(type=sanp_type)   #  SPOT/MARGIN/FUTURES
get_products = lambda client : client.get_products()