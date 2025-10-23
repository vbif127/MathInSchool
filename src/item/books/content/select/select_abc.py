import os
import re
from abc import abstractmethod

from PySide6.QtWidgets import QCheckBox, QPushButton, QTreeWidgetItem

from src.api import Api
from src.settings import BASE_PATH, SEPARATOR
from src.support.other import get_random_string
from src.support.work_with_files import PathToFile
from src.useui import UseUi
from ui import Ui
from ui.choice_video_or_answer.choice import ChoiceAnswerWindow, ChoiceFileWindow, ChoiceVideoWindow


def separation_of_files_and_urls(scraped: list) -> tuple[list, list]:
    urls = [url for url in scraped if url.startswith("http")]
    files = [file for file in scraped if not file.startswith("http")]
    return files, urls


def split_by_separator(item: str) -> list:
    return item.split(SEPARATOR)


def adaptation_paragraph(paragraph: str) -> str:
    return re.sub(r"§\.?\.?", "P.", paragraph)


class HandlerContentSelection(UseUi):
    def __init__(self, ui: Ui, api: Api, cb_btn: QPushButton) -> None:
        super().__init__(ui)

        self.api = api
        self.cb_btn = cb_btn

    @abstractmethod
    def __call__(self, item: QTreeWidgetItem, column: int) -> None:
        ...

    def view(self, item: QTreeWidgetItem, urls: list[str], files: list[str], check_box: QCheckBox) -> None:
        self.view_video(item, urls, check_box)
        self.view_files(item, files)

    def view_files(self, item: QTreeWidgetItem, files: list[str], check_box: QCheckBox | None = None) -> None:
        if check_box is None:
            setattr(self, get_random_string(), ChoiceFileWindow(item.text(0), files))
            return

        if not check_box.isChecked():
            return

        setattr(self, get_random_string(), ChoiceAnswerWindow(item.text(0), files))

    def view_video(self, item: QTreeWidgetItem, urls: list[str], check_box: QCheckBox | None = None) -> None:
        if not urls and check_box is not None and check_box.isChecked():
            os.startfile(os.path.join(PathToFile(BASE_PATH).fullpath(), "assets\\no_video.png").replace("\\", "/"))
            return

        if not urls or check_box is None or not check_box.isChecked():
            return
        setattr(self, get_random_string(), ChoiceVideoWindow(item.text(0), urls))
