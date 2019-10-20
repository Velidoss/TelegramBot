from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
parameters = {
  'symbol':'BTC,USDT,BNB'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '53667124-103a-49e3-8a3c-359dcbd37bec',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)