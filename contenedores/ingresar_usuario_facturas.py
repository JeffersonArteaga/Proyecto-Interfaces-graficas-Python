import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from contenedores import ingrese_todos_los_campos, usuario_no_esta_registrado, mostrar_factura
from controllers import controllerClientes

class Iuf(QMainWindow):
    def __init__(self):
        super(Iuf,self).__init__()
        uic.loadUi("contenedores/gui/ingresar_usuario_facturas.ui",self)
        self.bttn_volver_menu.clicked.connect(self.volver_menu)
        self.bttn_consultar_facturas.clicked.connect(self.consultar)

    def consultar(self):
        cc_usuario = self.campo_cc.text()
        if (len(cc_usuario) == 0):
            self.ventana = ingrese_todos_los_campos.Error()
            self.ventana.show()
        else:
            controller_cliente = controllerClientes.ControllerClientes()
            buscar_cliente = controller_cliente.buscar(cc_usuario)
            if buscar_cliente[0]:
                cliente = buscar_cliente[1]
                self.ventana = mostrar_factura.Mostrar(cliente)
                self.ventana.show()
                
            else:
                self.ventana = usuario_no_esta_registrado.Usuario_no_esta()
                self.ventana.show()

    def volver_menu(self):
        self.hide()
