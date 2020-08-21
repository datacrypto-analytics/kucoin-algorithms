#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Felipe Soares

"""
import pandas as pd
from kucoin.client import Client


# SUA CHAVE API VAI AQUI
api_key = '@'
api_secret = '@'
api_passphrase = '@'

# SE NÃO FOR PELA API SANDBOX TIRAR O COMENTARIO ABAIXO

#client = Client(api_key, api_secret, api_passphrase)

# or connect to Sandbox
client = Client(api_key, api_secret, api_passphrase, sandbox=True)

# ESCOLHA DA CRIPTOMOEDA
criptomoeda = input('DataCrypto Analytics | OBS: Separe os pares pelo sinal (-) EXEMPLO: BTC-USDT' 
                    '\n\n Twitter @DataCryptoML'
                    '\n Github @datacryptoanalytics'
                    '\n \nDigite o par de criptomoedas listada na Binance:')

print('\nO par de criptomoeda informada foi: %s' 
      '\n\nDataCrypto Analytics esta buscando os valores,' 
      ' por favor aguarde alguns segundos!' %(criptomoeda))

# BUSCA OS VALORES NA EXCHANGE, CONFIGURADO PARA -- BTCUSDT
accounts = client.get_accounts()
currencies = client.get_currencies()
depth = client.get_order_book(criptomoeda)
klines = client.get_kline_data(criptomoeda)
stats = client.get_24hr_stats(criptomoeda)


conta = pd.DataFrame(accounts)

# DATAFRAME DA CRIPTOMOEDA
coins = pd.DataFrame(klines)
coins.head(15)
coins.describe()

# ---============
print(conta)
print(coins.head(15))
print()

print(client)




