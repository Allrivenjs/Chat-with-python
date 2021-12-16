from PySide2.QtWidgets import QApplication
from controllers.login import LoginWindow
import sys


#Inicializamos las ventanas al ejecutarse el script
if __name__ == '__main__':
    app = QApplication(sys.argv) #para que funcione la ventana
    window = LoginWindow()

    window.show()
    app.exec_()