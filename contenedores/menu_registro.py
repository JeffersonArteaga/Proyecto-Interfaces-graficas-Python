import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from contenedores import ingrese_todos_los_campos, usuario_registrado
from controllers import controllerClientes

class Menu_registro(QMainWindow):
    def __init__(self):
        super(Menu_registro,self).__init__()
        uic.loadUi("contenedores/gui/menu_registro.ui",self)
        self.bttn_volver_menu.clicked.connect(self.volver_menu)
        self.bttn_registrar_usuario.clicked.connect(self.registrar_usuario)

    def registrar_usuario(self):
        cc = self.campo_cc.text()
        nombre = self.campo_nombre_usuario.text()

        if (len(cc) == 0 or len(nombre) == 0):
            self.error = ingrese_todos_los_campos.Error()
            self.error.show()
        else:
            controller_cliente = controllerClientes.ControllerClientes()
            nuevo_cliente = controller_cliente.crear(id_cliente = cc, nombre_cliente = nombre)
            guardar_cliente = controller_cliente.guardar(cliente = nuevo_cliente)
            self.succesful = usuario_registrado.Succesful()
            self.succesful.show()

    def volver_menu(self):
        self.hide()