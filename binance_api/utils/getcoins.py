from binance.client import Client
import os
from dotenv import load_dotenv
import pprint
import json

load_dotenv()

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
client = Client(api_key, api_secret)
coins = client.get_all_coins_info()
pp = pprint.PrettyPrinter(indent=4)
temp_dict = {}
# print(coins[0])
for i in coins:
    temp_dict[i['coin']] = i['name']
    if i['coin'] == 'BTC': 
        pp.pprint(i)
# pp.pprint(coins[0]) 
with open('coins_name.json', 'w') as fp:
    json.dump(temp_dict, fp)