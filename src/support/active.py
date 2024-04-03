from attr import define, field


@define
class SelectionItem:
    folder: str
    item: str
    filter_tags: list[str] = field(factory=list)
    root_dir_json: str = field(default="classes")
    root_dir: str = field(default="class")
