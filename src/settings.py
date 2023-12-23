import os

import requests

from dotenv import dotenv_values

env = dotenv_values(".env")

ID = env.get("ID")
SERVER = env.get("SERVER")
BASE_PATH = os.path.join(os.path.dirname(__file__), "..")
TMP = env.get("TMP", os.getenv("TMP"))

CONFIG = requests.get(f"{SERVER}/config").json()
