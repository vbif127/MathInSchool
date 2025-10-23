import time
from decimal import Decimal
from threading import Thread

from PySide6.QtWidgets import QListWidgetItem

from src.item.books.type.type_abc import Book
from src.item.books.type.type_base import BaseBook
from src.item.books.type.type_new import NewBook
from src.settings import CONFIG, NOT_SELECTION_ITEM
from src.storage import GlobalStateStorage
from src.support.errors import NotSelectionItemError
from src.support.other import Translate
from src.useui import Ui, UseUi
from ui.custom_widgets import BookWidgetItem


class ShowBooks(UseUi):

    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        self.translator = Translate(CONFIG)

    def get_books(self) -> list[Book]:
        if GlobalStateStorage.selection_item is None:
            raise NotSelectionItemError(NOT_SELECTION_ITEM)

        translate_item = self.translator.get_translate_item(GlobalStateStorage.selection_item.item)

        books: dict[str, dict] = CONFIG[GlobalStateStorage.selection_item.root_dir_json] \
            [f"{GlobalStateStorage.selection_item.folder}"][f"{translate_item}"]

        return list(filter(self.filter_books, map(self.map_book, books.items())))

    @staticmethod
    def map_book(book_tuple: tuple[str, dict]) -> Book:
        if GlobalStateStorage.selection_item is None:
            raise NotSelectionItemError(NOT_SELECTION_ITEM)
        books_ids = list(map(str, GlobalStateStorage.books))

        if book_tuple[0] in books_ids:
            return GlobalStateStorage.books[books_ids.index(book_tuple[0])]

        if book_tuple[1].get("type_") == "new":
            book = NewBook(
                GlobalStateStorage.selection_item,
                book_tuple[0],
                **book_tuple[1],
            )
        else:
            book = BaseBook(
                GlobalStateStorage.selection_item,
                book_tuple[0],
                **book_tuple[1],
            )

        GlobalStateStorage.books.append(book)
        return book

    @staticmethod
    def filter_books(book: Book) -> bool:
        if GlobalStateStorage.selection_item is None:
            raise ValueError("Not selection item")
        if GlobalStateStorage.selection_item.filter_tags is None:
            return True
        return book.tags == GlobalStateStorage.selection_item.filter_tags

    def show(self) -> None:
        self.ui.list_booksLW.clear()
        ths = []

        for book in self.get_books():
            book_widget = BookWidgetItem(book)
            if not book.image.is_installed():
                th = Thread(target=book_widget.show_image)
                ths.append(th)
            else:
                book_widget.show_image()
            item = QListWidgetItem(self.ui.list_booksLW)

            item.setSizeHint(book_widget.sizeHint())
            item.setData(0, book)

            self.ui.list_booksLW.addItem(item)
            self.ui.list_booksLW.setItemWidget(item, book_widget)

        for th in ths:
            th.start()
            # print(len(ths)*Decimal(0.013) < 0.1)
            if len(ths)*Decimal(0.02) < 0.15:
                time.sleep(0.15)
            else:
                time.sleep(float(len(ths)*Decimal(0.02)))
