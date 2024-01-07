import os
from collections import defaultdict
from dataclasses import dataclass, field

from src.api import Api
from src.settings import BASE_PATH
from src.support.active.item import SelectionItem
from src.support.other import Json
from src.support.work_with_files import PathToFile


@dataclass(frozen=True)
class Number:
    queri: str
    answer: str


@dataclass
class Content:
    json: Json
    paragraphs: dict[str, dict[str, str]] = field(init=False)
    numbers: dict[str, Number] = field(init=False)

    def __post_init__(self) -> None:
        self.paragraphs = defaultdict(**self.json.get("Paragrafs"))
        self.numbers = self.__convert_numbers(self.json.get("Numbers"))

    def __convert_numbers(self, numbers: dict[str, str]) -> dict[str, Number]:
        return {
            name: Number(queri, self.json["result"][name])
            for name, queri in numbers.items()
        }

    def __getitem__(self, item: str):
        return self.json[item]


@dataclass
class Book:
    active_item: SelectionItem

    id_: str
    file: str
    type_: str
    image: str
    description: str
    reinforce: bool = field(default=False)

    api: Api = field(init=False, default=Api())
    __content: Content = field(init=False, repr=False, default=None)  # type: ignore
    __image: str = field(init=False, repr=False)
    __description: str = field(init=False, repr=False)

    @property
    def content(self) -> Content:
        if not self.__content:
            self.__content = Content(Json(**self.api.get_json_book(
                self.active_item,
                self.id_,
            )))

        return self.__content

    @content.setter
    def content(self, value: Content) -> None:
        self.__content = value

    @property  # type: ignore
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, value: str) -> None:
        path = PathToFile(value)

        image = self.api.get_file(path.path)
        if not image:
            self.__image = os.path.join(PathToFile(BASE_PATH).fullpath(), 'default.png')
        else:
            self.__image = self.__image[0].replace("\\", "/")

    @property  # type: ignore
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value.replace("\n\n", "\n")

    def __str__(self) -> str:
        return self.id_
