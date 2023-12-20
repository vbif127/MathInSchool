from abc import abstractmethod
from typing import Any

from pydantic import BaseModel

from src.storage.main import StorageActiveItem
from src.useui import UseUi, Ui


class ActiveItem(BaseModel):
    class_: int
    text: str
    reinforce: bool


class WorkWithAny(UseUi):
    @abstractmethod
    def update(self, item: Any) -> None:
        ...


class WorkWithActiveItem(WorkWithAny):
    def __init__(self, ui: Ui):
        super().__init__(ui)
        self.active_item: ActiveItem = None

    @abstractmethod
    def update(self, item: ActiveItem):
        self.change = False
        self.active_item = item


class Notifier:
    __instance = None

    observers = []
    _item = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def notify(self):
        for observer in self.observers:
            observer.update(self._item)

    def add_observer(self, observer):
        self.observers.append(observer)

    def change_item(self, item: Any):
        self._item = item


class NotifierOfChangeActiveItem(Notifier):
    __instance = None

    observers = []
    storage = None
    _item = None
    change: bool = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def set_values(self, *observers, storage: StorageActiveItem, item: ActiveItem):
        super().__init__(*observers, item=item)
        self.storage = storage
        self._item = item

    def notify(self):
        for observer in self.observers:
            if self.change:
                observer.update(self._item)

    def change_item(self, item: ActiveItem):
        self.change = True
        self._item = item
        self.storage.add_save(item)

    # TODO: 1. Сохранять старое состояние предмета(ActiveItem) в хранилище
    #       2. Придумать как восстановить(Достать из хранилища) старое состояние при возникновении ошибки
    #       3. Переименовать treeWidget
    #       4. Организовать появления учебников в списках
    #       5. Переделать виджет учебника сверху картинка снизу описание(название)
    #       6. Продумать систему выбора учебника и дальнейшей его обработки
    #       7. Подключить Git
    #       8. Подключить Ruff


def add_observer_to_notifier(cls):
    def _add_observer_to_notifier(*args, **kwargs):
        notifier = NotifierOfChangeActiveItem()
        cls_ = cls(*args, **kwargs)
        if not isinstance(cls_, WorkWithActiveItem):
            raise TypeError("The class must inherit from WorkWithActiveItem")
        notifier.add_observer(cls_)

        return cls_
    return _add_observer_to_notifier
