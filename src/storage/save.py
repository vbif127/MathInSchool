from dataclasses import dataclass, field


@dataclass
class Save:
    sid: str = field(init=False)

    def __post_init__(self):
        self.sid = str(id(self))


class SaveActiveItem(Save):
    ...
