"""module for parsing historical data from binance"""
import os
from binance.client import Client
from binance_data import DataClient
client = Client(api_key=os.getenv('API_PUB_BINANCE'), api_secret=os.getenv('API_SECRET_BINANCE'))

def pars_history(base_currencies,storage):
    futures = True
    clientt = DataClient(futures=futures)
    pair_list = clientt.get_binance_pairs(base_currencies=base_currencies)
    while int(client.response.headers['x-mbx-used-weight']) < 1200:
        store_data = clientt.kline_data(pair_list,'1m',storage=['csv',storage],progress_statements=True)

def limit():
    res = client.response.headers['x-mbx-used-weight']
    print(res)


#if __name__ == "__main__":
    #limit()
    #pars_history(BASE_CURRENCIES,STORAGE)
