from itertools import cycle

from PySide6.QtWidgets import QListWidgetItem

from src.settings import CONFIG
from src.support.other import Translate
from src.types import Book
from src.useui import Ui
from src.support.active import (WorkWithActiveItem, ActiveItem,
                                NotifierOfChangeActiveItem, add_observer_to_notifier)
from ui.custom_widgets import BookWidgetItem


@add_observer_to_notifier
class ShowBooks(WorkWithActiveItem):

    def __init__(self, ui: Ui, active_item: ActiveItem, notifier: NotifierOfChangeActiveItem):
        super().__init__(ui)
        self.active_item: ActiveItem = active_item
        self.notifier = notifier
        self.translator = Translate(CONFIG)
        self.books = None

    def generate(self):
        translate_item = self.translator.get_translate_item(self.active_item.text)
        books: dict[str, dict] = CONFIG["classes"][f"{self.active_item.class_}"][f"{translate_item}"]

        def map_book(book_tuple: tuple[str, dict]):
            book = Book(
                book_tuple[0],
                **book_tuple[1],
            )
            return book

        return list(filter(self.filter_books, map(map_book, books.items())))

    def filter_books(self, book: Book) -> bool:
        return book.reinforce == self.active_item.reinforce

    def show(self):
        self.books = self.generate()

        widgets = self.ui.columnLW1, self.ui.columnLW2, self.ui.columnLW3
        [column_widget.clear() for column_widget in widgets]

        for column_widget, book in zip(cycle(widgets), self.books):

            book_widget = BookWidgetItem(book)
            book_widget.show_image()
            item = QListWidgetItem(column_widget)
            item.setSizeHint(book_widget.sizeHint())

            column_widget.addItem(item)
            column_widget.setItemWidget(item, book_widget)

    def update(self, item: ActiveItem):
        self.active_item = item
        self.show()
