import re
from collections import defaultdict
from collections.abc import Iterable

from PySide6.QtWidgets import QTreeWidgetItem

from src.item.books.content.fill.fill_abc import (
    NumbersConstructor,
    NumbersFiller,
    ParagraphConstructor,
    ParagraphsFiller,
    convert_strings_to_tree_widget_items,
)
from src.settings import NOT_SELECTION_BOOK
from src.storage import GlobalStateStorage
from src.support.errors import NotSelectionBookError
from src.useui import Ui


class BaseParagraphsConstructor(ParagraphConstructor):
    def __init__(self, include_desc: bool = True) -> None:
        super().__init__()
        self.include_desc = include_desc
        self.items: dict[str, list[str]] = defaultdict(list)

    def construct_paragraphs(
            self,
            top_level_item: QTreeWidgetItem,
            paragraphs: dict[str, str],
    ) -> None:
        for paragraph, paragraph_data in paragraphs.items():
            if paragraph == "title":
                continue

            child_item, child_item_text = self.create_child_item(paragraph, paragraph_data)

            top_level_item.addChild(child_item)
            self.items[top_level_item.text(0)].append(child_item_text)

    def create_child_item(self, paragraph: str, paragraph_data: str) -> tuple[QTreeWidgetItem, str]:
        child_item_text = self.construct_paragraph_text(paragraph, paragraph_data)
        child_item = QTreeWidgetItem()
        child_item.setText(0, child_item_text)
        child_item.setToolTip(0, f'{len([it for it in paragraph_data.split(" ???? ")[1:] if re.findall(r"http", it)])}'
                                 f' видео')
        return child_item, child_item_text

    def construct_paragraph_text(self, paragraph: str, paragraph_data: str) -> str:
        formatted_paragraph_num = f"{paragraph.replace('P.', '§.')}"

        if self.include_desc:
            formatted_desc = paragraph_data.split(' ???? ')[0]
            return f"{formatted_paragraph_num}. {formatted_desc}"
        else:
            return formatted_paragraph_num

    def build(self, chapters: dict[str, dict[str, str]]) -> Iterable:

        for topic, paragraphs in chapters.items():
            nw_top_level_item = self.create_top_level_item(paragraphs, topic)

            self.construct_paragraphs(nw_top_level_item, paragraphs)

            yield nw_top_level_item

    @staticmethod
    def create_top_level_item(paragraphs: dict[str, str], topic: str) -> QTreeWidgetItem:
        nw_top_level_item = QTreeWidgetItem()
        nw_top_level_item.setText(0, f"""{topic.replace('subject', f'Глава: {paragraphs["title"]}')}""")
        return nw_top_level_item


class BaseNumbersConstructor(NumbersConstructor):

    def build(self, numbers: Iterable) -> Iterable:
        return convert_strings_to_tree_widget_items(tuple(
            it.replace("N.", "№:") for it in numbers
        ))


# book_contentTW
class BaseParagraphsFiller(ParagraphsFiller):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui, BaseParagraphsConstructor())

    def search(self, text: str) -> None:
        ...


class BaseNumbersFiller(NumbersFiller):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui, BaseNumbersConstructor())

    def search(self, text: str) -> None:
        if not GlobalStateStorage.selection_book:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)
        if not self.ui.numbersPB.isChecked():
            return

        self.fill(list(filter(
            self.find_item_filter(text),
            self.builder.build(GlobalStateStorage.selection_book.content.numbers),
        )))
