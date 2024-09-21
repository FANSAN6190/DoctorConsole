# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"background:rgb(225, 245, 254);")
        self.actionPriscription = QAction(MainWindow)
        self.actionPriscription.setObjectName(u"actionPriscription")
        self.actionPatient_Details = QAction(MainWindow)
        self.actionPatient_Details.setObjectName(u"actionPatient_Details")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(0, 0, 401, 1031))
        self.verticalWidget.setStyleSheet(u"border-right: 2px solid black; background:rgb(207, 212, 233);")
        self.patientDetails = QGroupBox(self.verticalWidget)
        self.patientDetails.setObjectName(u"patientDetails")
        self.patientDetails.setGeometry(QRect(10, 350, 381, 621))
        self.patientDetails.setStyleSheet(u"background:rgb(222, 221, 218);")
        self.verticalLayout_2 = QVBoxLayout(self.patientDetails)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imageSection = QWidget(self.patientDetails)
        self.imageSection.setObjectName(u"imageSection")
        self.imageSection.setStyleSheet(u"border-right:none;")

        self.verticalLayout_2.addWidget(self.imageSection)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textDetails = QLabel(self.patientDetails)
        self.textDetails.setObjectName(u"textDetails")
        self.textDetails.setStyleSheet(u"border-right:none;")

        self.verticalLayout.addWidget(self.textDetails)

        self.medHistory = QPushButton(self.patientDetails)
        self.medHistory.setObjectName(u"medHistory")
        self.medHistory.setStyleSheet(u"margin: 20px")

        self.verticalLayout.addWidget(self.medHistory)

        self.newPriscrip = QPushButton(self.patientDetails)
        self.newPriscrip.setObjectName(u"newPriscrip")
        self.newPriscrip.setStyleSheet(u"margin: 20px")

        self.verticalLayout.addWidget(self.newPriscrip)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.searchInput = QLineEdit(self.verticalWidget)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setGeometry(QRect(10, 50, 281, 31))
        self.searchButton = QPushButton(self.verticalWidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(300, 50, 89, 31))
        self.searchLabel = QLabel(self.verticalWidget)
        self.searchLabel.setObjectName(u"searchLabel")
        self.searchLabel.setGeometry(QRect(10, 20, 251, 21))
        self.searchLabel.setStyleSheet(u"border-right:none;")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(410, 10, 1491, 1021))
        self.stackedWidget.setStyleSheet(u"")
        self.medicalHistory = QWidget()
        self.medicalHistory.setObjectName(u"medicalHistory")
        self.widget_2 = QWidget(self.medicalHistory)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(150, 10, 1231, 961))
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(560, 30, 201, 31))
        self.label_3.setStyleSheet(u"font: 700 20pt \"Ubuntu\";")
        self.stackedWidget.addWidget(self.medicalHistory)
        self.newPriscription = QWidget()
        self.newPriscription.setObjectName(u"newPriscription")
        self.widget_3 = QWidget(self.newPriscription)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(150, 10, 1231, 961))
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(560, 30, 221, 31))
        self.label_4.setStyleSheet(u"font: 700 20pt \"Ubuntu\";")
        self.stackedWidget.addWidget(self.newPriscription)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        self.menubar.setStyleSheet(u"background:rgb(157, 158, 168);")
        self.menuHome = QMenu(self.menubar)
        self.menuHome.setObjectName(u"menuHome")
        self.menuNew = QMenu(self.menubar)
        self.menuNew.setObjectName(u"menuNew")
        self.menuGet = QMenu(self.menubar)
        self.menuGet.setObjectName(u"menuGet")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuGet.menuAction())
        self.menuNew.addAction(self.actionPriscription)
        self.menuGet.addAction(self.actionPatient_Details)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionPriscription.setText(QCoreApplication.translate("MainWindow", u"Priscription", None))
        self.actionPatient_Details.setText(QCoreApplication.translate("MainWindow", u"Patient Details", None))
        self.patientDetails.setTitle(QCoreApplication.translate("MainWindow", u"Patient Details", None))
        self.textDetails.setText("")
        self.medHistory.setText(QCoreApplication.translate("MainWindow", u"View Medical History", None))
        self.newPriscrip.setText(QCoreApplication.translate("MainWindow", u"Create New Prescription", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.searchLabel.setText(QCoreApplication.translate("MainWindow", u"Search Patient by Email ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Medical History", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"New Priscription", None))
        self.menuHome.setTitle(QCoreApplication.translate("MainWindow", u"Home", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New", None))
        self.menuGet.setTitle(QCoreApplication.translate("MainWindow", u"Get", None))
    # retranslateUi

