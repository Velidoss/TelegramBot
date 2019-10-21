import requests
from main import write_json
import re



def get_price():
    key = '53667124-103a-49e3-8a3c-359dcbd37bec'
    parameters = {
        'symbol':'BTC'
    }
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map?CMC_PRO_API_KEY={key}'
    r = requests.get(url, params=parameters).json()
    slug = r["data"][-1]["slug"]
    return slug
    #write_json(r.json(), filename='price.json')

print(get_price())

def main():
    pass



if __name__ == '__main__':
    main()

