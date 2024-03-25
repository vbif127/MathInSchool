import webbrowser
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
            webbrowser.open_new_tab(url)
            # self.ui.webEngineView.setUrl(QUrl(url))

        elif it := url():
            webbrowser.open_new_tab(it)
            # self.ui.webEngineView.setUrl(QUrl(it))
        else:
            self.close()

    def closeEvent(self, ev: QEvent) -> None:  # noqa: N802
        if not isinstance(self.url, str) and (it := self.url()):
            webbrowser.open_new_tab(it)
            # self.ui.webEngineView.setUrl(QUrl(it))
            ev.ignore()
        else:
            self.ui.webEngineView.close()
            ev.accept()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication()
    view = View("https://youtu.be/rA0g6QOKsaE?list=PLsLi_s1jExgRpu2U6pHcTF71eh3UI2mbf")
    view.show()
    app.exec()