#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Felipe Soares

"""
import pandas as pd
from kucoin.client import Client

api_key = '@'
api_secret = '@'
api_passphrase = '@'

# or connect to Sandbox
client = Client(api_key, api_secret, api_passphrase, sandbox=True)

accounts = client.get_accounts()

currencies = client.get_currencies()

# get currencies
depth = client.get_order_book('BTC-USDT')

klines = client.get_kline_data('BTC-USDT')


df = pd.DataFrame(accounts)


print(df)

print(client)




