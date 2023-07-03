import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from contenedores import ingrese_todos_los_campos, menu_compra, usuario_no_esta_registrado
from controllers import controllerClientes

class Ingresar_usuario(QMainWindow):
    def __init__(self):
        super(Ingresar_usuario,self).__init__()
        uic.loadUi("contenedores/gui/ingresar_usuario.ui",self)
        self.bttn_ingresar_usuario.clicked.connect(self.ingresar)
        self.bttn_volver_menu.clicked.connect(self.volver_menu)

    def ingresar(self):
        cc_usuario = self.campo_cc.text()
        if(len(cc_usuario) == 0):
            self.ventana = ingrese_todos_los_campos.Error()
            self.ventana.show()
        else:
            controller_cliente = controllerClientes.ControllerClientes()
            buscar_cliente = controller_cliente.buscar(cc_usuario)
            if buscar_cliente[0]:
                cliente = buscar_cliente[1]
                self.ventana = menu_compra.Menu_compra(cliente)
                self.ventana.show()
            else:
                self.ventana = usuario_no_esta_registrado.Usuario_no_esta()
                self.ventana.show()
            

    def volver_menu(self):
        self.hide()