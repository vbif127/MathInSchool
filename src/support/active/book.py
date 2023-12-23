from src.item.books.type import Book
from src.storage.rollback import RollBackSelectionBook
from src.storage.save import SaveHistorySelection
from src.storage.storage import StorageHistorySelection
from src.types import EventsTypes
from src.useui import Ui

from src.support.active.base import WorkWithAny, Notifier


class WorkWithSelectionBook(WorkWithAny):
    def __init__(self, ui: Ui, notifier: Notifier):
        super().__init__(ui)
        self.notifier = notifier
        self.book = None

    def update(self, book: Book) -> None:
        self.book = book


class NotifierOfChangeSelectionBook(Notifier):
    __instance = None

    observers = []
    storage = None
    _book = None
    change: bool = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def set_values(self, *observers, storage: StorageHistorySelection, book: Book):
        super().__init__(*observers, item=book)
        self.storage = storage
        self._book = book

    def add_observer(self, observer: WorkWithSelectionBook):
        if not isinstance(observer, WorkWithSelectionBook):
            raise TypeError("The class must inherit from WorkWithSelectionItem")
        self.observers.append(observer)

    def notify(self):
        if self.change:
            self.storage.add_save(SaveHistorySelection(
                change_type=EventsTypes.SELECT_BOOK,
                roll_back_event=RollBackSelectionBook(),
                date={}
            ))

    def change_item(self, item: Book):
        self._book = item
        self.change = True
