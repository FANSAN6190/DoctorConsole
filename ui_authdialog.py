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
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(678, 525)
        self.login = QPushButton(Dialog)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(220, 330, 89, 25))
        self.regist = QPushButton(Dialog)
        self.regist.setObjectName(u"regist")
        self.regist.setGeometry(QRect(360, 330, 89, 25))
        self.phone_no = QLineEdit(Dialog)
        self.phone_no.setObjectName(u"phone_no")
        self.phone_no.setGeometry(QRect(230, 120, 221, 25))
        self.password = QLineEdit(Dialog)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(230, 190, 221, 25))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.regist.setText(QCoreApplication.translate("Dialog", u"Register", None))
    # retranslateUi

