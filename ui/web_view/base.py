from collections.abc import Callable
from typing import NewType

from PySide6.QtCore import QEvent, QUrl
from PySide6.QtWidgets import QMainWindow

from .web_view_ui import Ui_MainWindow as UiView

MyIter = NewType("MyIter", Callable)


class View(QMainWindow):

    def __init__(self, url: str | MyIter) -> None:
        super().__init__()
        self.ui = UiView()
        self.ui.setupUi(self)
        self.url: str | MyIter = url
        if isinstance(self.url, str):
            self.ui.webEngineView.setUrl(QUrl(url))

        elif it := url():
            self.ui.webEngineView.setUrl(QUrl(it))
        else:
            self.close()

    def closeEvent(self, ev: QEvent) -> None:  # noqa: N802
        if not isinstance(self.url, str) and (it := self.url()):
            self.ui.webEngineView.setUrl(QUrl(it))
            ev.ignore()
        else:
            self.ui.webEngineView.close()
            ev.accept()
