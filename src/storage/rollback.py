from abc import abstractmethod


class RollBack:
    @abstractmethod
    def __call__(self, *args, **kwargs) -> None:
        ...


class RollBackSelectItem(RollBack):
    def __call__(self, *args, **kwargs) -> None:
        # TODO document why this method is empty
        pass


class RollBackSelectionBook(RollBack):
    def __call__(self, *args, **kwargs) -> None:
        # TODO document why this method is empty
        pass
