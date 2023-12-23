from src.item.books.shows import ShowBooks
from src.item.select_item import HandleSelection
from src.storage.storage import StorageHistorySelection
from src.support.active.item import NotifierOfChangeSelectionItem
from src.useui import UseUi, Ui


class Builder(UseUi):
    def __init__(self, ui: Ui):
        super().__init__(ui)
        self.active_item = None

        self.storage = StorageHistorySelection()
        self.notifier = NotifierOfChangeSelectionItem()

        self.notifier.set_values(item=self.active_item, storage=self.storage)

        self.show_books = ShowBooks(ui, self.active_item, self.notifier)
        self.select_item = HandleSelection(
            ui,
            self.active_item,
            self.notifier,
        )

    def build(self):
        self.select_item.connect()
