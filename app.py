from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QMouseEvent, QIcon
from PySide6.QtWidgets import QMainWindow

from src.builder import Builder
from ui import Ui


class MathInSchool(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.moving_flag: bool = None
        self.maximize_flag: bool = False
        self.offset: QPoint = None

        self.ui = Ui()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon("icon.ico"))

        self.clicked_connect_to_control_window_buttons()

        self.builder = Builder(self.ui)
        self.builder.build()

    def clicked_connect_to_control_window_buttons(self) -> None:
        self.ui.clouseBT.clicked.connect(self.close)
        self.ui.minBT.clicked.connect(self.showMinimized)
        self.ui.maxBT.clicked.connect(self.change_size)

    def change_size(self) -> None:
        if self.maximize_flag:
            self.showNormal()
            self.maximize_flag = False
        else:
            self.showMaximized()
            self.maximize_flag = True

    def mouseMoveEvent(self, event: QMouseEvent) -> None:  # noqa: N802
        if self.moving_flag and not self.maximize_flag and event.position().y() < 55:
            self.move(event.globalPosition().toPoint() - self.offset)

    def mousePressEvent(self, event: QMouseEvent) -> None:  # noqa: N802
        if event.button() == Qt.LeftButton:
            self.moving_flag = True
            self.offset = event.position().toPoint()
