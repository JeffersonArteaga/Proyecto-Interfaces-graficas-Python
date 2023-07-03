import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from contenedores import menu_registro, ingresar_usuario, ingresar_usuario_facturas



class Menu_principal(QMainWindow):
    def __init__(self):
        super(Menu_principal,self).__init__()
        uic.loadUi("contenedores/gui/mp.ui",self)
        self.boton_registrar_usuario.clicked.connect(self.abrir_registrar_usuario)
        self.bttn_realizar_compra.clicked.connect(self.abrir_realizar_compra)
        self.bttn_mostrar_facturas.clicked.connect(self.abrir_mostrar_facturas)
        self.bttn_salir.clicked.connect(self.salir)
    
    def abrir_registrar_usuario(self):
        self.ui = menu_registro.Menu_registro()
        self.ui.show()

    def abrir_realizar_compra(self):
        self.ui = ingresar_usuario.Ingresar_usuario()
        self.ui.show()
    
    def abrir_mostrar_facturas(self):
        self.ui = ingresar_usuario_facturas.Iuf()
        self.ui.show()

    def salir(self):
        exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    clase = Menu_principal()
    clase.show()
    sys.exit(app.exec_())