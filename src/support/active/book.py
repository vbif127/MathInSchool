from src.item.books.type import Book
from src.storage.rollback import RollBackSelectionBook
from src.storage.save import SaveHistorySelection
from src.storage.storage import StorageHistorySelection
from src.support.active.base import WorkWithAny
from src.types import EventsTypes
from src.useui import Ui


class WorkWithSelectionBook(WorkWithAny):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        self.book: Book | None = None

    def update(self, book: Book) -> None:
        self.book = book


class NotifierOfChangeSelectionBook:
    __instance = None

    observers: list[WorkWithSelectionBook] = []
    storage: StorageHistorySelection | None = None
    _book: Book | None = None
    change: bool = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def set_values(self, *observers, storage: StorageHistorySelection, book: Book | None) -> None:
        self.observers = list(observers)
        self.storage = storage
        self._book = book

    def add_observer(self, observer: WorkWithSelectionBook) -> None:
        if not isinstance(observer, WorkWithSelectionBook):
            raise TypeError("The class must inherit from WorkWithSelectionItem")
        self.observers.append(observer)

    def notify(self) -> None:
        if self.storage is None:
            raise ValueError("Storage is not set")

        for observer in self.observers:
            if self._book is None:
                return
            if self.change:
                self.storage.add_save(SaveHistorySelection(
                    change_type=EventsTypes.SELECT_BOOK,
                    roll_back_event=RollBackSelectionBook(),
                    date={},
                ))
                observer.update(self._book)

    def change_item(self, item: Book) -> None:
        self._book = item
        self.change = True


def add_observer_to_notifier_selection_book(cls):  # noqa: ANN001, ANN201
    def _add_observer_to_notifier_selection_book(*args, **kwargs) -> WorkWithSelectionBook:
        notifier = NotifierOfChangeSelectionBook()
        cls_ = cls(*args, **kwargs)
        if not isinstance(cls_, WorkWithSelectionBook):
            raise TypeError("The class must inherit from WorkWithSelectionItem")
        notifier.add_observer(cls_)

        return cls_

    return _add_observer_to_notifier_selection_book
