from collections.abc import Iterable
from typing import Any

from PySide6.QtWidgets import QTreeWidgetItem

from src.item.books.content import ParagraphsFiller
from src.item.books.content.fill.fill_abc import NumbersConstructor, ParagraphConstructor
from src.item.books.type.type_abc import BaseParagraphData, ParagraphText, SubjectText
from src.item.books.type.type_new import NewParagraphData
from ui import Ui


class NewNumbersConstructor(NumbersConstructor):
    def build(self, numbers: dict) -> Iterable:
        for number, number_data in numbers.items():
            number_it = QTreeWidgetItem()
            number_it.setText(0, number.replace('N.', '№:'))
            number_it.setData(0, 1, number_data)

            yield number_it


class NewParagraphConstructor(ParagraphConstructor):
    def __init__(self):
        self.numbers_constructor = NewNumbersConstructor()

    def construct_paragraphs(self, top_level_item: QTreeWidgetItem,
                             paragraphs: dict[ParagraphText, NewParagraphData | BaseParagraphData]) -> None:
        for paragraph, paragraph_data in paragraphs.items():
            if paragraph == "title":
                continue

            child_item = QTreeWidgetItem()
            child_item.setText(0, self.construct_paragraph_text(paragraph))
            for number_it in self.numbers_constructor.build(paragraph_data["numbers"]):
                child_item.addChild(number_it)

            top_level_item.addChild(child_item)

    def construct_paragraph_text(self, paragraph: str, *_: Any) -> str:
        return paragraph.replace('P.', '§')

    def build(self, chapters: dict[SubjectText, dict[ParagraphText, NewParagraphData | BaseParagraphData]]) -> list:
        for topic, paragraphs in chapters.items():
            top_level_item = QTreeWidgetItem()
            top_level_item.setText(0, f"""{topic.replace('subject', f'Глава: {paragraphs["title"]}')}""")

            self.construct_paragraphs(top_level_item, paragraphs)

            yield top_level_item


class NewParagraphsFiller(ParagraphsFiller):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui, NewParagraphConstructor())

    def fill(self, built_paragraphs: Iterable) -> None:
        super_call = super().fill(built_paragraphs)
        self.ui.answersCB.show()
        self.ui.answersCB.setEnabled(True)

        return super_call

    def search(self, text: str) -> None:
        ...
