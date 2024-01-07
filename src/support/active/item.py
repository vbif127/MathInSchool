from abc import abstractmethod

from pydantic import BaseModel

from src.storage.rollback import RollBackSelectItem
from src.storage.save import SaveHistorySelection
from src.storage.storage import StorageHistorySelection
from src.support.active.base import Notifier, WorkWithAny
from src.types import EventsTypes
from src.useui import Ui


class SelectionItem(BaseModel):
    class_: int
    text: str
    reinforce: bool


class WorkWithSelectionItem(WorkWithAny):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        self.selection_item: SelectionItem | None = None

    @abstractmethod
    def update(self, item: SelectionItem) -> None:
        self.selection_item = item


class NotifierOfChangeSelectionItem(Notifier):
    __instance = None

    observers = []
    storage = None
    _item = None
    change: bool = False

    def __new__(cls, *args, **kwargs):  # noqa: ANN204
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add_observer(self, observer: WorkWithSelectionItem) -> None:  # type: ignore
        if not isinstance(observer, WorkWithSelectionItem):
            raise TypeError("The class must inherit from WorkWithSelectionItem")
        self.observers.append(observer)

    def set_values(self, *observers, storage: StorageHistorySelection, item: SelectionItem | None) -> None:
        self.observers = list(observers)
        self.storage = storage
        self._item = item

    def notify(self) -> None:
        for observer in self.observers:
            if self.change:
                observer.update(self._item)
            # TODO: Доделать систему сохранения истории состояний

    def change_item(self, item: SelectionItem) -> None:
        super().change_item(item)
        self.change = True
        self.storage.add_save(SaveHistorySelection(
            change_type=EventsTypes.SELECT_ITEM,
            roll_back_event=RollBackSelectItem(),
            date={},
        ))
    # TODO: 1. Сохранять старое состояние предмета(SelectionItem) в хранилище
    #       2. Придумать как восстановить(Достать из хранилища) старое состояние при возникновении ошибки
    #       3. Переименовать treeWidget
    #       4. Организовать появления учебников в списках
    #       5. Переделать виджет учебника сверху картинка снизу описание(название)
    #       6. Продумать систему выбора учебника и дальнейшей его обработки
    #       7. Подключить Git
    #       8. Подключить Ruff


def add_observer_to_notifier_selection_item(cls):  # noqa: ANN001, ANN201
    def _add_observer_to_notifier_selection_item(*args, **kwargs) -> WorkWithSelectionItem:
        notifier = NotifierOfChangeSelectionItem()
        cls_ = cls(*args, **kwargs)
        if not isinstance(cls_, WorkWithSelectionItem):
            raise TypeError("The class must inherit from WorkWithSelectionItem")
        notifier.add_observer(cls_)

        return cls_

    return _add_observer_to_notifier_selection_item
