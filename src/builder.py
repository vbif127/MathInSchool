import os

from PySide6.QtWidgets import QTreeWidgetItem

from src.item.books.content.select import HandlersContentSelectionConnector
from src.item.books.select_book import HandleSelectionBook
from src.item.books.shows import ShowBooks
from src.item.select_item import HandleSelectionItem
from src.settings import CONFIG
from src.storage import GlobalStateStorage
from src.support.other import Translate
from src.useui import Ui, UseUi


class Builder(UseUi):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        translater = Translate(CONFIG)
        self.fill_manage_tree(translater)

        for other, value in CONFIG["Other"].items():
            twi_other = QTreeWidgetItem()
            twi_other.setText(0, translater.get_translate_item(other))
            twi_other.setData(0, 4, ["Other", other])
            self.ui.treeWidget.addTopLevelItem(twi_other)

        self.handle_selection_book: HandleSelectionBook | None = None
        self.handle_selection_item: HandleSelectionItem | None = None
        self.handlers_content_selection_connector: HandlersContentSelectionConnector | None = None

        self.show_books = ShowBooks(ui)
        self.ui.itemL.hide()
        self.ui.maxBT.hide()

        self.handlers_create()

    def fill_manage_tree(self, translater: Translate) -> None:
        for class_, items in CONFIG["classes"].items():
            twi_class = QTreeWidgetItem()
            twi_class.setText(0, f"{class_} класс")
            twi_class.setData(0, 4, f"{class_} class")
            for item in items.keys():
                if item not in ["Algebra", "Geometry", "Mathematics"]:
                    continue
                twi_item = QTreeWidgetItem(twi_class)
                twi_item.setText(0, translater.get_translate_item(item))
                twi_item.setData(0, 4, item)

                base_tip = QTreeWidgetItem(twi_item)
                base_tip.setText(0, "Базовый курс")
                base_tip.setData(0, 4, [])

                reinforce_tip = QTreeWidgetItem(twi_item)
                reinforce_tip.setText(0, "Углублённый курс")
                reinforce_tip.setData(0, 4, ["reinforce"])

            self.ui.treeWidget.addTopLevelItem(twi_class)

    def handlers_create(self) -> None:
        self.handle_selection_item = HandleSelectionItem(
            self.ui, self.show_books,
        )
        self.handle_selection_book = HandleSelectionBook(
            self.ui,
        )

        self.handlers_content_selection_connector = HandlersContentSelectionConnector(
            self.ui,
        )

    def build(self) -> None:
        if self.handle_selection_item:
            self.handle_selection_item.connect()
        if self.handle_selection_book:
            self.handle_selection_book.connect()
        if self.handlers_content_selection_connector:
            self.handlers_content_selection_connector.connect()

    def __del__(self):
        for file in set(GlobalStateStorage.installed_files):
            os.remove(file)
