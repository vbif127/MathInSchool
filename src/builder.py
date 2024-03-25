import os

from src.item.books.content.select import HandlersContentSelectionConnector
from src.item.books.select_book import HandleSelectionBook
from src.item.books.shows import ShowBooks
from src.item.select_item import HandleSelectionItem
from src.storage import GlobalStateStorage
from src.useui import Ui, UseUi


class Builder(UseUi):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        self.handle_selection_book: HandleSelectionBook | None = None
        self.handle_selection_item: HandleSelectionItem | None = None
        self.handlers_content_selection_connector: HandlersContentSelectionConnector | None = None

        self.show_books = ShowBooks(ui)
        self.ui.itemL.hide()
        self.ui.maxBT.hide()

        self.handlers_create()

    def handlers_create(self) -> None:
        self.handle_selection_item = HandleSelectionItem(
            self.ui, self.show_books
        )
        self.handle_selection_book = HandleSelectionBook(
            self.ui,
        )

        self.handlers_content_selection_connector = HandlersContentSelectionConnector(
            self.ui
        )

    def build(self) -> None:
        if self.handle_selection_item:
            self.handle_selection_item.connect()
        if self.handle_selection_book:
            self.handle_selection_book.connect()
        if self.handlers_content_selection_connector:
            self.handlers_content_selection_connector.connect()

    def __del__(self):
        for file in set(GlobalStateStorage.installed_files):
            os.remove(file)
