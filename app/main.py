import requests
import json
from flask import Flask
from secret_token import TOKEN


"""TODO
1.прием сообщений
2.отсылка сообщений
"""
URL = f"https://api.telegram.org/bot{TOKEN}/"


def write_json(data, filename = 'answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_updates():
    url = URL+'getUpdates'#Добавляем метод getUpdates что бы получить овтет от телеграма
    r = requests.get(url)
    #write_json (r.json())
    return r.json()
#getUpdates возвращает обновления для бота за последние 24 часа

def send_message(chat_id, text='bla-bla-bla'):
    url=URL+'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

def main():
    #r = requests.get(URL + 'getMe') #Добавляем метод getMe к api телеграма
    #write_json (r.json())
    r = get_updates()
    chat_id = r['result'][-1]['message']['chat']['id']
    print(chat_id)
    send_message(chat_id)

if __name__ == '__main__':
   main()