from attrs import define, field  # noqa: I001
from typing import TypedDict

from src.item.books.type.type_abc import (
    Answer,
    Book,
    Content,
    File,
    NumberText,
    ParagraphText,
    Question,
    SubjectText,
    Video, BaseParagraphData
)
from src.support.other import Json


@define(frozen=True)
class NewNumberData:
    questions: list[Question]
    answers: list[Answer]


class NewParagraphData(TypedDict):
    files: list[File]
    videos: list[Video]
    numbers: dict[ParagraphText, dict[NumberText, NewNumberData]]


@define
class NewContent(Content):
    json: Json
    paragraphs: dict[SubjectText, dict[ParagraphText, NewParagraphData | BaseParagraphData]] = field(init=False)

    def __attrs_post_init__(self):
        self.paragraphs = self.__convert_paragraphs(self.json.get("Paragraphs"))

    def __convert_paragraphs(self, data: dict) ->\
            dict[SubjectText, dict[ParagraphText, NewParagraphData | BaseParagraphData]]:
        subjects = {}
        for subject, paragraphs in data.items():

            subjects[subject] = {}
            for paragraph, paragraph_data in paragraphs.items():

                if paragraph == "title":
                    subjects[subject][paragraph] = paragraph_data
                    continue
                subjects[subject][paragraph] = NewParagraphData(
                    files=paragraph_data["files"],
                    videos=paragraph_data["videos"],
                    numbers=self.__convert_numbers(paragraph_data["numbers"])
                )

        return subjects

    @staticmethod
    def __convert_numbers(data: dict) -> dict[NumberText, NewNumberData]:
        return {
            number: NewNumberData(questions=numbers["questions"], answers=numbers["answers"])
            for number, numbers in data.items()
        }


@define
class NewBook(Book):
    __content: NewContent = field(init=False, repr=False, default=None)

    @property
    def content(self) -> NewContent:
        if not self.__content:
            json_book = self.api.get_json_book(
                self.active_item,
                self.id_,
            )
            self.__content = NewContent(json_book)

        return self.__content

    @content.setter
    def content(self, value: NewContent) -> None:
        self.__content = value
