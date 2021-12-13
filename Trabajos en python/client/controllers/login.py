from PySide2.QtWidgest import QWidget
from views.login import loginForm
from pys2_msgboxes import msgboxes

class LoginWindow(QWidget, loginForm):

#creamos su constructor
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def join_to_chat(self):
        username = self.usernameLineEdit.text()

        if username != '':
            from controllers.chat import ChatWindow
            self.chat_window = ChatWindow()
            self.chat_window.show()
            self.close()
        else:
            msgboxes.input_error_msgbox('Dato requerido', 'Debe introducir un username')