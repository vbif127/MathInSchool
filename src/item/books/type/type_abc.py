import os
from enum import Enum
from typing import Any, TypeVar

from attrs import define, field

from src.api import Api
from src.settings import BASE_PATH
from src.support.active import SelectionItem
from src.support.other import Json
from src.support.work_with_files import PathToFile

File = TypeVar("File", bound=str)
Video = TypeVar("Video", bound=str)
Question = TypeVar("Question", bound=str)
Answer = TypeVar("Answer", bound=str)
SubjectText = TypeVar("SubjectText", bound=str)
ParagraphText = TypeVar("ParagraphText", bound=str)
BaseParagraphData = TypeVar("BaseParagraphData", bound=str)
NumberText = TypeVar("NumberText", bound=str)


class TypesBooks(Enum):
    BASE = "base"
    NEW = "new"


@define
class Content:
    json: Json
    paragraphs: Any = field(init=False)
    numbers: Any = field(init=False)


class Image:
    def __init__(self, path: str):
        self.api = Api()
        self.path = self.get_image(path)

    def get_image(self, path: str) -> str:
        path = PathToFile(path)

        image = self.api.get_file(path.path)

        if not image:
            return os.path.join(PathToFile(BASE_PATH).fullpath(), 'default.png').replace("\\", "/")

        return image[0].replace("\\", "/")

    def __str__(self):
        return self.path



@define
class Book:
    active_item: SelectionItem

    id_: str
    file: str
    type_: str
    image: Image | str = field(converter=Image)
    description: str
    tags: list[str] = field(default=[])

    api: Api = field(init=False, default=Api())
    __content: Content = field(init=False, repr=False, default=None)  # type: ignore
    __description: str = field(init=False, repr=False, converter=lambda desc: desc.replace("\n\n", "\n"))

    @property
    def content(self) -> Content:
        return self.__content

    @content.setter
    def content(self, value: Content) -> None:
        self.__content = value

    def __str__(self) -> str:
        return self.id_
