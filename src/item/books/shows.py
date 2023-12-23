from PySide6.QtWidgets import QListWidgetItem

from src.settings import CONFIG
from src.support.other import Translate
from src.item.books.type import Book
from src.useui import Ui
from src.support.active.item import (WorkWithSelectionItem, SelectionItem,
                                     NotifierOfChangeSelectionItem,
                                     add_observer_to_notifier_active_item)
from ui.custom_widgets import BookWidgetItem


@add_observer_to_notifier_active_item
class ShowBooks(WorkWithSelectionItem):

    def __init__(self, ui: Ui, active_item: SelectionItem, notifier: NotifierOfChangeSelectionItem):
        super().__init__(ui)
        self.active_item: SelectionItem = active_item
        self.notifier = notifier
        self.translator = Translate(CONFIG)
        self.books = None

    def generate(self):
        translate_item = self.translator.get_translate_item(self.active_item.text)
        books: dict[str, dict] = CONFIG["classes"][f"{self.active_item.class_}"][f"{translate_item}"]

        def map_book(book_tuple: tuple[str, dict]):
            book = Book(
                self.active_item,
                book_tuple[0],
                **book_tuple[1],
            )
            return book

        return list(filter(self.filter_books, map(map_book, books.items())))

    def filter_books(self, book: Book) -> bool:
        return book.reinforce == self.active_item.reinforce

    def show(self):
        self.books = self.generate()

        for book in self.books:
            book_widget = BookWidgetItem(book)
            book_widget.show_image()
            item = QListWidgetItem(self.ui.list_booksLW)
            item.setSizeHint(book_widget.sizeHint())

            self.ui.list_booksLW.addItem(item)
            self.ui.list_booksLW.setItemWidget(item, book_widget)

    def update(self, item: SelectionItem):
        self.active_item = item
        self.show()
