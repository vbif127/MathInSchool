from attr import define, field


@define
class SelectionItem:
    class_: int = field(converter=int)
    text: str
    reinforce: bool
