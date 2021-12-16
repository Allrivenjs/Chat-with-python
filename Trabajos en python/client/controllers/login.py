from PySide2.QtWidgets import QWidget
from views.login import LoginForm

from pys2_msgboxes import msgboxes

class LoginWindow(QWidget, LoginForm):
    
    #creamos su constructor
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.joinButton.clicked.connect(self.join_to_chat)#cuando se presione el boton de conectar mandara la funcion
    #mandamos el username del usuario que se quire conectar al chat
    def join_to_chat(self):
        username = self.usernameLineEdit.text()
        #verificamos que no este el input vacio, y iniciamos la otra ventana
        if username != '':
            from controllers.chat import ChatWindow
            self.chat_window = ChatWindow(username) #pasamos por parametro el username
            self.chat_window.show() #mostramos la ventana
            self.close() #cerramos esta ventana
        else:
            msgboxes.input_error_msgbox('Dato requerido', 'Debe introducir un username') #si no pasas un nombre mostrara este mensaje
