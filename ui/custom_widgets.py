import os

import requests
from PySide6.QtWidgets import QLabel, QWidget, QPlainTextEdit, QVBoxLayout

from src.api import Api
from src.settings import BASE_PATH
from src.support.work_with_files import PathToFile
from src.item.books.type import Book


class BookWidgetItem(QWidget):
    def __init__(self, book: Book) -> None:
        super().__init__()
        self.setMaximumWidth(230)

        self.vbl = QVBoxLayout()
        self.book = book
        self.api = Api()

        self.book_image_label = self._create_book_image_label()

        self.description_book = self._create_description_book_widget(book)

        self.vbl.addWidget(self.book_image_label, 60)
        self.vbl.addWidget(self.description_book, 40)

        self.setLayout(self.vbl)

    @staticmethod
    def _create_description_book_widget(book: Book) -> QPlainTextEdit:
        description_book = QPlainTextEdit()
        description_book.setReadOnly(True)
        description_book.setPlainText(book.description.replace("\n\n", "\n"))
        return description_book

    @staticmethod
    def _create_book_image_label() -> QLabel:
        book_image_label = QLabel()
        book_image_label.setMinimumHeight(230)
        return book_image_label

    def show_image(self) -> None:
        if self.book.image is not None:
            path = PathToFile(self.book.image)

            try:
                file = self.api.get_file(path.path)[0].replace("\\", "/")

            except requests.HTTPError:
                default_img = (os.path.join(PathToFile(BASE_PATH).fullpath(), 'default.png')
                               .replace("\\", "/"))
                self.book_image_label.setStyleSheet(f"border-image: url('{default_img}');")

                return

            self.book_image_label.setStyleSheet(f"border-image: url({file});")
        else:
            self.book_image_label.setStyleSheet(self.book.image)
