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





def main():
    r = requests.get(URL + 'getMe') #Добавляем метод getMe к api телеграма
    write_json (r.json())


if __name__ == '__main__':
   main()