from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.chat import ChatForm
from controllers.login import LoginWindow

import socket
import threading

#creamos la clase y pasamos por parametros las dos clases importadas
class ChatWindow(QWidget, ChatForm):

#creamos el constructor y pasamos por parametros el username
    def __init__(self, username):
        #llamos el contructor de la clase padre del Qwidget
        super().__init()
        #almacenamos el username
        self.username = username
        #construimos la interfaz
        self.setupUi(self)

        #creamos la conexion
        self.connect()

        #conectamos el boton de enviar con el texto a enviar
        self.sendButton.clicked.connect(self.send_messages())

    #creamos la conexion
    def connect(self):
        connection_data = ('127.0.0.1', 55555)

    #Creamos el socket de conexion
        af_inet = socket.AF_INET
        sock_stream = socket.SOCK_STREAM
        self.client = socket.socket(af_inet,sock_stream)
        self.client.connect(connection_data)

    #creamos los thread para cada cliente
        receive_thread = threading.Thread(target=self.receive_messages)
        #cerramos el hilo cuando se cierra la apliacion
        receive_thread.daemon = True
        receive_thread.start()
    #enviamos el username
        self.client.send(self.username.encode('utf-8'))


    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.client.close()
        self.close()

## aqui obtenemos los mensajes que llegan al servidor
    def receive_messages(self):
        while(True):
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.chatTextEdit.append(message)
                self.chatTextEdit.setAlignment(Qt.AlignLeft)
            except:
                self.client.close()
                break

    def send_messages(self):
        #obtenemos el mensaje
        message = self.messageLineEdit.text()
        #le damos formato
        message = f"{self.username}: {message}"
        self.client.send(message.encode('utf-8'))
        self.chatTextEdit.append(message)
        self.messageLineEdit.clear()