import os
from abc import abstractmethod

from PySide6.QtWidgets import QCheckBox, QPushButton, QTreeWidgetItem

from src.api import Api
from src.item.books.select_book import NotSelectionBookError
from src.settings import SPLIT_PARAGRAPH_SYMBOL
from src.support.active.book import WorkWithSelectionBook, add_observer_to_notifier_selection_book
from src.support.my_iter import MyIter
from src.support.other import web_view
from src.useui import Ui, UseUi


class HandlerContentSelection(WorkWithSelectionBook):

    def __init__(self, ui: Ui, api: Api, cb_btn: QPushButton) -> None:
        super().__init__(ui)
        self.api = api
        self.cb_btn = cb_btn

    @abstractmethod
    def __call__(self, item: QTreeWidgetItem, column: int) -> None:
        ...

    def view(self, urls: list[str], files: list[str], check_box: QCheckBox) -> None:
        if check_box.isChecked() and urls:
            web_view(self, MyIter(urls))

        for received_files in (self.api.get_file(filepath) for filepath in files):
            for file in received_files:
                os.startfile(file)


@add_observer_to_notifier_selection_book
class HandlerContentSelectionNumber(HandlerContentSelection):

    def __call__(self, item: QTreeWidgetItem, _: int) -> None:
        if not self.cb_btn.isChecked():
            return


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
        self.view(urls, files, self.ui.videoCB)

    @staticmethod
    def get_adaptation_topic(topic: str) -> str:
        return topic.split(":")[0].replace("Тема", "subject")

    def get_scraped_paragraph(self, paragraph: str, topic: str) -> list[str]:
        if self.book is None:
            raise NotSelectionBookError("Не выбрана книга")

        paragraphs = self.book.content.paragraphs[topic]
        paragraph = paragraphs[self.get_adaptation_paragraph(paragraph)]
        return paragraph.split(SPLIT_PARAGRAPH_SYMBOL)[1:]

    @staticmethod
    def get_adaptation_paragraph(paragraph: str) -> str:
        return paragraph.replace('§', "P.").split(". ")[0]

    @staticmethod
    def separation_of_files_and_urls(scraped: list) -> tuple[list, list]:
        urls = [url for url in scraped if url.startswith("http")]
        files = [file for file in scraped if not file.startswith("http")]
        return urls, files


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
