# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_replace.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SimpleReplace(object):
    def setupUi(self, SimpleReplace):
        if not SimpleReplace.objectName():
            SimpleReplace.setObjectName(u"SimpleReplace")
        SimpleReplace.resize(300, 130)
        self.centralwidget = QWidget(SimpleReplace)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.label)

        self.cb_item = QComboBox(self.centralwidget)
        self.cb_item.addItem("")
        self.cb_item.addItem("")
        self.cb_item.addItem("")
        self.cb_item.setObjectName(u"cb_item")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_item.sizePolicy().hasHeightForWidth())
        self.cb_item.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.cb_item)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_value = QLineEdit(self.centralwidget)
        self.le_value.setObjectName(u"le_value")

        self.horizontalLayout_2.addWidget(self.le_value)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        SimpleReplace.setCentralWidget(self.centralwidget)

        self.retranslateUi(SimpleReplace)
        self.pushButton.clicked.connect(SimpleReplace.fn_apply)
        self.pushButton_2.clicked.connect(SimpleReplace.close)
        self.cb_item.currentTextChanged.connect(SimpleReplace.on_item_changed)
        self.le_value.textEdited.connect(SimpleReplace.on_value_changed)

        QMetaObject.connectSlotsByName(SimpleReplace)
    # setupUi

    def retranslateUi(self, SimpleReplace):
        SimpleReplace.setWindowTitle(QCoreApplication.translate("SimpleReplace", u"Simple Replace", None))
        self.label.setText(QCoreApplication.translate("SimpleReplace", u"Item", None))
        self.cb_item.setItemText(0, QCoreApplication.translate("SimpleReplace", u"item1", None))
        self.cb_item.setItemText(1, QCoreApplication.translate("SimpleReplace", u"item2", None))
        self.cb_item.setItemText(2, QCoreApplication.translate("SimpleReplace", u"item3", None))

        self.label_2.setText(QCoreApplication.translate("SimpleReplace", u"Value", None))
        self.pushButton.setText(QCoreApplication.translate("SimpleReplace", u"Apply", None))
        self.pushButton_2.setText(QCoreApplication.translate("SimpleReplace", u"Close", None))
    # retranslateUi

