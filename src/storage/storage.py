from abc import abstractmethod

from src.storage.save import SaveHistorySelection, Save


class Storage:

    @abstractmethod
    def add_save(self, save: Save):
        ...

    @abstractmethod
    def load_save(self, *, id_save: str = None, back: bool = False) -> Save:
        if id_save is not None and not back:
            raise ValueError("id_save must be None if back is False")


class StorageHistorySelection(Storage):

    def __init__(self):
        self.saves: dict[str, SaveHistorySelection] = {}

    def add_save(self, save: SaveHistorySelection) -> None:
        self.saves[save.sid] = save

    def load_save(self, *, id_save: str = None, back: bool = False) -> SaveHistorySelection:
        super().load_save(id_save=id_save, back=back)
        save = self.saves[id_save]
        save.roll_back_event()

        return save

