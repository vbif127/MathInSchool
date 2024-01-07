from dataclasses import dataclass, field

from src.storage.rollback import RollBack
from src.types import EventsTypes


@dataclass
class Save:
    sid: str = field(init=False)

    def __post_init__(self) -> None:
        self.sid = str(id(self))


@dataclass
class SaveHistorySelection(Save):
    change_type: EventsTypes
    roll_back_event: RollBack
    date: dict

