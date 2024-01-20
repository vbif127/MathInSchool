import os
from abc import abstractmethod
from collections import namedtuple
from tkinter import messagebox

from PySide6.QtWidgets import QListWidgetItem, QMainWindow

from src.api import Api
from src.support.other import web_view
from ui.choice_video_or_answer.choice_video_or_answer_ui import Ui_MainWindow

ItemData = namedtuple("ItemData", ["number", "file"])


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
        self.ui.fileLW.itemClicked.connect(self.view)


class ChoiceVideoWindow(ChoiceWindow):

    @staticmethod
    def build_item(data: ItemData) -> QListWidgetItem:
        item = QListWidgetItem()
        item.setData(1, {"file": data[1]})
        item.setText(f"Видео {data[0]}")
        return item

    def view(self, item: QListWidgetItem) -> None:
        url: str = item.data(1).get("file")
        web_view(self, url)


class ChoiceFileWindow(ChoiceWindow):

    @staticmethod
    def build_item(data: ItemData) -> QListWidgetItem:
        item = QListWidgetItem()
        item.setData(1, {"file": data[1]})
        item.setText(f"Файл {data[0]}")
        return item

    def view(self, item: QListWidgetItem) -> None:
        for received_file in self.api.get_file(item.data(1).get("file")):
            if not received_file:
                messagebox.showerror("Error", "Не получилось загрузить файл")
                continue

            os.startfile(received_file)


class ChoiceAnswerWindow(ChoiceFileWindow):

    @staticmethod
    def build_item(data: ItemData) -> QListWidgetItem:
        item = QListWidgetItem()
        item.setData(1, {"file": data[1]})
        item.setText(f"Ответ(Решение) {data[0]}")
        return item
