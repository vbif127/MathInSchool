from PySide6.QtWidgets import QListWidgetItem

from src.item.books.type import Book
from src.item.select_item import NotSelectionItemError
from src.settings import CONFIG, NOT_SELECTION_ITEM
from src.support.active.item import (
    NotifierOfChangeSelectionItem,
    SelectionItem,
    WorkWithSelectionItem,
    add_observer_to_notifier_selection_item,
)
from src.support.other import Translate
from src.useui import Ui
from ui.custom_widgets import BookWidgetItem


@add_observer_to_notifier_selection_item
class ShowBooks(WorkWithSelectionItem):

    def __init__(self, ui: Ui, selection_item: SelectionItem | None, notifier: NotifierOfChangeSelectionItem,
                 books: list[Book]) -> None:
        super().__init__(ui)
        self.selection_item = selection_item
        self.notifier = notifier
        self.translator = Translate(CONFIG)
        self.books = books

    def get_books(self) -> list[Book]:
        if self.selection_item is None:
            raise NotSelectionItemError(NOT_SELECTION_ITEM)

        translate_item = self.translator.get_translate_item(self.selection_item.text)
        books: dict[str, dict] = CONFIG["classes"][f"{self.selection_item.class_}"][f"{translate_item}"]

        return list(filter(self.filter_books, map(self.map_book, books.items())))

    def map_book(self, book_tuple: tuple[str, dict]) -> Book:
        if self.selection_item is None:
            raise NotSelectionItemError(NOT_SELECTION_ITEM)
        books_ids = list(map(str, self.books))
        if book_tuple[0] in books_ids:
            return self.books[books_ids.index(book_tuple[0])]

        book = Book(
            self.selection_item,
            book_tuple[0],
            **book_tuple[1],
        )

        self.books.append(book)
        return book

    def filter_books(self, book: Book) -> bool:
        if self.selection_item is None:
            raise ValueError("Not selection item")
        return book.reinforce == self.selection_item.reinforce

    def show(self) -> None:
        self.ui.list_booksLW.clear()

        for book in self.get_books():
            book_widget = BookWidgetItem(book)
            book_widget.show_image()

            item = QListWidgetItem(self.ui.list_booksLW)
            item.setSizeHint(book_widget.sizeHint())
            item.setData(0, book)

            self.ui.list_booksLW.addItem(item)
            self.ui.list_booksLW.setItemWidget(item, book_widget)

    def update(self, item: SelectionItem) -> None:
        self.selection_item = item
        self.show()
