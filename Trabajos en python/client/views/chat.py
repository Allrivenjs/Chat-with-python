# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ChatForm(object):
    def setupUi(self, chatForm):
        if not chatForm.objectName():
            chatForm.setObjectName(u"chatForm")
        chatForm.resize(860, 628)
        self.frame = QFrame(chatForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(210, 0, 451, 631))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, -10, 451, 71))
        self.frame_4.setStyleSheet(u"background-color: #3498db;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 10, 191, 61))
        font = QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:white;")
        self.chatTextEdit = QTextEdit(self.frame)
        self.chatTextEdit.setObjectName(u"chatTextEdit")
        self.chatTextEdit.setGeometry(QRect(0, 60, 451, 521))
        self.chatTextEdit.setFont(font)
        self.chatTextEdit.setStyleSheet(u"QTextEdit{\n"
"	background-color: #2980b9;\n"
"	color: white;\n"
"	border: 1px solid  white;\n"
"}")
        self.chatTextEdit.setReadOnly(True)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 579, 451, 61))
        self.frame_5.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.messageLineEdit = QLineEdit(self.frame_5)
        self.messageLineEdit.setObjectName(u"messageLineEdit")
        self.messageLineEdit.setGeometry(QRect(10, 10, 321, 31))
        font1 = QFont()
        font1.setPointSize(8)
        self.messageLineEdit.setFont(font1)
        self.sendButton = QPushButton(self.frame_5)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(340, 10, 91, 31))
        self.sendButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #2ecc71;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #27ae60;\n"
"}")
        self.frame_5.raise_()
        self.frame_4.raise_()
        self.chatTextEdit.raise_()
        self.frame_2 = QFrame(chatForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 211, 631))
        self.frame_2.setStyleSheet(u"background-color: #3498db;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 161, 71))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;")
        self.textEdit_2 = QTextEdit(self.frame_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(30, 70, 151, 261))
        self.frame_3 = QFrame(chatForm)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(659, -1, 201, 631))
        self.frame_3.setStyleSheet(u"background-color: #3498db;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.logoutButton = QPushButton(self.frame_3)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(50, 20, 91, 31))
        self.logoutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoutButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: #e74c3c;\n"
"	box-shadow: 5px 5px 15px -7px #000000;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c0392b;\n"
"}")
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(chatForm)

        QMetaObject.connectSlotsByName(chatForm)
    # setupUi

    def retranslateUi(self, chatForm):
        chatForm.setWindowTitle(QCoreApplication.translate("chatForm", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("chatForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Chat global</span></p></body></html>", None))
        self.messageLineEdit.setPlaceholderText(QCoreApplication.translate("chatForm", u"   Type something to send...", None))
        self.sendButton.setText(QCoreApplication.translate("chatForm", u"> SEND", None))
        self.label.setText(QCoreApplication.translate("chatForm", u"<html><head/><body><p align=\"center\">Usuarios Activos</p></body></html>", None))
        self.logoutButton.setText(QCoreApplication.translate("chatForm", u"Exit", None))
    # retranslateUi

