from abc import ABC, abstractmethod
from collections.abc import Callable, Iterable
from typing import Any

from PySide6.QtWidgets import QLineEdit, QPushButton, QTreeWidgetItem

from src.settings import NOT_SELECTION_BOOK
from src.storage import GlobalStateStorage
from src.support.errors import NotSelectionBookError
from src.useui import UseUi
from ui import Ui


class StringConstructor:
    @abstractmethod
    def build(self, items: dict) -> Iterable:
        ...


class Filler(UseUi):
    def __init__(self, ui: Ui, builder: StringConstructor) -> None:
        super().__init__(ui)
        
        self.builder = builder

    @abstractmethod
    def __call__(self) -> None:
        self.ui.book_contentTW.clear()

    def connect(self, btn: QPushButton, line_edit: QLineEdit) -> None:
        btn.clicked.connect(self.__call__)
        line_edit.textEdited.connect(self.search)

    @abstractmethod
    def fill(self, data) -> None:  # noqa: ANN001
        ...

    @staticmethod
    def find_item_filter(text: str) -> Callable:
        return lambda item: bool(text in item.text(0))

    @abstractmethod
    def search(self, text: str) -> None:
        ...


class ParagraphsFiller(Filler, ABC):

    def __call__(self) -> None:
        super().__call__()
        if not GlobalStateStorage.selection_book:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)
        self.ui.answersCB.setEnabled(False)
        self.ui.answersCB.hide()

        self.fill(self.builder.build(GlobalStateStorage.selection_book.content.paragraphs))

    def fill(self, built_paragraphs: Iterable) -> None:
        self.ui.searchLE.hide()
        for paragraph in built_paragraphs:
            self.ui.book_contentTW.addTopLevelItem(paragraph)


class NumbersFiller(Filler, ABC):
    def __call__(self) -> None:
        if not GlobalStateStorage.selection_book:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)

        self.ui.answersCB.setEnabled(True)
        self.ui.answersCB.show()

        self.fill(self.builder.build(GlobalStateStorage.selection_book.content.numbers))

    def fill(self, built_numbers: Iterable) -> None:
        self.ui.book_contentTW.clear()
        self.ui.searchLE.show()

        for number in built_numbers:
            self.ui.book_contentTW.addTopLevelItem(number)


def convert_strings_to_tree_widget_items(strings: Iterable[str]) -> tuple[QTreeWidgetItem, ...]:
    """Convert a list of strings to a list of QTreeWidgetItem objects.

    :param strings: A list of strings to be converted.
    :type strings: list[str]
    :return: A list of QTreeWidgetItem objects created from the input strings.
    :rtype: list[QTreeWidgetItem]
    """
    return tuple(QTreeWidgetItem([string]) for string in strings)


class ParagraphConstructor(StringConstructor):

    @abstractmethod
    def construct_paragraphs(self, tw_item: QTreeWidgetItem, paragraphs: dict) -> None:
        ...

    @abstractmethod
    def construct_paragraph_text(self, paragraph: str, paragraph_data: Any) -> str:
        ...


class NumbersConstructor(StringConstructor, ABC):
    ...
