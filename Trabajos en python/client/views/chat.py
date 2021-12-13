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

import res_rc

class ChatForm(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(875, 666)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 241, 671))
        font = QFont()
        font.setFamily(u"Sans Serif Collection")
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: #3498db;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 221, 41))
        font1 = QFont()
        font1.setFamily(u"DejaVu Sans")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: white;\n"
"")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 31, 41))
        self.label_4.setStyleSheet(u"font-size: 22px;")
        self.label_4.setPixmap(QPixmap(u":/icons/iconmonstr-user-20.svg"))
        self.inLineTextEdit = QPlainTextEdit(self.frame)
        self.inLineTextEdit.setObjectName(u"inLineTextEdit")
        self.inLineTextEdit.setGeometry(QRect(20, 70, 201, 581))
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(680, 0, 211, 671))
        self.frame_2.setStyleSheet(u"background-color: #3498db;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.logoutButton = QPushButton(self.frame_2)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(60, 620, 95, 36))
        self.logoutButton.setFont(font1)
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
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(240, 0, 441, 671))
        self.frame_3.setStyleSheet(u"background-color: #3498db;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 441, 71))
        self.frame_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_4.setStyleSheet(u"background-color: #3498db;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 441, 61))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;")
        self.messageLineEdit = QLineEdit(self.frame_3)
        self.messageLineEdit.setObjectName(u"messageLineEdit")
        self.messageLineEdit.setGeometry(QRect(10, 620, 311, 41))
        self.messageLineEdit.setFont(font1)
        self.messageLineEdit.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.sendbutton = QPushButton(self.frame_3)
        self.sendbutton.setObjectName(u"sendbutton")
        self.sendbutton.setGeometry(QRect(330, 620, 101, 41))
        self.sendbutton.setFont(font1)
        self.sendbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendbutton.setStyleSheet(u"QPushButton {\n"
"	background-color: #2ecc71;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #27ae60;\n"
"}")
        self.chatTestEdit = QTextEdit(self.frame_3)
        self.chatTestEdit.setObjectName(u"chatTestEdit")
        self.chatTestEdit.setGeometry(QRect(0, 70, 441, 541))
        self.chatTestEdit.setStyleSheet(u"background-color: #2980b9;")
        self.chatTestEdit.setReadOnly(True)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 610, 441, 61))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: #000000FF;\n"
"border: 1px solid white;\n"
"")
        self.label_3.raise_()
        self.frame_4.raise_()
        self.messageLineEdit.raise_()
        self.sendbutton.raise_()
        self.chatTestEdit.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Usuarios activos</span></p></body></html>", None))
        self.label_4.setText("")
        self.logoutButton.setText(QCoreApplication.translate("Dialog", u"Exit", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Chat global</span></p></body></html>", None))
        self.messageLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type something to send...", None))
        self.sendbutton.setText(QCoreApplication.translate("Dialog", u"Send", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

