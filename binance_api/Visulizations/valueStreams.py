from binance.websockets import BinanceSocketManager
from dotenv import load_dotenv
import os
from binance.client import Client
import pprint

pp = pprint.PrettyPrinter(indent=4)
load_dotenv()

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)


def process_message(msg):
    if msg['e'] == 'error':
        # close and restart the socket
        bm.close()
        bm.start()
    elif msg['m'] == 'Max reconnect retries reached':
        # process message normally
        bm.close()
        os.exit(0)
    else:
        print(chr(27) + "[2J") # Clears screen 
        pp.pprint(msg)

def process_m_message(msg):
    if msg['e'] == 'error':
        # close and restart the socket
        bm.close()
        bm.start()
    elif msg['m'] == 'Max reconnect retries reached':
        # process message normally
        bm.close()
        os.exit(0)
    else:
        print(chr(27) + "[2J") # Clears screen 
        pp.pprint(msg)
    # print("stream: {} data: {}".format(msg['stream'], msg['data']))

bm = BinanceSocketManager(client)
# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('BNBBTC', process_message)
bm.start()
# conn_key = bm.start_multiplex_socket(['bnbbtc@aggTrade', 'neobtc@ticker'], process_m_message)
# then start the socket manager
# bm.start()
