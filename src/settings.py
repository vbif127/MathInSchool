import requests

from dotenv import dotenv_values

env = dotenv_values(".env")

ID = env.get("ID")
SERVER = env.get("SERVER")
BASE_PATH = env.get("BASE_PATH")
TMP = env.get("TMP")

CONFIG = requests.get(f"{SERVER}/config").json()
