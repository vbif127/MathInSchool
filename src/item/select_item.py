import re

from PySide6.QtWidgets import QTreeWidgetItem

from src.item.books.shows import ShowBooks
from src.storage import GlobalStateStorage
from src.support.active import SelectionItem
from src.useui import Ui, UseUi


class HandleSelectionItem(UseUi):

    def __init__(self, ui: Ui, show_books: ShowBooks) -> None:
        super().__init__(ui)
        
        self.last_item: QTreeWidgetItem | None = None
        self.show_books = show_books

    def handle_selection_item(self, item: QTreeWidgetItem) -> None:
        if self.last_item == item:
            return

        self.last_item = item

        if item.parent() is None or item.parent().parent() is None:
            return

        if not re.findall(r"\d*", item.parent().text(0)):
            return

        GlobalStateStorage.selection_item = self.make_active_item(item)

        self.show_books.show()

    @staticmethod
    def make_active_item(item: QTreeWidgetItem) -> SelectionItem:
        return SelectionItem(
            class_=re.findall(r"\d*", item.parent().parent().text(0))[0],
            text=item.parent().text(0),
            reinforce=bool(item.parent().indexOfChild(item)),
        )

    def connect(self) -> None:
        self.ui.treeWidget.itemClicked.connect(self.handle_selection_item)
