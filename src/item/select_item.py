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
        is_oge = item.text(0) == "ОГЭ"
        if not item.parent():
            return
        if not item.parent().parent() and not is_oge:
            return

        if not re.findall(r"\d*", item.parent().text(0)):
            return

        GlobalStateStorage.selection_item = self.make_active_item(item, is_oge)

        self.ui.itemL.setText(f"{item.parent().text(0) if not is_oge else item.text(0)}. {GlobalStateStorage.selection_item.class_} класс")
        self.ui.itemL.show()
        self.show_books.show()

    @staticmethod
    def make_active_item(item: QTreeWidgetItem, is_oge: bool) -> SelectionItem:
        return SelectionItem(
            class_=re.findall(r"\d*", item.parent().parent().text(0)
            if item.parent().parent() and item.text(0) != "ОГЭ" else
            item.parent().text(0))[0],
            text=item.parent().text(0) if not is_oge else item.text(0),
            filter_tags=["reinforce"] if item.parent().indexOfChild(item) else [],
        )

    def connect(self) -> None:
        self.ui.treeWidget.itemClicked.connect(self.handle_selection_item)
