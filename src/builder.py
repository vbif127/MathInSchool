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
        self.handle_selection_book: HandleSelectionBook | None = None
        self.handle_selection_item: HandleSelectionItem | None = None
        self.handlers_content_selection_connector: HandlersContentSelectionConnector | None = None

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

        self.handlers_create()

    def handlers_create(self) -> None:
        self.handle_selection_item = HandleSelectionItem(
            self.ui,
            self.selected_item,
            self.selected_item_notifier,
        )
        self.handle_selection_book = HandleSelectionBook(
            self.ui,
            self.book,
            self.selected_book_notifier,
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
