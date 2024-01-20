import re

from PySide6.QtWidgets import QTreeWidgetItem

from src.support.active.item import NotifierOfChangeSelectionItem, SelectionItem
from src.useui import Ui, UseUi


class NotSelectionItemError(Exception):
    pass


class HandleSelectionItem(UseUi):

    def __init__(self, ui: Ui, selection_item: SelectionItem | None,
                 notifier: NotifierOfChangeSelectionItem) -> None:
        super().__init__(ui)
        self.selection_item = selection_item
        self.notifier = notifier

        self.last_item: QTreeWidgetItem | None = None

    def handle_selection_item(self, item: QTreeWidgetItem) -> None:
        if self.last_item == item:
            return

        self.last_item = item

        if item.parent() is None or item.parent().parent() is None:
            return

        if not re.findall(r"\d*", item.parent().text(0)):
            return

        self.selection_item = self.make_active_item(item)

        self.notifier.change_item(self.selection_item)
        self.notifier.notify()

    @staticmethod
    def make_active_item(item: QTreeWidgetItem) -> SelectionItem:
        return SelectionItem(
            class_=re.findall(r"\d*", item.parent().parent().text(0))[0],
            text=item.parent().text(0),
            reinforce=bool(item.parent().indexOfChild(item)),
        )

    def connect(self) -> None:
        self.ui.treeWidget.itemClicked.connect(self.handle_selection_item)
