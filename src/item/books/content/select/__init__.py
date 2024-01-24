from src.api import Api
from src.item.books.content.select.select_base import HandlerContentSelectionNumber, HandlerContentSelectionParagraph
from src.useui import UseUi
from ui import Ui


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
