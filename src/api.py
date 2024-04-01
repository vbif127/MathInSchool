import requests

from src.settings import CONFIG, ID, SERVER
from src.support.active import SelectionItem
from src.support.other import Json, Translate
from src.support.work_with_files import PathToFile, install_and_extract_files


class Api:
    __instance = None

    def __new__(cls, *args, **kwargs):  # noqa: ANN204
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self.server = SERVER
        self.config = CONFIG
        self.id = ID

        self.translate = Translate(self.config)

    def get_file(self, path: str) -> list[str] | list:
        file_path = PathToFile(path)

        response = requests.get(
            f"{self.server}/file/{self.id}",
            json={"path": file_path.path.replace("\\", "/")},
        )
        try:
            response.raise_for_status()
        except requests.HTTPError:
            return []

        return install_and_extract_files(response)

    def get_json_book(self, active_item: SelectionItem, book_identifier: str, is_oge: bool = False) -> dict:
        print(active_item)
        translated_book_name, translated_item = self.get_translated(
            active_item,
            book_identifier,
        )
        queri_type = "OGE" if is_oge else f"{active_item.class_} class"

        response = requests.get(f"{SERVER}/json/{queri_type}/{translated_item}/{translated_book_name}")

        if response.status_code != 200:
            raise requests.HTTPError(response.text)

        return Json().loads(response.text)

    def get_translated(
            self, selection_item: SelectionItem,
            book_identifier: str,
    ) -> tuple[str, str]:

        translated_book_name = self.translate.get_translate_book(
            selection_item.text,
            book_identifier,
            selection_item.class_,
        )
        translated_subject = self.translate.get_translate_item(selection_item.text)

        return translated_book_name, translated_subject
