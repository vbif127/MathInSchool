from src.item.books.type.type_abc import Book
from src.support.active import SelectionItem


class GlobalStateStorage:
    selection_item: SelectionItem | None = None
    selection_book: Book | None = None
    books: list[Book] = []

    installed_files: list[str] = []
