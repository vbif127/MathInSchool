import os

import requests

# Получение значения переменной окружения
ID = os.getenv("ID")
SERVER = os.getenv("SERVER")
BASE_PATH = os.getenv("BASE_PATH")
TMP = os.getenv("TMP")

CONFIG = requests.get(f"{SERVER}/config").json()
