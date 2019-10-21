import requests
from main import write_json
import re

#парсер текста
def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    print(crypto)



def get_price():
    
    parameters = {
        'start':'1',
        'limit':'1',
        'convert':'USD'
    }
    headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '53667124-103a-49e3-8a3c-359dcbd37bec',
}
    url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    r = requests.get(url, headers = headers, params=parameters).json() #при оборачивании в .json() объекст становится итерируемым, то есть можно обратиться по индексу и тд.
    price = r["data"][-1]["quote"]["USD"]["price"]
    return price
    #write_json(r.json(), filename='price.json')



def main():
    print(get_price())



if __name__ == '__main__':
    main()

