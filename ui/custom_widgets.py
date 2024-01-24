from PySide6.QtWidgets import QLabel, QPlainTextEdit, QVBoxLayout, QWidget

from src.api import Api
from src.item.books.type.type_abc import Book


class BookWidgetItem(QWidget):
    def __init__(self, book: Book) -> None:
        super().__init__()
        self.setMaximumWidth(200)
        self.setMaximumHeight(380)

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
        description_book.setPlainText(book.description)
        return description_book

    @staticmethod
    def _create_book_image_label() -> QLabel:
        book_image_label = QLabel()
        book_image_label.setMinimumHeight(230)
        return book_image_label

    def show_image(self) -> None:

        self.book_image_label.setStyleSheet(f"border-image: url('{self.book.image}');")
