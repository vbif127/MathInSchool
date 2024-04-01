import os
from collections import OrderedDict
from pathlib import Path

import requests
from dotenv import dotenv_values

BASE_PATH = Path(os.path.dirname(__file__)) / ".."

env = dotenv_values(BASE_PATH / ".env")

ID = env.get("ID")
SERVER = env.get("SERVER")
TMP = env.get("TMP", os.getenv("TMP"))
SEPARATOR = env.get("SPLIT_PARAGRAPH_SYMBOL")
NOT_SELECTION_ITEM = "Not selection item"
NOT_SELECTION_BOOK = "Not selection book"

CONFIG = requests.get(f"{SERVER}/config").json(object_pairs_hook=OrderedDict)
