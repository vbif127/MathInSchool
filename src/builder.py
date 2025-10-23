import os

from PySide6.QtWidgets import QTreeWidgetItem

from src.item.books.content.select import HandlersContentSelectionConnector
from src.item.books.select_book import HandleSelectionBook
from src.item.books.shows import ShowBooks
from src.item.select_item import HandleSelectionItem
from src.settings import BASE_PATH, CONFIG
from src.storage import GlobalStateStorage
from src.support.other import Translate
from src.support.work_with_files import PathToFile
from src.useui import Ui, UseUi


class Builder(UseUi):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        translator = Translate(CONFIG)

        self.fill_manage_tree(translator)
        self.fill_other_to_manage_tree(translator)
        path = os.path.join(PathToFile(BASE_PATH).fullpath(), "assets\\Icon.png").replace("\\", "/")
        self.ui.icon.setStyleSheet(f"border-image: url({path});")

        self.handle_selection_book: HandleSelectionBook | None = None
        self.handle_selection_item: HandleSelectionItem | None = None
        self.handlers_content_selection_connector: HandlersContentSelectionConnector | None = None

        self.show_books = ShowBooks(ui)
        self.ui.itemL.hide()
        self.ui.maxBT.hide()

        self.handlers_create()

        self.ui.aboutB.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(2))
        self.ui.back2B.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))

    def fill_other_to_manage_tree(self, translator: Translate) -> None:
        for other, _ in CONFIG["Other"].items():
            twi_other = self.build_other_twi(
                translator.get_translate_item(other),
                other,
                None,
            )

            match other:
                case "EGE":
                    base_child = self.build_other_twi("Базовый", other, [])
                    reinforce_child = self.build_other_twi("Профиль", other, ["reinforce"])
                    twi_other.addChild(base_child)
                    twi_other.addChild(reinforce_child)
                case "Library":
                    fragment_child = self.build_other_twi("Новинки издательств", other, ["fragment"])
                    directory_child = self.build_other_twi("Справочники", other, ["directory"])

                    twi_other.addChild(directory_child)
                    # twi_other.addChild(table_child)
                    twi_other.addChild(fragment_child)

            self.ui.treeWidget.addTopLevelItem(twi_other)

    @staticmethod
    def build_other_twi(text: str, dir_: str, filter_tags: list[str] | None) -> QTreeWidgetItem:
        child = QTreeWidgetItem()
        child.setText(0, text)
        child.setData(0, 4, ["Other", dir_, filter_tags])
        return child

    def fill_manage_tree(self, translator: Translate) -> None:
        for class_, items in CONFIG["classes"].items():
            twi_class = QTreeWidgetItem()
            twi_class.setText(0, f"{class_} класс")
            twi_class.setData(0, 4, f"{class_} class")
            for item in items.keys():
                if item not in ["Algebra", "Geometry", "Mathematics"]:
                    continue
                twi_item = QTreeWidgetItem(twi_class)
                twi_item.setText(0, translator.get_translate_item(item))
                twi_item.setData(0, 4, item)

                base_tip = QTreeWidgetItem(twi_item)
                base_tip.setText(0, "Базовый уровень")
                base_tip.setData(0, 4, [])

                reinforce_tip = QTreeWidgetItem(twi_item)
                reinforce_tip.setText(0, "Углублённый уровень")
                reinforce_tip.setData(0, 4, ["reinforce"])

            self.ui.treeWidget.addTopLevelItem(twi_class)

    def handlers_create(self) -> None:
        self.handle_selection_item = HandleSelectionItem(
            self.ui,
            self.show_books,
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
