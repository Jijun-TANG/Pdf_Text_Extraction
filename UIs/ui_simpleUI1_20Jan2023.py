# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simpleUI1_20Jan2023.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(390, 529)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 220, 171, 41))
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.BrowseButton = QPushButton(Widget)
        self.BrowseButton.setObjectName(u"BrowseButton")
        self.BrowseButton.setGeometry(QRect(210, 240, 161, 31))
        self.ExtractTextButton = QPushButton(Widget)
        self.ExtractTextButton.setObjectName(u"ExtractTextButton")
        self.ExtractTextButton.setGeometry(QRect(210, 360, 161, 41))
        self.CancelButton = QPushButton(Widget)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(120, 470, 121, 41))
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 420, 351, 31))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(Widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 280, 351, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.changeSaveLocationButton = QPushButton(Widget)
        self.changeSaveLocationButton.setObjectName(u"changeSaveLocationButton")
        self.changeSaveLocationButton.setGeometry(QRect(20, 360, 151, 41))
        self.logoLabel1 = QLabel(Widget)
        self.logoLabel1.setObjectName(u"logoLabel1")
        self.logoLabel1.setGeometry(QRect(10, 10, 231, 221))
        self.logoLabel1.setPixmap(QPixmap(u"../logo_format_jpg.jpg"))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Choose Files (.pdf) :", None))
        self.BrowseButton.setText(QCoreApplication.translate("Widget", u"Browse...", None))
        self.ExtractTextButton.setText(QCoreApplication.translate("Widget", u"Extract text", None))
        self.CancelButton.setText(QCoreApplication.translate("Widget", u"Cancel Quit", None))
        self.changeSaveLocationButton.setText(QCoreApplication.translate("Widget", u"Change Save Location", None))
        self.logoLabel1.setText("")
    # retranslateUi

