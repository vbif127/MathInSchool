from attr import define, field


@define
class SelectionItem:
    class_: int = field(converter=int)
    text: str
    filter_tags: list[str] = field(factory=list)
