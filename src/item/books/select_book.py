from PySide6.QtWidgets import QListWidgetItem

from src.item.books.content import BaseContentBuilder, ContentBuilder, NewContentBuilder
from src.support.errors import NotSelectionBookError
from src.item.books.type.type_abc import Book, TypesBooks
from src.settings import NOT_SELECTION_BOOK
from src.storage import GlobalStateStorage
from src.useui import Ui, UseUi


class HandleSelectionBook(UseUi):

    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        
        self.content_builder: ContentBuilder = None

    def handle_selection_book(self, item: QListWidgetItem) -> None:
        if item is None:
            return
        GlobalStateStorage.selection_book = item.data(0)
        self.set_content_builder()

        self.ui.stackedWidget_2.setCurrentIndex(1)

        self.set_book_info()

        self.ui.backPB.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))

        self.content_builder.build()
        self.ui.paragraphsPB.click()

    def set_content_builder(self) -> None:
        if GlobalStateStorage.selection_book.type_ == TypesBooks.BASE.value:
            self.content_builder = BaseContentBuilder(self.ui)
        elif GlobalStateStorage.selection_book.type_ == TypesBooks.NEW.value:
            self.content_builder = NewContentBuilder(self.ui)

    def set_book_info(self) -> None:
        if GlobalStateStorage.selection_book is None:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)

        self.ui.book_imgL.setStyleSheet(f"border-image: url({GlobalStateStorage.selection_book.image});")
        self.ui.book_description.setPlainText(GlobalStateStorage.selection_book.description)

    def connect(self) -> None:
        self.ui.list_booksLW.currentItemChanged.connect(
            self.handle_selection_book,
        )
