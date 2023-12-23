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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1172, 888)
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
        self.horizontalFrame = QFrame(self.header)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(110, 40))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 35))
        self.horizontalFrame.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, -1, -1)
        self.label = QLabel(self.horizontalFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.minBT = QPushButton(self.horizontalFrame)
        self.minBT.setObjectName(u"minBT")
        self.minBT.setMinimumSize(QSize(30, 30))
        self.minBT.setMaximumSize(QSize(30, 30))
        self.minBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.minBT.setStyleSheet(u"border: rgb(0, 0, 0);\n"
"background-color: rgb(236, 236, 0);\n"
"border-radius: 15")

        self.horizontalLayout.addWidget(self.minBT)

        self.maxBT = QPushButton(self.horizontalFrame)
        self.maxBT.setObjectName(u"maxBT")
        self.maxBT.setMinimumSize(QSize(30, 30))
        self.maxBT.setMaximumSize(QSize(30, 16777215))
        self.maxBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.maxBT.setStyleSheet(u"border: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius: 15")

        self.horizontalLayout.addWidget(self.maxBT)

        self.clouseBT = QPushButton(self.horizontalFrame)
        self.clouseBT.setObjectName(u"clouseBT")
        self.clouseBT.setMinimumSize(QSize(30, 30))
        self.clouseBT.setMaximumSize(QSize(30, 16777215))
        self.clouseBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.clouseBT.setStyleSheet(u"border: rgb(255, 255, 255);\n"
"background-color: rgb(218, 0, 0);\n"
"border-radius: 15")

        self.horizontalLayout.addWidget(self.clouseBT)


        self.horizontalLayout_3.addWidget(self.horizontalFrame)


        self.verticalLayout_3.addWidget(self.header)

        self.main = QFrame(self.verticalFrame)
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(0, 800))
        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(260, 0, 881, 781))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.itemL = QLabel(self.page)
        self.itemL.setObjectName(u"itemL")
        self.itemL.setGeometry(QRect(10, -5, 161, 31))
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(560, -5, 131, 31))
        self.list_booksLW = QListWidget(self.page)
        self.list_booksLW.setObjectName(u"list_booksLW")
        self.list_booksLW.setGeometry(QRect(0, 30, 871, 751))
        self.list_booksLW.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_booksLW.setAutoScroll(False)
        self.list_booksLW.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.list_booksLW.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.list_booksLW.setMovement(QListView.Static)
        self.list_booksLW.setFlow(QListView.LeftToRight)
        self.list_booksLW.setProperty("isWrapping", True)
        self.list_booksLW.setViewMode(QListView.IconMode)
        self.list_booksLW.setUniformItemSizes(True)
        self.list_booksLW.setBatchSize(3)
        self.list_booksLW.setWordWrap(True)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 131, 31))
        self.stackedWidget.addWidget(self.page_2)
        self.treeWidget = QTreeWidget(self.main)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem6 = QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem7)
        __qtreewidgetitem8 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem9 = QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem9)
        QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10 = QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem11 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem12 = QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem12)
        QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem13 = QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem13)
        QTreeWidgetItem(__qtreewidgetitem13)
        __qtreewidgetitem14 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem15 = QTreeWidgetItem(__qtreewidgetitem14)
        QTreeWidgetItem(__qtreewidgetitem15)
        QTreeWidgetItem(__qtreewidgetitem15)
        __qtreewidgetitem16 = QTreeWidgetItem(__qtreewidgetitem14)
        QTreeWidgetItem(__qtreewidgetitem16)
        QTreeWidgetItem(__qtreewidgetitem16)
        __qtreewidgetitem17 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem18 = QTreeWidgetItem(__qtreewidgetitem17)
        QTreeWidgetItem(__qtreewidgetitem18)
        QTreeWidgetItem(__qtreewidgetitem18)
        __qtreewidgetitem19 = QTreeWidgetItem(__qtreewidgetitem17)
        QTreeWidgetItem(__qtreewidgetitem19)
        QTreeWidgetItem(__qtreewidgetitem19)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(5, 0, 251, 781))
        self.treeWidget.header().setVisible(False)

        self.verticalLayout_3.addWidget(self.main)


        self.verticalLayout_4.addWidget(self.verticalFrame)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0432 \u0428\u043a\u043e\u043b\u0435 \u2116103", None))
        self.minBT.setText("")
        self.maxBT.setText("")
        self.clouseBT.setText("")
        self.itemL.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u044f", None))

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"5 \u043a\u043b\u0430\u0441\u0441", None));
        ___qtreewidgetitem1 = ___qtreewidgetitem.child(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem4 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"6 \u043a\u043b\u0430\u0441\u0441", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem5.child(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem8 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"7 \u043a\u043b\u0430\u0441\u0441", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem8.child(0)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u0435\u0431\u0440\u0430", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem9.child(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem9.child(1)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem8.child(1)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u044f", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem12.child(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem12.child(1)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem15 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"8 \u043a\u043b\u0430\u0441\u0441", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem15.child(0)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u0435\u0431\u0440\u0430", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem16.child(1)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem15.child(1)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u044f", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem19.child(0)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem19.child(1)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem22 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"9 \u043a\u043b\u0430\u0441\u0441", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u0435\u0431\u0440\u0430", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem23.child(0)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem23.child(1)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem22.child(1)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u044f", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem26.child(0)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem26.child(1)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem29 = self.treeWidget.topLevelItem(5)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"10 \u043a\u043b\u0430\u0441\u0441", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem29.child(0)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u0435\u0431\u0440\u0430", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem30.child(0)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem30.child(1)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem29.child(1)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u044f", None));
        ___qtreewidgetitem34 = ___qtreewidgetitem33.child(0)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem35 = ___qtreewidgetitem33.child(1)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem36 = self.treeWidget.topLevelItem(6)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("MainWindow", u"11 \u043a\u043b\u0430\u0441\u0441", None));
        ___qtreewidgetitem37 = ___qtreewidgetitem36.child(0)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u0435\u0431\u0440\u0430", None));
        ___qtreewidgetitem38 = ___qtreewidgetitem37.child(0)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem39 = ___qtreewidgetitem37.child(1)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem40 = ___qtreewidgetitem36.child(1)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u044f", None));
        ___qtreewidgetitem41 = ___qtreewidgetitem40.child(0)
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        ___qtreewidgetitem42 = ___qtreewidgetitem40.child(1)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043b\u0443\u0431\u043b\u0451\u043d\u043d\u044b\u0439 \u043a\u0443\u0440\u0441", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

