import requests


data = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=BTC-ETH')
print(data.json())