import requests

from src.settings import SERVER, ID, CONFIG
from src.support.active.item import SelectionItem
from src.support.other import Json, Translate
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

        self.translate = Translate(self.config)

    def get_file(self, path: str) -> list[str]:
        file_path = PathToFile(path)

        response = requests.get(
            f"{self.server}/file/{self.id}",
            json={"path": file_path.path},
        )
        response.raise_for_status()
        return install_and_extract_files(response)

    def get_json_book(self, active_item: SelectionItem, book_identifier: str, is_oge: bool = False) -> Json:

        translated_book_name, translated_item = self.get_translated(
            active_item,
            book_identifier,
        )
        queri_type = "OGE" if is_oge else f"{active_item.class_} class"

        response = requests.get(f"{SERVER}/json/{queri_type}/{translated_item}/{translated_book_name}")

        if response.status_code != 200:
            raise requests.HTTPError(response.text)

        return Json.loads(response.text)

    def get_translated(
            self, active_item: SelectionItem,
            book_identifier: str
    ) -> tuple[str, str]:

        translated_book_name = self.translate.get_translate_book(
            active_item.text,
            book_identifier,
            active_item.class_,
        )
        translated_subject = self.translate.get_translate_item(active_item.text)

        return translated_book_name, translated_subject
