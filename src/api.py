import requests

from src.settings import SERVER, ID, CONFIG
from src.support.work_with_files import PathToFile, install_and_extract_files


class Api:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.server = SERVER
        self.config = CONFIG
        self.id = ID

    def get_file(self, path: str) -> list[str]:
        file_path = PathToFile(path)

        response = requests.get(
            f"{self.server}/file/{self.id}",
            json={"path": file_path.path},
        )
        response.raise_for_status()
        return install_and_extract_files(response)

    def get_json(self):
        # TODO: implement
        ...
