# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QCheckBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextBrowser, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1546, 917)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"#verticalFrame {\n"
"	border: 2px solid rgb(186, 186, 186);\n"
"	border-radius: 50;\n"
"	background-color: rgb(236, 236, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 89, 208, 255), stop:0.511364 rgba(203, 148, 203, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"* {\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 140);\n"
"	border: 1.5px solid rgba(26, 118, 255, 100);\n"
"	border-radius: 8px;\n"
"	padding-bottom: 3.5px;\n"
"}\n"
"QPushButton:enabled:hover:!pressed{\n"
"	background-color: rgb(155, 192, 253);\n"
"	border: 1.5px solid rgba(26, 118, 255, 100);\n"
"	border-bottom: 1.5px rgba(26, 118, 255, 100);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:enabled:pressed{\n"
"	background-color: rgba(161, 136, 204, 190);\n"
"	border: 1.5px solid rgba(169, 156, 214, 170);\n"
"	border-radius: 8px;\n"
"	color: rgb(236, 236, 236);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.header = QFrame(self.verticalFrame)
        self.header.setObjectName(u"header")
        self.header.setCursor(QCursor(Qt.SizeAllCursor))
        self.header.setStyleSheet(u"#header{\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 7)
        self.horizontalFrame = QFrame(self.header)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(110, 40))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 70))
        self.horizontalFrame.setStyleSheet(u"border-radius:8px")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, -1, -1)
        self.icon = QLabel(self.horizontalFrame)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(50, 50))
        self.icon.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.icon)

        self.label = QLabel(self.horizontalFrame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(310, 16777215))
        self.label.setStyleSheet(u"padding-left:15px;\n"
"padding-right:15px;\n"
"padding-bottom:5px;\n"
"margin-bottom:5px;\n"
"background-color: rgba(255, 255, 255, 20);")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.minBT = QPushButton(self.horizontalFrame)
        self.minBT.setObjectName(u"minBT")
        self.minBT.setMinimumSize(QSize(30, 30))
        self.minBT.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.minBT.setFont(font)
        self.minBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.minBT.setStyleSheet(u"border: rgb(0, 0, 0);\n"
"background-color:rgb(255, 217, 3);\n"
"border-radius: 15;\n"
"color: \"#fff\";\n"
"font: 26pt \"Consolas\";\n"
"padding-bottom: 4.8;")

        self.horizontalLayout.addWidget(self.minBT)

        self.maxBT = QPushButton(self.horizontalFrame)
        self.maxBT.setObjectName(u"maxBT")
        self.maxBT.setMinimumSize(QSize(30, 30))
        self.maxBT.setMaximumSize(QSize(30, 16777215))
        self.maxBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.maxBT.setStyleSheet(u"border: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius: 15;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Consolas\";\n"
"padding-bottom: 1.5px")
        self.maxBT.setFlat(False)

        self.horizontalLayout.addWidget(self.maxBT)

        self.clouseBT = QPushButton(self.horizontalFrame)
        self.clouseBT.setObjectName(u"clouseBT")
        self.clouseBT.setMinimumSize(QSize(30, 30))
        self.clouseBT.setMaximumSize(QSize(30, 16777215))
        self.clouseBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.clouseBT.setStyleSheet(u"border: rgb(255, 255, 255);\n"
"background-color: rgb(218, 0, 0);\n"
"border-radius: 15;\n"
"padding-bottom: 1.8;\n"
"font: 16pt \"Consolas\";\n"
"color: #fff")

        self.horizontalLayout.addWidget(self.clouseBT)


        self.horizontalLayout_3.addWidget(self.horizontalFrame)


        self.verticalLayout_3.addWidget(self.header)

        self.main = QFrame(self.verticalFrame)
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(0, 800))
        self.main.setStyleSheet(u"")
        self.stackedWidget_2 = QStackedWidget(self.main)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(10, 0, 1521, 791))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"border-radius:8px;\n"
"border: 2px solid rgba(255, 255, 255, 100);")
        self.horizontalLayout_7 = QHBoxLayout(self.page_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.treeWidget = QTreeWidget(self.page_3)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setStyleSheet(u"border-radius:8px;\n"
"border: 2px solid rgba(255, 255, 255, 100);")
        self.treeWidget.header().setVisible(False)

        self.verticalLayout_5.addWidget(self.treeWidget)

        self.aboutB = QPushButton(self.page_3)
        self.aboutB.setObjectName(u"aboutB")
        self.aboutB.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 140);\n"
"	border: 1.5px solid rgba(26, 118, 255, 100);\n"
"	border-radius: 8px;\n"
"	padding-bottom: 3.5px;\n"
"}\n"
"QPushButton:enabled:hover:!pressed{\n"
"	background-color: rgb(155, 192, 253);\n"
"	border: 1.5px solid rgba(26, 118, 255, 100);\n"
"	border-bottom: 1.5px rgba(26, 118, 255, 100);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:enabled:pressed{\n"
"	background-color: rgba(161, 136, 204, 190);\n"
"	border: 1.5px solid rgba(169, 156, 214, 170);\n"
"	border-radius: 8px;\n"
"	color: rgb(236, 236, 236);\n"
"}")

        self.verticalLayout_5.addWidget(self.aboutB)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.sadasFV = QFrame(self.page_3)
        self.sadasFV.setObjectName(u"sadasFV")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(70)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sadasFV.sizePolicy().hasHeightForWidth())
        self.sadasFV.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.sadasFV)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.itemL = QLabel(self.sadasFV)
        self.itemL.setObjectName(u"itemL")
        self.itemL.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.itemL)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.list_booksLW = QListWidget(self.sadasFV)
        self.list_booksLW.setObjectName(u"list_booksLW")
        self.list_booksLW.setStyleSheet(u"*{\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgba(255, 255, 255, 200);\n"
"}\n"
"QListWidget:item:hover{\n"
"	border: 3.5px solid rgba(120, 142, 216, 180);\n"
"	border-radius: 10px;\n"
"}\n"
"QPlainTextEdit {\n"
"	border: 2px solid rgba(158, 158, 158, 150);\n"
"	border-radius: 0px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	margin-right: 15px;\n"
"	margin-left: 15px;\n"
"}\n"
"")
        self.list_booksLW.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_booksLW.setAutoScroll(False)
        self.list_booksLW.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.list_booksLW.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.list_booksLW.setMovement(QListView.Static)
        self.list_booksLW.setFlow(QListView.LeftToRight)
        self.list_booksLW.setProperty("isWrapping", True)
        self.list_booksLW.setResizeMode(QListView.Fixed)
        self.list_booksLW.setLayoutMode(QListView.SinglePass)
        self.list_booksLW.setGridSize(QSize(185, 340))
        self.list_booksLW.setViewMode(QListView.IconMode)
        self.list_booksLW.setUniformItemSizes(False)
        self.list_booksLW.setBatchSize(4)
        self.list_booksLW.setWordWrap(True)
        self.list_booksLW.setSelectionRectVisible(True)

        self.verticalLayout_6.addWidget(self.list_booksLW)


        self.horizontalLayout_7.addWidget(self.sadasFV)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_5 = QHBoxLayout(self.page_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_4)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(15)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.book_imgL = QLabel(self.frame)
        self.book_imgL.setObjectName(u"book_imgL")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(65)
        sizePolicy3.setHeightForWidth(self.book_imgL.sizePolicy().hasHeightForWidth())
        self.book_imgL.setSizePolicy(sizePolicy3)
        self.book_imgL.setStyleSheet(u"border-radius: 18px;")

        self.verticalLayout_2.addWidget(self.book_imgL)

        self.book_description = QPlainTextEdit(self.frame)
        self.book_description.setObjectName(u"book_description")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(34)
        sizePolicy4.setHeightForWidth(self.book_description.sizePolicy().hasHeightForWidth())
        self.book_description.setSizePolicy(sizePolicy4)
        self.book_description.setStyleSheet(u"")
        self.book_description.setFrameShape(QFrame.StyledPanel)
        self.book_description.setFrameShadow(QFrame.Sunken)
        self.book_description.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.book_description.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.book_description)

        self.verticalSpacer = QSpacerItem(20, 240, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addWidget(self.frame)

        self.gdfgdfFV = QFrame(self.page_4)
        self.gdfgdfFV.setObjectName(u"gdfgdfFV")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(60)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.gdfgdfFV.sizePolicy().hasHeightForWidth())
        self.gdfgdfFV.setSizePolicy(sizePolicy5)
        self.verticalLayout_7 = QVBoxLayout(self.gdfgdfFV)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.asdsF = QFrame(self.gdfgdfFV)
        self.asdsF.setObjectName(u"asdsF")
        self.asdsF.setStyleSheet(u"*{\n"
"	background-color: rgba(255, 255, 255, 85);\n"
"	border-radius:13px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 140);\n"
"	border: 1.5px solid rgba(26, 118, 255, 100);\n"
"	border-radius: 8px;\n"
"	padding-bottom: 3.5px;\n"
"}\n"
"QPushButton:enabled:hover:!pressed{\n"
"	background-color: rgb(155, 192, 253);\n"
"	border: 1.5px solid rgba(26, 118, 255, 100);\n"
"	border-bottom: 1.5px rgba(26, 118, 255, 100);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:enabled:pressed{\n"
"	background-color: rgba(161, 136, 204, 190);\n"
"	border: 1.5px solid rgba(169, 156, 214, 170);\n"
"	border-radius: 8px;\n"
"	color: rgb(236, 236, 236);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.asdsF)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.backPB = QPushButton(self.asdsF)
        self.backPB.setObjectName(u"backPB")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(10)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.backPB.sizePolicy().hasHeightForWidth())
        self.backPB.setSizePolicy(sizePolicy6)
        self.backPB.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.backPB.setFont(font1)
        self.backPB.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.backPB)

        self.paragraphsPB = QPushButton(self.asdsF)
        self.btG = QButtonGroup(MainWindow)
        self.btG.setObjectName(u"btG")
        self.btG.addButton(self.paragraphsPB)
        self.paragraphsPB.setObjectName(u"paragraphsPB")
        self.paragraphsPB.setEnabled(False)
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(35)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.paragraphsPB.sizePolicy().hasHeightForWidth())
        self.paragraphsPB.setSizePolicy(sizePolicy7)
        self.paragraphsPB.setMinimumSize(QSize(0, 35))
        self.paragraphsPB.setStyleSheet(u"QPushButton:checked{\n"
"	color:rgb(150, 150, 150)\n"
"}")
        self.paragraphsPB.setCheckable(True)
        self.paragraphsPB.setChecked(True)

        self.horizontalLayout_2.addWidget(self.paragraphsPB)

        self.numbersPB = QPushButton(self.asdsF)
        self.btG.addButton(self.numbersPB)
        self.numbersPB.setObjectName(u"numbersPB")
        sizePolicy7.setHeightForWidth(self.numbersPB.sizePolicy().hasHeightForWidth())
        self.numbersPB.setSizePolicy(sizePolicy7)
        self.numbersPB.setMinimumSize(QSize(0, 35))
        self.numbersPB.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.numbersPB)


        self.verticalLayout_7.addWidget(self.asdsF)

        self.searchLE = QLineEdit(self.gdfgdfFV)
        self.searchLE.setObjectName(u"searchLE")
        self.searchLE.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.searchLE)

        self.tsdada = QFrame(self.gdfgdfFV)
        self.tsdada.setObjectName(u"tsdada")
        self.tsdada.setStyleSheet(u"*{\n"
"border-radius: 8px;\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.tsdada)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.videoCB = QCheckBox(self.tsdada)
        self.videoCB.setObjectName(u"videoCB")
        sizePolicy7.setHeightForWidth(self.videoCB.sizePolicy().hasHeightForWidth())
        self.videoCB.setSizePolicy(sizePolicy7)
        self.videoCB.setLayoutDirection(Qt.RightToLeft)
        self.videoCB.setStyleSheet(u"*{\n"
"padding-right: 15px;\n"
"}\n"
"QCheckBox::indicator{\n"
"	border: 0.5px solid;\n"
"	border-color:  rgba(0, 0, 0, 160);\n"
"	border-radius:8px;\n"
"	height: 20px;\n"
"	width: 20px;\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.videoCB.setTristate(False)

        self.horizontalLayout_4.addWidget(self.videoCB)

        self.answersCB = QCheckBox(self.tsdada)
        self.answersCB.setObjectName(u"answersCB")
        self.answersCB.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.answersCB.sizePolicy().hasHeightForWidth())
        self.answersCB.setSizePolicy(sizePolicy7)
        self.answersCB.setLayoutDirection(Qt.LeftToRight)
        self.answersCB.setStyleSheet(u"*{\n"
"padding-left:15px;\n"
"}\n"
"QCheckBox::indicator{\n"
"	border: 0.5px solid;\n"
"	border-color:  rgba(0, 0, 0, 160);\n"
"	border-radius:8px;\n"
"	height: 20px;\n"
"	width: 20px;\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.answersCB)


        self.verticalLayout_7.addWidget(self.tsdada)

        self.book_contentTW = QTreeWidget(self.gdfgdfFV)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.book_contentTW.setHeaderItem(__qtreewidgetitem1)
        self.book_contentTW.setObjectName(u"book_contentTW")
        self.book_contentTW.setStyleSheet(u"font: 11pt \"Consolas\";\n"
"border: 1px solid rgba(255, 255, 255, 120);\n"
"border-right: 2px solid rgba(0, 0, 0, 50);\n"
"border-bottom: 2px solid rgba(0, 0, 0, 50);\n"
"border-radius: 8px;\n"
"background-color: rgba(255, 255, 255, 140);")
        self.book_contentTW.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.book_contentTW.setIndentation(10)
        self.book_contentTW.setItemsExpandable(True)
        self.book_contentTW.setAnimated(True)
        self.book_contentTW.setAllColumnsShowFocus(False)
        self.book_contentTW.setWordWrap(False)
        self.book_contentTW.setHeaderHidden(True)

        self.verticalLayout_7.addWidget(self.book_contentTW)


        self.horizontalLayout_5.addWidget(self.gdfgdfFV)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.back2B = QPushButton(self.page)
        self.back2B.setObjectName(u"back2B")
        self.back2B.setMinimumSize(QSize(80, 40))

        self.horizontalLayout_9.addWidget(self.back2B, 0, Qt.AlignTop)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.textBrowser_2 = QTextBrowser(self.page)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setAutoFillBackground(True)

        self.horizontalLayout_8.addWidget(self.textBrowser_2)

        self.textBrowser = QTextBrowser(self.page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setAutoFillBackground(True)

        self.horizontalLayout_8.addWidget(self.textBrowser)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.stackedWidget_2.addWidget(self.page)

        self.verticalLayout_3.addWidget(self.main)


        self.verticalLayout_4.addWidget(self.verticalFrame)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.clouseBT.clicked.connect(MainWindow.close)
        self.minBT.clicked.connect(MainWindow.showMinimized)

        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0432 \u0448\u043a\u043e\u043b\u0435 \u2116103", None))
#if QT_CONFIG(tooltip)
        self.minBT.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0441\u0432\u0435\u0440\u043d\u0443\u0442\u044c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.minBT.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.maxBT.setText(QCoreApplication.translate("MainWindow", u"M", None))
#if QT_CONFIG(tooltip)
        self.clouseBT.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0417\u0430\u043a\u0440\u044b\u0442\u044c</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.clouseBT.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.aboutB.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.itemL.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.book_imgL.setText("")
        self.book_description.setPlainText("")
        self.backPB.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.paragraphsPB.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u0433\u0440\u0430\u0444\u044b", None))
        self.numbersPB.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440\u0430", None))
        self.searchLE.setText("")
        self.searchLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.videoCB.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0432\u0438\u0434\u0435\u043e", None))
        self.answersCB.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0440\u0435\u0448\u0435\u043d\u0438\u0435 (\u043e\u0442\u0432\u0435\u0442)", None))
        self.back2B.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">\u041f\u0440\u0438\u0432\u0435\u0442, \u0412\u0441\u0435\u043c \u043b\u044e\u0431\u0438\u0442\u0435\u043b\u044f\u043c \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0438!</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\""
                        ">1.\u00a0\u00a0\u00a0 \u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u0430\u044f </span><span style=\" font-size:14pt; color:#0070c0;\">\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430</span><span style=\" font-size:14pt;\"> </span><span style=\" font-size:14pt; color:#0070c0;\">\u00ab\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0432 \u0448\u043a\u043e\u043b\u0435\u00bb </span><span style=\" font-size:14pt;\">(\u0430\u043d\u0433\u043b.\u00abMath in school\u00bb),\u00a0\u00a0 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u00a0\u0441\u043e\u0431\u043e\u0439\u00a0 \u043f\u043e\u043b\u043d\u044b\u0439 \u043a\u0443\u0440\u0441\u00a0 \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0438 \u00a0\u0448\u043a\u043e\u043b\u044c\u043d\u043e\u0439 \u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u00a0\u0441 \u00a05 \u0433\u043e \u043f\u043e 11 \u043a\u043b\u0430\u0441\u0441\u044b \u00a0\u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430"
                        "\u0435\u043c\u044b\u0435 \u00a0\u00a0\u0432 \u00a0\u00a0\u041c\u0410\u041e\u0423\u00a0 \u00a0\u0448\u043a\u043e\u043b\u0435 \u00a0\u2116. 103\u0433. \u00a0\u0433. \u00a0\u041d. \u00a0\u041d\u043e\u0432\u0433\u043e\u0440\u043e\u0434 \u00a0\u00a0\u0432\u00a0 2023-2024 \u0443\u0447\u0435\u0431\u043d\u043e\u043c \u0433\u043e\u0434\u0443. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">2.\u00a0\u00a0 \u0412\u0441\u044f \u00a0\u00a0\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u00a0\u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0430\u044f\u0441\u044f \u00a0\u00a0\u0432\u00a0 \u00a0\u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 \u00a0\u0441\u043e\u0431\u0440\u0430\u043d\u0430\u00a0 \u00a0\u0438\u0437 \u00a0\u00a0\u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0445 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442 \u0440\u0435\u0441\u0443\u0440\u0441\u043e\u0432\u00a0 "
                        "\u0438 \u0441\u0438\u0441\u0442\u0435\u043c\u0430\u0442\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u0430 \u043f\u043e \u00a0\u0443\u0447\u0435\u0431\u043d\u044b\u043c \u043a\u043b\u0430\u0441\u0441\u0430\u043c, \u00a0\u00a0\u0440\u0430\u0437\u0434\u0435\u043b\u0430\u043c \u00a0\u00a0\u0441 \u0446\u0435\u043b\u044c\u044e \u00a0\u0443\u0434\u043e\u0431\u0441\u0442\u0432\u0430 \u00a0\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044e, \u00a0\u043e\u0431\u043b\u0435\u0433\u0447\u0435\u043d\u0438\u044e \u00a0\u0437\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f \u0438 \u044d\u043a\u043e\u043d\u043e\u043c\u0438\u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0438.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">3.\u00a0\u00a0 \u00ab\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0432 \u0448\u043a\u043e\u043b\u0435\u00bb \u00a0-\u00a0 \u044d\u0442\u043e \u00a0\u0447\u0438"
                        "\u0441\u0442\u043e \u00a0\u0432\u043e\u043b\u043e\u043d\u0442\u0435\u0440\u0441\u043a\u0438\u0439 \u00a0\u043f\u0440\u043e\u0434\u0443\u043a\u0442, \u00a0\u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u00a0\u00a0\u043d\u0435\u00a0 \u043f\u0440\u0435\u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u043d\u0438 \u043a\u0430\u043a\u043e\u0433\u043e \u043a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u0430. \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u00a0\u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0441\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u043d\u043e\u00a0 \u00a0\u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e\u00a0 \u00a0\u043b\u044e\u0431\u043e\u043c\u0443 \u00a0\u00a0\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e, \u00a0\u00a0\u0441\u043a\u0430\u0447\u0430\u0432\u0448\u0435\u043c\u0443 \u00a0\u00a0\u0435\u0435\u00a0\u00a0 \u043d\u0430 \u00a0\u00a0\u043b\u0438"
                        "\u0447- \u043d\u044b\u0439 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440 \u0438\u043b\u0438 \u043d\u043e\u0443\u0442\u0431\u0443\u043a.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">4.\u00a0 \u0412\u0441\u044f\u00a0 \u00a0\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u00a0\u00ab\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445\u00bb \u00a0\u00a0\u044d\u0442\u043e\u0439 \u00a0\u00a0\u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u00a0\u00a0\u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u00a0\u00a0\u043d\u0430 \u0443\u0434\u0430\u043b\u0435\u043d\u043d\u043e\u043c \u0441\u0435\u0440\u0432\u0435\u0440\u0435, \u00a0\u0447\u0442\u043e \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u043d\u0435 \u043f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0436\u0430\u0442\u044c \u043f\u0430\u043c\u044f\u0442"
                        "\u044c \u00a0\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430 \u0438 \u00a0\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u043b\u044e\u0431\u043e\u043c\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u00a0 \u0432 \u043b\u044e\u0431\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u00a0\u0441\u0443\u0442\u043e\u043a (24/7). \u00a0\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u00a0 \u00a0\u043d\u0435 \u0441\u043e\u0431\u0438\u0440\u0430\u0435\u0442 \u00a0\u043d\u0438\u043a\u0430\u043a\u0438\u0445 \u00a0\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445 \u00a0\u0438 \u00a0\u043d\u0435 \u00a0\u043e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u0435\u0442 \u043f\u043e\u043b\u044c\u0437\u043e"
                        "\u0432\u0430\u0442\u0435\u043b\u0435\u0439, \u043d\u0435 \u0442\u0440\u0435\u0431\u0443\u0435\u0442 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438, \u043d\u0435 \u0438\u043c\u0435\u0435\u0442 \u043f\u0430\u0440\u043e\u043b\u0435\u0439. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">5. \u00a0\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440 \u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u00a0\u0438 \u00a0\u0435\u0435 \u00a0\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u00a0-\u00a0 \u044d\u0442\u043e \u00a0\u043e\u0434\u043d\u043e \u0444\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043b\u0438\u0446\u043e (\u0443\u0447\u0435\u043d\u0438\u043a \u043e\u0434\u043d\u043e\u0433\u043e \u0438\u0437 \u0441\u0442\u0430\u0440\u0448\u0438\u0445 \u043a\u043b\u0430\u0441\u0441\u043e\u0432 \u0448\u043a"
                        "\u043e\u043b\u044b \u2116 103. ) \u0438:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u00a0-\u00a0 \u043d\u0438\u043a\u0430\u043a \u00a0\u043d\u0435 \u00a0\u0441\u0432\u044f\u0437\u0430\u043d\u00a0 \u0441\u00a0 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u043c\u0438 \u00a0\u0438\u043d\u0442\u0435\u043b\u043b\u0435\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0445 \u043f\u0440\u0430\u0432, \u00a0\u0438 \u00a0\u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u043d\u044b\u043c\u0438 \u00ab\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c\u0438\u00bb \u00a0\u043d\u0430 \u00a0\u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442 \u00a0\u0441\u0430\u0439\u0442\u0430\u0445; \u00a0\u00a0\u043a\u0430\u043a \u00a0\u0438 \u00a0\u043d\u0435 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0438\u043d\u0438\u0446\u0438\u0430\u0442\u043e\u0440\u043e\u043c \u0438\u0445 \u0440"
                        "\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u044f;</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u00a0- \u00a0\u043d\u0435 \u00a0\u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0435\u0442 \u00a0\u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443\u00a0 \u043f\u043e\u0434\u043b\u0438\u043d\u043d\u043e\u0441\u0442\u0438, \u00a0\u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u043c\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u00a0\u0438 \u00a0\u043d\u0430\u043b\u0438\u0447\u0438\u044f \u00a0\u0443 \u00a0\u00ab\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439\u00bb \u00a0\u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0433\u043e \u00a0\u043e\u0431\u044a\u0435\u043c\u0430 \u043f\u0440\u0430\u0432 \u043d\u0430"
                        " \u0440\u0430\u0441\u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0438\u043b\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u043a\u0438\u0445 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432;</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u00a0- \u00a0\u043d\u0435 \u00a0\u0432\u043d\u043e\u0441\u0438\u0442 \u00a0\u043a\u0430\u043a\u0438\u0445-\u043b\u0438\u0431\u043e \u00a0\u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0439 \u0432 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b, \u0440\u0430\u0437\u043c\u0435\u0449\u0430\u0435\u043c\u044b\u0435 \u00ab\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430-\u0442\u0435\u043b\u044f\u043c\u0438\u00bb \u0432 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435;</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px"
                        "; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u00a0-\u00a0 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u00a0\u043b\u0438\u0448\u044c \u00a0\u00a0\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u043c \u00a0\u043f\u043e\u0441\u0440\u0435\u0434\u043d\u0438\u043a\u043e\u043c,\u00a0 \u00a0\u0432 \u00a0\u0442\u043e\u043c \u00a0\u0441\u043c\u044b\u0441\u043b\u0435 \u00a0\u043a\u0430\u043a \u00a0\u044d\u0442\u043e \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043e \u0432 \u0441\u0442. 1253 \u00a0\u0433\u0440\u0430\u0436\u0434\u0430\u043d\u0441\u043a\u043e\u0433\u043e \u043a\u043e\u0434\u0435\u043a\u0441\u0430 \u00a0\u0420.\u0424.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- \u00a0\u0432 \u00a0\u0441\u043b\u0443\u0447\u0430\u0435 \u00a0\u00a0\u0432\u043e\u0437\u043d\u0438\u043a\u043d\u043e\u0432\u0435\u043d\u0438\u044f"
                        " \u00a0\u00a0\u043f\u0440\u0435\u0442\u0435\u043d\u0437\u0438\u0439 \u00a0\u00a0\u0441\u043e \u00a0\u0441\u0442\u043e\u0440\u043e\u043d\u044b \u00a0\u043f\u0440\u0430\u0432\u043e\u043e\u0431\u043b\u0430\u0434\u0430\u0442\u0435\u043b\u0435\u0439 \u00a0\u00a0\u0438\u043d-\u0442\u0435\u043b\u043b\u0435\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439\u00a0 \u00a0\u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0441\u0442\u0438\u00a0\u00a0 \u00a0( \u0441\u00a0 \u00a0\u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u043c\u00a0 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435\u043c\u00a0 \u00a0\u0438\u00a0\u00a0 \u00a0\u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435\u043c \u00a0\u00a0\u043f\u0440\u0435\u0442\u0435\u043d\u0437\u0438\u0438 \u00a0\u00a0\u0441\u00a0 \u00a0\u0443\u043a\u0430\u0437\u0430\u043d\u0438\u0435\u043c \u00a0\u00a0\u043d\u0430\u00a0 \u00a0\u043f\u0440\u044f\u043c\u044b\u0435\u00a0 \u0441"
                        "\u0441\u044b\u043b\u043a\u0438 \u00a0\u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u00a0\u043f\u043e\u0434\u043b\u0435\u0436\u0430\u0449\u0438\u0445 \u00a0\u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044e). \u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440 \u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u043e\u0431\u044f\u0437\u0443\u0435\u0442\u0441\u044f \u0443\u0434\u0430\u043b\u0438\u0442\u044c\u00a0 \u00a0\u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u00a0\u00a0\u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b, \u00a0\u0432 \u0442\u0435\u0447\u0435\u043d\u0438\u0435 \u00a03-\u0445 \u00a0\u0440\u0430\u0431\u043e\u0447\u0438\u0445 \u0434\u043d\u0435\u0439 \u0441 \u0434\u0430\u0442\u044b \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u043f\u0440\u0435\u0442\u0435\u043d\u0437\u0438\u0438.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- \u00a0\u0432\u0441\u0435 \u00a0\u0443\u0447\u0435\u0431\u043d\u044b\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b (\u0443\u0447\u0435\u0431\u043d\u0438\u043a\u0438 \u0438 \u0443\u0447\u0435\u0431\u043d\u044b\u0435 \u043f\u043e\u0441\u043e\u0431\u0438\u044f), \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u0432 \u0434\u0430\u043d\u043d\u043e\u0439 \u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435, \u00a0\u0438\u043c\u0435\u044e\u0442 \u00a0\u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u00a0\u0432\u0438\u0434, \u00a0\u00ab\u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u00a0 \u0440\u0430\u0437\u0440\u0435\u0437\u0430\u043d\u044b\u00bb\u00a0 \u043d\u0430 \u00a0\u00a0\u00a0\u0443\u0447\u0430\u0441\u0442\u043a\u0438\u00a0 \u00a0( \u0434\u043e \u00a0\u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a"
                        "\u0438\u0445 \u00a0\u0441\u0442\u0440\u0430\u043d\u0438\u0446 ), \u00a0\u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0442\u00a0\u00a0 \u00a0\u043d\u0435\u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e\u00a0 \u00a0\u0447\u0430\u0441\u0442\u044c\u00a0 \u0443\u0447\u0435\u0431\u043d\u043e\u0433\u043e \u00a0\u00a0\u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430, \u00a0\u00a0\u0442\u0435\u043c \u00a0\u00a0\u0441\u0430\u043c\u044b\u043c \u00a0\u00a0\u043d\u0435 \u00a0\u00a0\u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u00a0\u00a0\u0435\u0434\u0438\u043d\u044b\u043c,\u00a0 \u00a0\u043f\u043e\u043b\u043d\u043e\u0446\u0435\u043d\u043d\u044b\u043c \u0443\u0447\u0435\u0431\u043d\u044b\u043c \u043f\u043e\u0441\u043e\u0431\u0438\u0435\u043c \u0438\u043b\u0438 \u0443\u0447\u0435\u0431\u043d\u0438\u043a\u043e\u043c.</span> </p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u00a0\u00a06.\u00a0 \u00a0\u0412 \u00a0\u0434\u0430\u043d\u043d\u043e\u0439 \u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0430 \u0442\u043e\u043b\u044c\u043a\u043e \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c"
                        "\u0430\u0446\u0438\u044f \u0432\u00a0 \u00a0\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e\u043c \u00a0\u0448\u043a\u043e\u043b\u044c\u043d\u043e\u043c\u00a0 \u00a0\u043e\u0431\u044a\u0435\u043c\u0435\u00a0 (\u043f\u043e \u043c\u043d\u0435\u043d\u0438\u044e \u00a0\u0430\u0432\u0442\u043e\u0440\u0430 \u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b), \u00a0\u0447\u0442\u043e\u0431\u044b \u0441\u0434\u0430\u0442\u044c \u00a0\u0432\u0441\u0435\u00a0 \u0438\u0442\u043e\u0433\u043e\u0432\u044b\u0435 \u00a0\u0430\u0442\u0442\u0435\u0441\u0442\u0430\u0446\u0438\u0438\u00a0 \u00a0\u0438 \u00a0\u00a0\u0432\u044b\u043f\u0443\u0441\u043a\u043d\u044b\u0435 \u00a0\u044d\u043a\u0437\u0430\u043c\u0435\u043d\u044b \u00a0\u00a09 , 11\u00a0 \u043a\u043b\u0430\u0441\u0441\u043e\u0432 \u00a0\u00a0\u043f\u043e\u00a0 \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0435.\u00a0 \u0412\u0441\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432"
                        "\u043b\u0435\u043d\u0430 \u0432 \u00a0\u0444\u0430\u0439\u043b\u0430\u0445 PDF, \u00a0JPG, \u00a0PNG \u00a0\u0444\u043e\u0440\u043c\u0430-\u0442\u043e\u0432,\u00a0 \u0430 \u00a0\u0442\u0430\u043a\u0436\u0435 \u00a0\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u00a0\u043b\u0438\u0448\u044c\u00a0 \u0443\u0447\u0435\u0431\u043d\u043e-\u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0432\u0438\u0434\u0435\u043e \u0441\u0441\u044b\u043b\u043a\u0438 \u0441 \u0432\u0438\u0434\u0435\u043e \u043f\u043e\u0440\u0442\u0430\u043b\u043e\u0432\u00a0 \u042e\u0442\u0443\u0431\u0430 \u0438 \u0412\u041a \u00a0\u043e\u0442 \u0441\u0442\u043e\u0440\u043e\u043d\u043d\u0438\u0445 \u00ab\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439\u00bb.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">7. \u00a0\u00a0\u041f\u0440\u043e\u0433\u0440\u0430\u043c"
                        "\u043c\u0430\u00a0 \u00a0\u00a0\u00ab\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0432 \u0448\u043a\u043e\u043b\u0435\u00bb, \u00a0\u00a0( \u0414.\u0420.: \u0430\u043f\u0440\u0435\u043b\u044c 2024\u0433.), \u00a0\u00a0\u00a0\u043d\u0430\u00a0 \u00a0\u00a0\u043c\u043e\u043c\u0435\u043d\u0442 \u0432\u044b\u043f\u0443\u0441\u043a\u0430\u00a0 \u00a0\u043d\u0435 \u00a0\u0438\u043c\u0435\u0435\u0442 \u00a0\u043f\u043e\u043a\u0430 \u00a0\u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f. \u00a0\u0414\u043b\u044f \u0435\u0435 \u0440\u0430\u0431\u043e\u0442\u044b \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0441\u0442\u0430\u0446\u0438\u043e\u043d\u0430\u0440\u043d\u044b\u0439 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440 \u0438\u043b\u0438 \u043d\u043e\u0443\u0442\u0431\u0443\u043a ,\u00a0 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435. \u00a0"
                        "\u0418\u0437\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e \u00a0\u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u00a0 \u0437\u0430\u043d\u0438\u043c\u0430\u0435\u0442 \u00a0\u043d\u0430 \u00a0\u0436\u0435\u0441\u0442\u043a\u043e\u043c \u00a0\u0434\u0438\u0441\u043a\u0435 \u00a072 \u041c\u0431\u00a0 \u00a0\u043c\u0435\u0441\u0442\u0430\u00a0 \u043f\u0430\u043c\u044f\u0442\u0438.\u00a0 \u0412 \u00a0\u0431\u0443\u0434\u0443\u0449\u0435\u043c, \u043f\u0440\u0435\u0434\u043f\u043e\u043b\u0430\u0433\u0430\u0435\u0442\u0441\u044f \u00a0\u00a0\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u043e\u0435 \u00a0\u00a0\u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435\u00a0 \u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b\u00a0 \u00a0\u043f\u043e\u00a0 \u00a0\u043c\u0435\u0440\u0435 \u00a0\u043f\u043e\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u043d\u043e\u0432\u044b\u0445 \u00a0\u0443\u0447\u0435\u0431\u043d\u044b\u0445 \u00a0\u043f\u043e\u0441\u043e\u0431\u0438\u0439 \u00a0\u043f\u043e"
                        " \u00a0\u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0435 \u00a0\u0432 \u00a0\u0448\u043a\u043e\u043b\u044c\u043d\u043e\u0439 \u00a0\u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0435, \u00a0\u043d\u043e\u0432\u0438\u043d\u043e\u043a \u0432 \u043f\u0440\u0435\u0441\u0441\u0435 \u0438\u043b\u0438\u00a0 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0439 \u0443\u0447\u0438\u0442\u0435\u043b\u0435\u0439\u00a0 \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0438 \u0448\u043a\u043e\u043b\u044b.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">8. \u00a0\u00a0\u00a0</span><span style=\" font-size:14pt; color:#0070c0;\">\u041f\u0435\u0440\u0432\u043e\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f\u00a0 \u00a0\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430\u00a0 \u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u00a0\u00a0</s"
                        "pan><span style=\" font-size:14pt;\">\u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442\u00a0 \u00a0\u043f\u043e \u00a0\u0441\u0441\u044b\u043b\u043a\u0435 \u00a0\u0430\u0434\u043c\u0438- \u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430 \u0441 \u0441\u0430\u0439\u0442\u0430 Boosty \u00a0\u0441 \u043f\u043e\u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0439 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u043e\u0439 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0449\u0438\u043a\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u043d\u0430 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f (\u043d\u0430\u0436\u0430\u0442\u0438\u0435\u043c \u043c\u044b\u0448\u043a\u043e\u0439 \u043d\u0430 exe.\u0444\u0430\u0439\u043b ). </span><span style=\" font-size:14pt; color:#0070c0;\">\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435! \u00a0\u00a0<"
                        "/span><span style=\" font-size:14pt;\">\u0414\u043b\u044f \u00a0\u00a0\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u00a0\u00a0\u043d\u0430 \u00a0\u00a0\u0441\u0430\u0439\u0442\u0435 \u00a0\u00a0Boosty , \u00a0\u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439, \u00a0\u0437\u0430\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0435\u0442 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430\u00a0 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u0438 \u0432\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f.</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">9. \u00a0\u00a0</span><span style=\" font-size:14pt; color:#0070c0;\">\u041f\u0440\u0435\u0434\u0443\u043f\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0435 1</span><span style=\" font-size:14pt;\">. \u00a0\u0414\u0430\u043d\u043d\u0430\u044f"
                        "\u00a0 </span><span style=\" font-size:14pt; color:#0070c0;\">\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043d\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0432\u0438\u0440\u0443\u0441\u043e\u0432 </span><span style=\" font-size:14pt;\">\u0438\u043b\u0438 \u0441\u0442\u043e\u0440\u043e\u043d- \u043d\u0435\u0433\u043e \u00a0\u041f\u041e,\u00a0 \u043d\u043e \u00a0\u00a0\u0430\u043d\u0442\u0438\u0432\u0438\u0440\u0443\u0441\u043d\u044b\u0435\u00a0 \u00a0\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u00a0\u00a0\u00a0\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u00a0\u0438\u043b\u0438\u00a0 \u00a0\u0432\u0441\u0442\u0440\u043e\u0435\u043d\u043d\u044b\u0435 \u0438\u0437\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u00a0 \u043d\u0430 \u00a0\u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440 \u00a0\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u00a0\u00a0\u0432\u0441\u0435\u0433\u0434\u0430\u00a0 \u00a0\u043f\u0440\u0435"
                        "\u0434\u0443\u043f\u0440\u0435\u0436\u0434\u0430\u044e\u0442 \u00a0\u00a0\u043f\u043e\u043b\u044c\u0437\u043e- \u0432\u0430\u0442\u0435\u043b\u044f \u00a0\u043e\u0431 \u00a0\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438 \u00a0\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0441\u0442\u043e\u0440\u043e\u043d\u043d\u0435\u0433\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430. \u0417\u0430\u0433\u0440\u0443- \u0436\u0430\u0439\u0442\u0435. \u041d\u0435 \u0431\u043e\u0439\u0442\u0435\u0441\u044c!\u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">10. \u00a0\u00a0</span><span style=\" font-size:14pt; color:#0070c0;\">\u041f\u0440\u0435\u0434\u0443\u043f\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0435 2</span><span style=\" font-size:14pt;\">. \u00a0\u0418\u0437-\u0437\u0430, \u0434\u043e\u0441\u0442"
                        "\u0430\u0442\u043e\u0447\u043d\u043e \u0431\u043e\u043b\u044c\u0448\u043e\u0439\u00a0 \u0411\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445, \u00a0\u0438 \u00a0\u00a0\u043d\u0435\u0434\u043e-\u0440\u043e\u0433\u043e\u0433\u043e \u00a0\u0445\u043e\u0441\u0442\u0438\u043d\u0433\u0430 \u00a0\u0430\u0440\u0435\u043d\u0434\u044b \u00a0\u0443\u0434\u0430\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u00a0\u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u043e\u0433\u043e \u0441\u0435\u0440\u0432\u0435\u0440\u0430 (\u0431\u044e\u0434\u0436\u0435\u0442\u043d\u043e\u0433\u043e),\u00a0 \u0432 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b \u043d\u0435\u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435\u00a0 </span><span style=\" font-size:14pt; color:#0070c0;\">\u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438 \u00a0\u043f\u043e \u00a0\u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u00a0</span><span style=\" font-size:14pt;\">\u043f\u0440\u0438"
                        " \u00a0\u043f\u043e\u043b\u0443\u0447\u0435-\u043d\u0438\u0438 \u00a0\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u043c, \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e \u00a0\u043f\u0440\u0438\u00a0 \u043c\u0430\u0441\u0441\u043e\u0432\u044b\u0445 \u043e\u0434\u043d\u043e\u043c\u043e\u043c\u0435\u043d\u0442\u043d\u044b\u0445 \u0437\u0430\u043f\u0440\u043e\u0441\u0430\u0445 \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c\u0438. \u041f\u0440\u043e\u0441\u0442\u043e \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u043f\u043e\u0434\u043e\u0436\u0434\u0438\u0442\u0435.\u00a0\u00a0\u00a0\u00a0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0421 \u0443\u0432\u0430\u0436\u0435\u043d\u0438\u0435\u043c.\u00a0\u00a0\u00a0\u00a0\u00a0"
                        "\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 \u0410\u0434\u043c\u0438\u043d. \u041c\u0438\u0445\u0430\u0438\u043b.\u0411.</span> </p></body></html>", None))
    # retranslateUi

