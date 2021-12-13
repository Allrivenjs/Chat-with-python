# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class LoginForm(object):
    def setupUi(self, loginForm):
        if not loginForm.objectName():
            loginForm.setObjectName(u"loginForm")
        loginForm.resize(480, 278)
        loginForm.setStyleSheet(u"background-color: #FEFCFB;")
        self.frame = QFrame(loginForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 481, 81))
        self.frame.setStyleSheet(u"background-color: #3498db;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 191, 51))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label_2 = QLabel(loginForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 120, 121, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.usernameLineEdit = QLineEdit(loginForm)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(150, 120, 301, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.usernameLineEdit.setFont(font2)
        self.joinButton = QPushButton(loginForm)
        self.joinButton.setObjectName(u"joinButton")
        self.joinButton.setGeometry(QRect(170, 200, 121, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.joinButton.setFont(font3)
        self.joinButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #2ecc71;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #27ae60;\n"
"}")

        self.retranslateUi(loginForm)

        QMetaObject.connectSlotsByName(loginForm)
    # setupUi

    def retranslateUi(self, loginForm):
        loginForm.setWindowTitle(QCoreApplication.translate("loginForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("loginForm", u"Python Chat", None))
        self.label_2.setText(QCoreApplication.translate("loginForm", u"NICKNAME: ", None))
        self.joinButton.setText(QCoreApplication.translate("loginForm", u"LOGIN", None))
    # retranslateUi

