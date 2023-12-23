from abc import abstractmethod
from typing import Any

from src.useui import UseUi


class WorkWithAny(UseUi):
    @abstractmethod
    def update(self, item: Any) -> None:
        ...


class Notifier:
    __instance = None

    observers = []
    _item = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @abstractmethod
    def notify(self):
        for observer in self.observers:
            observer.update(self._item)

    @abstractmethod
    def add_observer(self, observer: WorkWithAny):
        self.observers.append(observer)

    @abstractmethod
    def change_item(self, item: Any):
        self._item = item
