import os

import requests
from PySide6.QtWidgets import QLabel, QHBoxLayout, QWidget, QPlainTextEdit

from src.api import Api
from src.settings import SERVER, TMP, BASE_PATH
from src.support.work_with_files import PathToFile
from src.types import Book


class BookWidgetItem(QWidget):
    def __init__(self, book: Book) -> None:
        super().__init__()

        self.vbl = QHBoxLayout()
        self.book = book
        self.api = Api()

        self.book_image_label = self._create_book_image_label()

        self.description_book = self._create_description_book_widget(book)

        self.vbl.addWidget(self.book_image_label, 35)
        self.vbl.addWidget(self.description_book, 65)

        self.setLayout(self.vbl)

    @staticmethod
    def _create_description_book_widget(book: Book) -> QPlainTextEdit:
        description_book = QPlainTextEdit()
        description_book.setReadOnly(True)
        description_book.setPlainText(book.description)
        return description_book

    @staticmethod
    def _create_book_image_label() -> QLabel:
        book_image_label = QLabel()
        book_image_label.setMinimumHeight(230)
        return book_image_label

    def show_image(self) -> None:
        if self.book.image is None:
            path = PathToFile(self.book.image)
            req = self.api.get_file(path.path)
            print(req)
            # if req.status_code == 200:
            #     name = os.path.join(TMP, f'{id(path.path)}.{str(path).split(".")[-1]}').replace("\\", "/")
            #     if not os.path.exists(os.path.dirname(name)):
            #         os.makedirs(os.path.dirname(name))
            #     with open(name, "wb") as f:
            #         f.write(req.content)
            #     self.book.path = f"border-image: url({name});"
            #     self.book_image_label.setStyleSheet(f"border-image: url({name});")
            # else:
            #     self.book.path = f"border-image: url('{BASE_PATH}/img/default.png');".replace("\\", "/")
            #     self.book_image_label.setStyleSheet(
            #         f"border-image: url('{BASE_PATH}/img/default.png');".replace("\\", "/"))
        else:
            self.book_image_label.setStyleSheet(self.book.image)
