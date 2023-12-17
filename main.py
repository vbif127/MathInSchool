import sys

from PySide6.QtWidgets import QApplication
from app import MathInSchool


def main():
    app = QApplication(sys.argv)
    window = MathInSchool()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
