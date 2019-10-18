import requests
from flask import Flask
from config.secret_token import TOKEN


"""TODO
1.прием сообщений
2.отсылка сообщений
"""



URL = f"https://api.telegram.org/bot{TOKEN}"

def main():
    r = requests.get(URL + 'getMe') #Добавляем метод getMe к api телеграма
    print (r.json())


if __name__ == '__main__':
   main()