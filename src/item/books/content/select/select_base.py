from PySide6.QtWidgets import QPushButton, QTreeWidgetItem

from src.api import Api
from src.item.books.content.select.select_abc import (
    HandlerContentSelection,
    adaptation_paragraph,
    separation_of_files_and_urls,
    split_by_separator,
)
from src.item.books.type.type_abc import TypesBooks
from src.item.books.type.type_base import BaseNumberData
from src.item.books.type.type_new import NewParagraphData
from src.settings import NOT_SELECTION_BOOK
from src.storage import GlobalStateStorage
from src.support.errors import NotSelectionBookError
from ui import Ui


class HandlerContentSelectionNumber(HandlerContentSelection):

    def __call__(self, item: QTreeWidgetItem, _: int) -> None:
        if not self.cb_btn.isChecked():
            return

        number = self.get_number(item)

        self.view_files(item, [number.path_to_question])
        self.view_answers(item, number)

    def view_answers(self, item: QTreeWidgetItem, number: BaseNumberData) -> None:
        files_result, urls = separation_of_files_and_urls(split_by_separator(number.path_to_answers))

        self.view_video(item, urls, self.ui.videoCB)
        self.view_files(item, files_result, self.ui.answersCB)

    @staticmethod
    def get_number(item: QTreeWidgetItem) -> BaseNumberData:
        if not GlobalStateStorage.selection_book:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)

        question = item.text(0).replace("№:", "N.")
        number = GlobalStateStorage.selection_book.content.numbers[question]
        return number


class ParagraphGetter:
    @staticmethod
    def get_adaptation_topic(topic: str) -> str:
        return topic.split(":")[0].replace("Глава", "subject")

    @staticmethod
    def get_paragraph(topic: str, paragraph: str) -> dict | str:
        if GlobalStateStorage.selection_book is None:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)

        paragraphs = GlobalStateStorage.selection_book.content.paragraphs[topic]
        adapted_paragraph = adaptation_paragraph(paragraph)

        if GlobalStateStorage.selection_book.type_ == TypesBooks.NEW.value:
            return paragraphs[adapted_paragraph]
        print(paragraph, adapted_paragraph)
        return paragraphs[adapted_paragraph.split(". ")[0]]

    def get_scraped_paragraph(self, topic: str, paragraph: str) -> list[str]:
        paragraph = self.get_paragraph(topic, paragraph)
        return split_by_separator(paragraph)[1:]


class WorkWithParagraph:
    def __init__(self):
        self.paragraph_getter = ParagraphGetter()

    def get_files_and_urls_or_numbers(self, item: QTreeWidgetItem, is_paragraph: bool = False) -> \
            dict[str, dict[str, list[str]]] | tuple[list[str], list[str]]:
        if GlobalStateStorage.selection_book.type_ == TypesBooks.NEW.value:
            files, urls, numbers = self.get_urls_and_files_from_new_paragraph(item)
            if not is_paragraph:
                return numbers
            return files, urls
        else:
            files, urls = self.get_urls_and_files_from_base_paragraph(item)
        return files, urls

    def get_urls_and_files_from_base_paragraph(self, item: QTreeWidgetItem) -> tuple[list[str], list[str]]:
        topic = self.paragraph_getter.get_adaptation_topic(item.parent().text(0))
        paragraph = self.paragraph_getter.get_scraped_paragraph(topic, item.text(0))
        return separation_of_files_and_urls(paragraph)

    def get_urls_and_files_from_new_paragraph(self, item: QTreeWidgetItem) -> \
            tuple[list[str], list[str], dict[str, dict[str, list[str]]]]:
        topic = self.paragraph_getter.get_adaptation_topic(item.parent().text(0))
        paragraph: NewParagraphData = self.paragraph_getter.get_paragraph(topic, item.text(0))
        return paragraph["files"], paragraph["videos"], paragraph["numbers"]


class HandlerContentSelectionParagraph(HandlerContentSelection):
    def __init__(self, ui: Ui, api: Api, cb_btn: QPushButton):
        super().__init__(ui, api, cb_btn)
        self.work_with_paragraph = WorkWithParagraph()

    def __call__(self, item: QTreeWidgetItem, _: int) -> None:
        if not self.cb_btn.isChecked():
            return
        if item.parent() is None:
            return

        if GlobalStateStorage.selection_book.type_ == TypesBooks.NEW.value:
            if item.parent().parent():
                files_and_urls = self.work_with_paragraph.get_files_and_urls_or_numbers(item.parent())
                numbers = files_and_urls

                number_text = item.text(0).replace("№:", "N.")
                number = numbers[number_text]

                self.view_files(item, number.questions)
                self.view_files(item, [
                    file for file in number.answers
                    if file.startswith("classes")
                ], self.ui.answersCB)

                self.view_video(item, [
                    url for url in number.answers
                    if url.startswith("http")
                ], self.ui.videoCB)

                return
            files, urls = self.work_with_paragraph.get_files_and_urls_or_numbers(item, True)
        else:
            files, urls, *_ = self.work_with_paragraph.get_files_and_urls_or_numbers(item)

        self.view(item, urls, files, self.ui.videoCB)
