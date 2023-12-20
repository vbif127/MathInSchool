from abc import abstractmethod

from src.storage.save import SaveActiveItem, Save


class Storage:

    @abstractmethod
    def add_save(self, save: Save):
        ...

    @abstractmethod
    def load_save(self, *, id_save: str = None, back: bool = False) -> Save:
        if id_save is not None and back is False:
            raise ValueError("id_save must be None if back is False")


class StorageActiveItem(Storage):

    def __init__(self):
        ...

    def add_save(self, save: SaveActiveItem) -> None:
        ...

    def load_save(self, *, id_save: str = None, back: bool = False) -> SaveActiveItem:
        super().load_save(id_save=id_save, back=back)
