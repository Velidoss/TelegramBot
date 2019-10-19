import requests
import json
from flask import Flask, request, jsonify #это не те реквесты что выше
from secret_token import TOKEN, COIN_API


app = Flask(__name__)

URL = f"https://api.telegram.org/bot{TOKEN}/"


def write_json(data, filename = 'answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_price():
    url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin'
    r = requests.get(url)
    write_json(r.json(), filename='price.json')


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