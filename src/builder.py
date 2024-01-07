from src.item.books.content.select import HandlersContentSelectionConnector
from src.item.books.select_book import HandleSelectionBook
from src.item.books.shows import ShowBooks
from src.item.books.type import Book
from src.item.select_item import HandleSelectionItem
from src.storage.storage import StorageHistorySelection
from src.support.active.book import NotifierOfChangeSelectionBook
from src.support.active.item import NotifierOfChangeSelectionItem, SelectionItem
from src.useui import Ui, UseUi


class Builder(UseUi):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        self.selected_item: SelectionItem | None = None
        self.book: Book | None = None

        self.books: list[Book] = []

        self.storage = StorageHistorySelection()

        self.selected_item_notifier = NotifierOfChangeSelectionItem()
        self.selected_book_notifier = NotifierOfChangeSelectionBook()

        self.selected_item_notifier.set_values(item=self.selected_item, storage=self.storage)
        self.selected_book_notifier.set_values(book=self.book, storage=self.storage)

        self.show_books = ShowBooks(ui, self.selected_item,
                                    self.selected_item_notifier, self.books)

        self.handle_selection_item = HandleSelectionItem(
            ui,
            self.selected_item,
            self.selected_item_notifier,
        )
        self.handle_selection_book = HandleSelectionBook(
            self.ui,
            self.book,
            self.selected_book_notifier,
        )

        self.handlers_content_selection_connector = HandlersContentSelectionConnector(ui)

    def build(self) -> None:
        self.handle_selection_item.connect()
        self.handle_selection_book.connect()
        self.handlers_content_selection_connector.connect()
