import re

from PySide6.QtWidgets import QTreeWidgetItem

from src.support.active import ActiveItem
from src.useui import UseUi, Ui


class HandleSelection(UseUi):

    def __init__(self, ui: Ui):
        super().__init__(ui)
        self.active_item: ActiveItem = None

    def __call__(self, item: QTreeWidgetItem):
        if item.parent() is None or item.parent().parent() is None:
            return

        if not re.findall(r"\d*", item.parent().text(0)):
            return

        self.active_item = self.make_active_item(item)
        self.change = True

    @staticmethod
    def make_active_item(item: QTreeWidgetItem) -> ActiveItem:
        return ActiveItem(
            class_=re.findall(r"\d*", item.parent().parent().text(0))[0],
            text=item.parent().text(0),
            reinforce=bool(item.parent().indexOfChild(item))
        )

    def connect(self):
        self.ui.z.itemClicked.connect(self.__call__)


class WorkWithActiveItem(UseUi):

    def __init__(self, ui: Ui):
        super().__init__(ui)
        self.selected_item: ActiveItem =

    def
