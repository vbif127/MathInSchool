from abc import abstractmethod
from typing import Any

from src.useui import UseUi


class WorkWithAny(UseUi):
    @abstractmethod
    def update(self, item: Any) -> None:  # noqa: ANN401
        ...


class Notifier:
    __instance = None

    observers: list[WorkWithAny] = []
    _item = None

    def __new__(cls, *args, **kwargs):  # noqa: ANN204
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @abstractmethod
    def notify(self) -> None:
        for observer in self.observers:
            observer.update(self._item)  # type: ignore

    @abstractmethod
    def add_observer(self, observer: WorkWithAny) -> None:
        self.observers.append(observer)

    @abstractmethod
    def change_item(self, item: Any) -> None:  # noqa: ANN401
        self._item = item
