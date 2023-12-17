from abc import abstractmethod
from typing import Any

from pydantic import BaseModel

from src.useui import UseUi, Ui


class ActiveItem(BaseModel):
    class_: int
    text: str
    reinforce: bool


class WorkWithAny(UseUi):
    @abstractmethod
    def update(self, item: Any) -> None:
        ...


class WorkWithActive(WorkWithAny):
    def __init__(self, ui: Ui):
        super().__init__(ui)
        self.change: bool = False
        self.active_item: ActiveItem = None

    @abstractmethod
    def update(self, item: ActiveItem):
        self.change = False
        self.active_item = item


class Notifier:
    def __init__(self, *observers):
        self.observers = list(observers)

    def notify(self, item: Any):
        for observer in self.observers:
            observer.update(item)

    def add_observer(self, observer):
        self.observers.append(observer)


class NotifierOfChangeActiveItem(Notifier):
    def __init__(self, *observers):
        super().__init__(*observers)

    def notify(self, item: ActiveItem):
        for observer in self.observers:
            if observer.change:
                observer.update(item)
    # TODO: 1. Сохранять старое состояние предмета(ActiveItem) в хранилище
    #       2. Придумать как восстановить(Достать из хранилища) старое состояние при возникновении ошибки
    #       3. Переименовать treeWidget
    #       4. Организовать появления учебников в списках
    #       5. Переделать виджет учебника сверху картинка снизу описание(название)
    #       6. Продумать систему выбора учебника и дальнейшей его обработки
    #       7. Подключить Git
    #       8. Подключить Ruff

