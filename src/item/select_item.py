import re

from PySide6.QtWidgets import QTreeWidgetItem

from src.item.books.shows import ShowBooks
from src.settings import CONFIG
from src.storage import GlobalStateStorage
from src.support.active import SelectionItem
from src.support.other import Translate, get_nesting_level
from src.useui import Ui, UseUi


class HandleSelectionItem(UseUi):

    def __init__(self, ui: Ui, show_books: ShowBooks) -> None:
        super().__init__(ui)

        self.last_item: QTreeWidgetItem | None = None
        self.show_books = show_books
        self.translater = Translate(CONFIG)

    def handle_selection_item(self, item: QTreeWidgetItem) -> None:
        if self.last_item == item:
            return
        self.last_item = item
        nesting_level = get_nesting_level(item)
        match nesting_level:
            case 1 if "Other" in item.data(0, 4):
                selection_item = SelectionItem(
                    item="Математика",
                    folder=item.data(0, 4)[1],
                    filter_tags=None,
                    root_dir_json="Other",
                    root_dir=item.data(0, 4)[1],
                )
                self.ui.itemL.setText(f"{self.translater.get_translate_item(item.data(0, 4)[1])}. Математике")
            case 2:
                class_ = re.findall(r"\d+", item.parent().text(0))[0]
                selection_item = SelectionItem(
                    item=item.text(0),
                    folder=class_,
                    filter_tags=[],
                    root_dir=f"{class_} class",
                )
                self.ui.itemL.setText(f"{selection_item.item}. {selection_item.folder} класс")
            case 3:
                class_ = re.findall(r"\d+", item.parent().parent().text(0))[0]
                selection_item = SelectionItem(
                    item=item.parent().text(0),
                    folder=class_,
                    filter_tags=["reinforce"] if item.parent().indexOfChild(item) else [],
                    root_dir=f"{class_} class",
                )
                self.ui.itemL.setText(f"{selection_item.item}. {selection_item.folder} класс")
            case _:
                return
        GlobalStateStorage.selection_item = selection_item

        # self.set_info_text(item)
        self.ui.itemL.show()
        self.show_books.show()


    def connect(self) -> None:
        self.ui.treeWidget.currentItemChanged.connect(self.handle_selection_item)
