from abc import abstractmethod

from src.item.books.content.fill.fill_abc import Filler, NumbersFiller, ParagraphsFiller
from src.item.books.content.fill.fill_base import BaseNumbersFiller, BaseParagraphsFiller
from src.item.books.content.fill.fill_new import NewParagraphsFiller
from src.useui import Ui, UseUi


class ContentBuilder(UseUi):
    @abstractmethod
    def __init__(self, ui: Ui):
        super().__init__(ui)
        self.paragraph_filler: ParagraphsFiller = None

    def connect(self) -> None:
        self.paragraph_filler.connect(self.ui.paragraphsPB, self.ui.searchLE)

    def build(self) -> None:
        self.paragraph_filler()
        self.connect()


class BaseContentBuilder(ContentBuilder):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        self.paragraph_filler = BaseParagraphsFiller(ui)
        self.number_filler = BaseNumbersFiller(ui)
        self.ui.numbersPB.setEnabled(True)

    def connect(self) -> None:
        super().connect()
        self.number_filler.connect(self.ui.numbersPB, self.ui.searchLE)


class NewContentBuilder(ContentBuilder):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        self.paragraph_filler = NewParagraphsFiller(ui)
        self.ui.numbersPB.setEnabled(False)
