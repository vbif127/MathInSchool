from src.select.select_item import HandleSelection
from src.useui import UseUi, Ui


class Builder(UseUi):
    def __init__(self, ui: Ui):
        super().__init__(ui)
        self.select_item = HandleSelection(ui)

    def build(self):
        self.select_item.connect()
