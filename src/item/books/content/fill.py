from abc import abstractmethod
from collections import defaultdict
from collections.abc import Iterable

from PySide6.QtWidgets import QPushButton, QTreeWidgetItem

from src.item.books.type import NotSelectionBookError
from src.settings import NOT_SELECTION_BOOK
from src.support.active.book import WorkWithSelectionBook, add_observer_to_notifier_selection_book
from src.useui import Ui


def convert_strings_to_tree_widget_items(strings: Iterable[str]) -> tuple[QTreeWidgetItem, ...]:
    """Convert a list of strings to a list of QTreeWidgetItem objects.

    :param strings: A list of strings to be converted.
    :type strings: list[str]
    :return: A list of QTreeWidgetItem objects created from the input strings.
    :rtype: list[QTreeWidgetItem]
    """
    return tuple(QTreeWidgetItem([string]) for string in strings)


class StringBuilder:
    @abstractmethod
    def build(self, items: dict) -> Iterable:
        ...


class ParagraphConstructor(StringBuilder):
    def __init__(self, include_desc: bool = True) -> None:
        super().__init__()
        self.include_desc = include_desc
        self.items: dict[str, list[str]] = defaultdict(list)

    def construct_paragraph(
            self,
            nw_top_level_item: QTreeWidgetItem,
            paragraphs: dict[str, str],
    ) -> None:
        for paragraph_num, desc in paragraphs.items():
            if paragraph_num == "title":
                continue

            child_item_text = self.construct_paragraph_text(desc, paragraph_num)

            child_item = QTreeWidgetItem()
            child_item.setText(0, child_item_text)

            nw_top_level_item.addChild(child_item)
            self.items[nw_top_level_item.text(0)].append(child_item_text)

    def construct_paragraph_text(self, desc: str, paragraph_num: str) -> str:
        formatted_paragraph_num = f"§{paragraph_num.replace('P.', '')}."

        if self.include_desc:
            formatted_desc = desc.split(' ???? ')[0]
            return f"{formatted_paragraph_num} {formatted_desc}"
        else:
            return formatted_paragraph_num

    def build(self, chapters: dict[str, dict[str, str]]) -> Iterable:
        for topic, paragraphs in chapters.items():
            nw_top_level_item = QTreeWidgetItem()
            nw_top_level_item.setText(0, f"""{topic.replace('subject', f'Тема: {paragraphs["title"]}')}""")

            self.construct_paragraph(nw_top_level_item, paragraphs)

            yield nw_top_level_item


class NumberConstructor(StringBuilder):
    def build(self, numbers: Iterable) -> Iterable:
        return convert_strings_to_tree_widget_items(tuple(
            it.replace("N.", "№:") for it in numbers
        ))


class Filler(WorkWithSelectionBook):
    def __init__(self, ui: Ui, builder: StringBuilder) -> None:
        super().__init__(ui)
        self.builder = builder

    @abstractmethod
    def __call__(self) -> None:
        self.ui.book_contentTW.clear()

    def connect(self, btn: QPushButton) -> None:
        btn.clicked.connect(self.__call__)


# book_contentTW
@add_observer_to_notifier_selection_book
class ParagraphFiller(Filler):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui, ParagraphConstructor())

    def __call__(self) -> None:
        super().__call__()
        if not self.book:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)
        self.ui.answersCB.setEnabled(False)

        built_paragraphs = self.builder.build(self.book.content.paragraphs)
        for paragraph in built_paragraphs:
            self.ui.book_contentTW.addTopLevelItem(paragraph)


@add_observer_to_notifier_selection_book
class NumberFiller(Filler):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui, NumberConstructor())

    def __call__(self) -> None:
        super().__call__()
        if not self.book:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)
        self.ui.answersCB.setEnabled(True)

        built_numbers = self.builder.build(self.book.content.numbers)
        for number in built_numbers:
            self.ui.book_contentTW.addTopLevelItem(number)
