import requests
import json
import re
from flask import Flask, request, jsonify #это не те реквесты что выше
from secret_token import TOKEN, CRYPTO_API_KEY


app = Flask(__name__)

URL = f"https://api.telegram.org/bot{TOKEN}/"


def write_json(data, filename = 'answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


#парсер текста
def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto[1:]



def get_price(crypto):
    
    parameters = {
        'start':'1',
        'limit':'1',
        'convert':f'{crypto}'
    }
    headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': f'{CRYPTO_API_KEY}'
}
    url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    r = requests.get(url, headers = headers, params=parameters).json() #при оборачивании в .json() объекст становится итерируемым, то есть можно обратиться по индексу и тд.
    price = r["data"][-1]["quote"][f"{crypto}"]["price"]
    return price


    #write_json(r.json(), filename='price.json')




def send_message(chat_id, text='bla-bla-bla'):
    url=URL+'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()




@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']#Обращаемся к ключу id
        message = r['message']['text']

        if 'bitcoin' in message:
            send_message(chat_id, text='очень дорогой')
       # write_json(r)
        return jsonify(r)
    
    return '<h1>Bot welcomes You!</h1>'



if __name__ == '__main__':
   #main()
   app.run()