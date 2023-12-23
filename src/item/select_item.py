import re

from PySide6.QtWidgets import QTreeWidgetItem

from src.support.active.item import SelectionItem, NotifierOfChangeSelectionItem
from src.useui import UseUi, Ui


class HandleSelection(UseUi):

    def __init__(self, ui: Ui, active_item: SelectionItem, notifier: NotifierOfChangeSelectionItem):
        super().__init__(ui)
        self.active_item: SelectionItem = active_item
        self.notifier = notifier

        self.last_item: QTreeWidgetItem = None

    def handle_selection_item(self, item: QTreeWidgetItem):
        if self.last_item == item:
            return

        self.last_item = item

        if item.parent() is None or item.parent().parent() is None:
            return

        if not re.findall(r"\d*", item.parent().text(0)):
            return

        self.active_item = self.make_active_item(item)

        self.notifier.change_item(self.active_item)
        self.notifier.notify()

    @staticmethod
    def make_active_item(item: QTreeWidgetItem) -> SelectionItem:
        return SelectionItem(
            class_=re.findall(r"\d*", item.parent().parent().text(0))[0],
            text=item.parent().text(0),
            reinforce=bool(item.parent().indexOfChild(item))
        )

    def connect(self):
        self.ui.treeWidget.itemClicked.connect(self.handle_selection_item)
