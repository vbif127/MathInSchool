from src.books.shows import ShowBooks
from src.select.select_item import HandleSelection
from src.storage.main import StorageActiveItem
from src.support.active import NotifierOfChangeActiveItem
from src.useui import UseUi, Ui


class Builder(UseUi):
    def __init__(self, ui: Ui):
        super().__init__(ui)
        self.active_item = None

        self.storage = StorageActiveItem()
        self.notifier = NotifierOfChangeActiveItem()

        self.notifier.set_values(item=self.active_item, storage=self.storage)

        self.show_books = ShowBooks(ui, self.active_item, self.notifier)
        self.select_item = HandleSelection(
            ui,
            self.active_item,
            self.notifier,
            self.show_books
        )

    def build(self):
        self.select_item.connect()
