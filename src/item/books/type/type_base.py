from collections import defaultdict

from attrs import define, field

from src.item.books.type.type_abc import BaseParagraphData, Book, Content, NumberText, ParagraphText, SubjectText
from src.support.other import Json


@define(frozen=True)
class BaseNumberData:
    path_to_question: str
    path_to_answers: str


@define
class BaseContent(Content):
    json: Json
    paragraphs: dict[SubjectText, dict[ParagraphText, BaseParagraphData]] = field(init=False)
    numbers: dict[NumberText, BaseNumberData] = field(init=False)

    def __attrs_post_init__(self) -> None:
        self.paragraphs = defaultdict(**self.json.get("Paragrafs"))
        self.numbers = self.__convert_numbers(self.json.get("Numbers"))

    def __convert_numbers(self, numbers: dict[NumberText, str]) -> dict[NumberText, BaseNumberData]:
        return {
            question: BaseNumberData(path_to_question, self.json["result"][question])
            for question, path_to_question in numbers.items()
        }

    def __getitem__(self, item: str):
        return self.json[item]


@define
class BaseBook(Book):
    __content: Content = field(init=False, repr=False, default=None)  # type: ignore

    @property
    def content(self) -> BaseContent:
        if not self.__content:
            json_book = self.api.get_json_book(
                self.active_item,
                self.id_,
            )
            self.__content = BaseContent(json_book)

        return self.__content

    @content.setter
    def content(self, value: Content) -> None:
        self.__content = value
