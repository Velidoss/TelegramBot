from flask import Flask
from config.secret_token import TOKEN

"""TODO
1.прием сообщений
2.отсылка сообщений
"""



URL = f"https://api.telegram.org/bot{TOKEN}"

#app = Flask(__name__)


if __name__ == '__main__':
   main()