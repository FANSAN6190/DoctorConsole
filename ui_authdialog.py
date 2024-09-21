# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(721, 536)
        self.login = QPushButton(Dialog)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(200, 320, 131, 41))
        self.regist = QPushButton(Dialog)
        self.regist.setObjectName(u"regist")
        self.regist.setGeometry(QRect(410, 320, 121, 41))
        self.password = QLineEdit(Dialog)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(190, 200, 396, 25))
        self.phone_no = QLineEdit(Dialog)
        self.phone_no.setObjectName(u"phone_no")
        self.phone_no.setGeometry(QRect(190, 120, 396, 25))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 200, 65, 29))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 120, 67, 29))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.regist.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Phone No", None))
    # retranslateUi

