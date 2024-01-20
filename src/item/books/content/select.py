from abc import abstractmethod

from PySide6.QtWidgets import QCheckBox, QPushButton, QTreeWidgetItem

from src.api import Api
from src.item.books.type import NotSelectionBookError, Number
from src.settings import NOT_SELECTION_BOOK, SEPARATOR
from src.support.active.book import WorkWithSelectionBook, add_observer_to_notifier_selection_book
from src.support.other import get_random_string
from src.useui import Ui, UseUi
from ui.choice_video_or_answer.choice import ChoiceAnswerWindow, ChoiceFileWindow, ChoiceVideoWindow


class HandlerContentSelection(WorkWithSelectionBook):

    def __init__(self, ui: Ui, api: Api, cb_btn: QPushButton) -> None:
        super().__init__(ui)

        self.api = api
        self.cb_btn = cb_btn

    @abstractmethod
    def __call__(self, item: QTreeWidgetItem, column: int) -> None:
        ...

    def view(self, item: QTreeWidgetItem, urls: list[str], files: list[str], check_box: QCheckBox) -> None:
        self.view_video(item, urls, check_box)
        self.view_files(item, files)

    def view_files(self, item: QTreeWidgetItem, files: list[str], check_box: QCheckBox | None = None) -> None:
        if check_box is None:
            setattr(self, get_random_string(), ChoiceFileWindow(item.text(0), files))
            return

        if not check_box.isChecked():
            return

        setattr(self, get_random_string(), ChoiceAnswerWindow(item.text(0), files))

    def view_video(self, item: QTreeWidgetItem,  urls: list[str], check_box: QCheckBox | None = None) -> None:
        if not urls or check_box is None or not check_box.isChecked():
            return
        setattr(self, get_random_string(), ChoiceVideoWindow(item.text(0), urls))

    @staticmethod
    def separation_of_files_and_urls(scraped: list) -> tuple[list, list]:
        urls = [url for url in scraped if url.startswith("http")]
        files = [file for file in scraped if not file.startswith("http")]
        return urls, files

    @staticmethod
    def split_by_separator(item: str) -> list:
        return item.split(SEPARATOR)


@add_observer_to_notifier_selection_book
class HandlerContentSelectionNumber(HandlerContentSelection):

    def __call__(self, item: QTreeWidgetItem, _: int) -> None:
        if not self.cb_btn.isChecked():
            return

        number = self.get_number(item)

        self.view_files(item, [number.path_to_question])
        self.view_answers(item, number)

    def view_answers(self, item: QTreeWidgetItem, number: Number) -> None:
        urls, files_result = self.separation_of_files_and_urls(self.split_by_separator(number.path_to_answers))

        self.view_video(item, urls, self.ui.videoCB)
        self.view_files(item, files_result, self.ui.answersCB)

    def get_number(self, item: QTreeWidgetItem) -> Number:
        if not self.book:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)

        question = item.text(0).replace("№:", "N.")
        number = self.book.content.numbers[question]
        return number


@add_observer_to_notifier_selection_book
class HandlerContentSelectionParagraph(HandlerContentSelection):

    def __call__(self, item: QTreeWidgetItem, _: int) -> None:
        if not self.cb_btn.isChecked():
            return
        if item.parent() is None:
            return

        topic = self.get_adaptation_topic(item.parent().text(0))
        paragraph = self.get_scraped_paragraph(item.text(0), topic)
        urls, files = self.separation_of_files_and_urls(paragraph)
        self.view(item, urls, files, self.ui.videoCB)

    @staticmethod
    def get_adaptation_topic(topic: str) -> str:
        return topic.split(":")[0].replace("Тема", "subject")

    def get_scraped_paragraph(self, paragraph: str, topic: str) -> list[str]:
        if self.book is None:
            raise NotSelectionBookError(NOT_SELECTION_BOOK)

        paragraphs = self.book.content.paragraphs[topic]
        paragraph = paragraphs[self.get_adaptation_paragraph(paragraph)]
        return self.split_by_separator(paragraph)[1:]

    @staticmethod
    def get_adaptation_paragraph(paragraph: str) -> str:
        return paragraph.replace('§', "P.").split(". ")[0]


class HandlersContentSelectionConnector(UseUi):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        self.api = Api()

        self.handler_selection_number = HandlerContentSelectionNumber(
            self.ui, self.api, self.ui.numbersPB
        )
        self.handler_selection_paragraph = HandlerContentSelectionParagraph(
            self.ui, self.api, self.ui.paragraphsPB
        )

    def connect(self) -> None:
        self.ui.book_contentTW.itemDoubleClicked.connect(
            self.handler_selection_paragraph
        )
        self.ui.book_contentTW.itemDoubleClicked.connect(
            self.handler_selection_number
        )
