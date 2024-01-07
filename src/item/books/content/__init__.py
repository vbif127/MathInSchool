from src.item.books.content.fill import Filler, NumberConstructor, NumberFiller, ParagraphConstructor, ParagraphFiller
from src.useui import Ui, UseUi


class ContentBuilder(UseUi):
    def __init__(self, ui: Ui) -> None:
        super().__init__(ui)
        self.paragraph_filler = ParagraphFiller(ui)
        self.number_filler = NumberFiller(ui)

    def connect(self) -> None:
        self.paragraph_filler.connect(self.ui.paragraphsPB)
        self.number_filler.connect(self.ui.numbersPB)

    def build(self) -> None:
        self.paragraph_filler()
        self.connect()
