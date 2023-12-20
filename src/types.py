from dataclasses import dataclass, field

from src.api import Api
from src.support.active import ActiveItem, WorkWithActiveItem, add_observer_to_notifier
from src.support.other import Json


@dataclass(frozen=True)
class Number:
    queri: str
    answer: str


@dataclass
class Content:
    json: Json
    paragraph: dict[str] = field(init=False)
    numbers: dict[str, Number] = field(init=False)

    def __post_init__(self):
        self.paragraph = self.json.get("paragraph")
        self.numbers = self.__convert_numbers(self.json.get("numbers"))

    def __convert_numbers(self, numbers: dict[str, str]) -> dict[str, Number]:
        return {
            name: Number(queri, self.json["result"][name])
            for name, queri in numbers.items()
        }


@add_observer_to_notifier
@dataclass
class Book(WorkWithActiveItem):
    active_item: ActiveItem = field(init=False, default=None)

    id_: str
    description: str
    file: str
    image: str
    type_: str
    reinforce: bool = field(default=False)

    api: Api = field(init=False, default=Api())
    __content: Content = field(init=False, repr=False)

    @property
    def content(self):
        if not self.__content:
            self.__content = Content(self.api.get_json_book(
                self.active_item,
                self.id_,
            ))

        return self.__content

    def update(self, item: ActiveItem):
        self.active_item = item
