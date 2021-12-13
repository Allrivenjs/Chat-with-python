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


class loginForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(316, 242)
        Form.setMinimumSize(QSize(0, 242))
        Form.setStyleSheet(u"background-color: #2980b9;")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 316, 80))
        self.frame.setStyleSheet(u"background-color: #3498db;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 221, 41))
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 130, 81, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white;")
        self.usernameLineEdit = QLineEdit(Form)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(120, 120, 181, 36))
        self.joinButton = QPushButton(Form)
        self.joinButton.setObjectName(u"joinButton")
        self.joinButton.setGeometry(QRect(100, 190, 95, 36))
        self.joinButton.setFont(font)
        self.joinButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #2ecc71;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #27ae60;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; vertical-align:sub;\">Python Chat</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nickname</span></p></body></html>", None))
        self.joinButton.setText(QCoreApplication.translate("Form", u"Iniciar", None))
    # retranslateUi

