import os

import requests
from dotenv import dotenv_values

env = dotenv_values(".env")

ID = env.get("ID")
SERVER = env.get("SERVER")
BASE_PATH = os.path.join(os.path.dirname(__file__), "..")
TMP: str = env.get("TMP", os.getenv("TMP"))
SEPARATOR = env.get("SPLIT_PARAGRAPH_SYMBOL")
NOT_SELECTION_ITEM = "Not selection item"
NOT_SELECTION_BOOK = "Not selection book"

CONFIG = requests.get(f"{SERVER}/config").json()
