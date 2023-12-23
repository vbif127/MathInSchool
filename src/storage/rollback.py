from abc import abstractmethod


class RollBack:
    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...


class RollBackSelectItem(RollBack):
    def __call__(self, *args, **kwargs):
        # TODO document why this method is empty
        pass


class RollBackSelectionBook(RollBack):
    def __call__(self, *args, **kwargs):
        # TODO document why this method is empty
        pass
