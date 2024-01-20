from PySide6.QtWidgets import QListWidgetItem

from src.item.books.content import ContentBuilder
from src.item.books.type import Book, NotSelectionBookError
from src.settings import NOT_SELECTION_BOOK
from src.support.active.book import NotifierOfChangeSelectionBook
from src.useui import Ui, UseUi


class HandleSelectionBook(UseUi):

    def __init__(self, ui: Ui, book: Book | None, notifier: NotifierOfChangeSelectionBook) -> None:
        super().__init__(ui)
        self.notifier = notifier
        self.book = book
        self.content_builder = ContentBuilder(ui)

    def handle_selection_book(self, item: QListWidgetItem) -> None:
        if item is None:
            return
        self.book: Book = item.data(0)
        self.ui.stackedWidget_2.setCurrentIndex(1)

        self.set_book_info()

        self.ui.backPB.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))

        self.notifier.change_item(self.book)
        self.notifier.notify()

        self.content_builder.build()
        self.ui.paragraphsPB.click()

    def set_book_info(self) -> None:
        if self.book is None:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)

        self.ui.book_imgL.setStyleSheet(f"border-image: url({self.book.image});")
        self.ui.book_description.setPlainText(self.book.description)

    def connect(self) -> None:
        self.ui.list_booksLW.currentItemChanged.connect(
            self.handle_selection_book
        )
