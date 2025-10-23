import os
import re
from abc import abstractmethod
from collections import namedtuple

from PySide6.QtWidgets import QListWidgetItem, QMainWindow, QMessageBox
from pytube import YouTube  # type: ignore

from src.api import Api
from src.storage import GlobalStateStorage
from src.support.other import web_view
from ui.choice_video_or_answer.choice_video_or_answer_ui import Ui_MainWindow

ItemData = namedtuple("ItemData", ["number", "file"])


def is_youtube_url(url: str) -> bool:
    """
    Check if the given URL is a YouTube URL.

    :param url: A string representing the URL to be checked.
    :type url: str
    :return: True if the URL is a YouTube URL, False otherwise.
    :rtype: bool
    """
    is_youtube = re.findall(r"youtube|youtu\.be", url)
    if is_youtube:
        return True
    return False


class ChoiceWindow(QMainWindow):
    def __init__(self, text: str, files: list[str]) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.api = Api()

        self.text = text
        self.files = files

        self.connect_()
        self.show()

    def show(self) -> None:
        super().show()
        self.ui.questionL.setText(self.text)
        self.setWindowTitle(self.text)
        self.add_files()

    @staticmethod
    @abstractmethod
    def build_item(data: ItemData) -> QListWidgetItem:
        ...

    def add_files(self) -> None:
        for item in map(self.build_item, enumerate(self.files, 1)):
            self.ui.fileLW.addItem(item)

    @abstractmethod
    def view(self, item: QListWidgetItem) -> None:
        ...

    def connect_(self) -> None:
        self.ui.fileLW.itemDoubleClicked.connect(self.view)


class ChoiceVideoWindow(ChoiceWindow):
    @staticmethod
    def build_item(data: ItemData) -> QListWidgetItem:
        item = QListWidgetItem()
        item.setData(1, {"url": data[1]})
        if is_youtube_url(data[1]):
            video_title = YouTube(data[1]).title
        else:
            video_title = ""
        item.setText(f"Видео {data[0]}. {video_title}")
        return item

    def view(self, item: QListWidgetItem) -> None:
        url: str = item.data(1).get("url")
        web_view(self, url)


class ChoiceFileWindow(ChoiceWindow):
    @staticmethod
    def build_item(data: ItemData) -> QListWidgetItem:
        item = QListWidgetItem()
        item.setData(1, {"file": data[1]})
        item.setData(3, [])
        item.setText(f"Файл {data[0]}")
        return item

    def view(self, item: QListWidgetItem) -> None:
        if not item.data(3):
            received_files = self.api.get_file(item.data(1).get("file"))
        else:
            received_files = item.data(3)

        if not received_files:
            QMessageBox.critical(None, "Error", "Файл не найден")
            self.close()
        for received_file in received_files:
            if not received_file:
                QMessageBox.critical(None, "Error", "Не получилось загрузить файл")
                continue
            if not item.data(3):
                item.setData(3, item.data(3) + [received_file])
            GlobalStateStorage.installed_files.append(received_file)
            os.startfile(received_file)


class ChoiceAnswerWindow(ChoiceFileWindow):
    @staticmethod
    def build_item(data: ItemData) -> QListWidgetItem:
        item = QListWidgetItem()
        item.setData(1, {"file": data[1]})
        item.setData(3, [])
        item.setText(f"Решение (ответ) {data[0]}")
        return item
