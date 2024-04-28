# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datatable_replace.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DatatableReplace(object):
    def setupUi(self, DatatableReplace):
        if not DatatableReplace.objectName():
            DatatableReplace.setObjectName(u"DatatableReplace")
        DatatableReplace.resize(800, 600)
        self.centralwidget = QWidget(DatatableReplace)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.tw_data = QTableWidget(self.centralwidget)
        self.tw_data.setObjectName(u"tw_data")
        self.tw_data.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.verticalLayout.addWidget(self.tw_data)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        DatatableReplace.setCentralWidget(self.centralwidget)

        self.retranslateUi(DatatableReplace)
        self.pushButton.clicked.connect(DatatableReplace.close)
        self.pushButton_2.clicked.connect(DatatableReplace.fn_apply)

        QMetaObject.connectSlotsByName(DatatableReplace)
    # setupUi

    def retranslateUi(self, DatatableReplace):
        DatatableReplace.setWindowTitle(QCoreApplication.translate("DatatableReplace", u"DataTable Replace", None))
        self.pushButton_2.setText(QCoreApplication.translate("DatatableReplace", u"Apply", None))
        self.pushButton.setText(QCoreApplication.translate("DatatableReplace", u"Close", None))
    # retranslateUi

