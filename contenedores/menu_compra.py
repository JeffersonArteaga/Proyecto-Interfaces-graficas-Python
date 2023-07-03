import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from contenedores import menu_productos_control, menu_antibioticos, factura_creada
from controllers import controllerFacturas
from datetime import datetime

class Menu_compra(QMainWindow):
    def __init__(self,cliente):
        super(Menu_compra,self).__init__()
        uic.loadUi("contenedores/gui/menu_compra.ui",self)
        fecha_factura = datetime.now()
        self.cliente = cliente
        controller_factura = controllerFacturas.ControllerFacturas()
        self.factura = controller_factura.crear(fecha = fecha_factura)
        self.bttn_comprar_pc.clicked.connect(self.comprar_pc)
        self.bttn_comprar_antibioticos.clicked.connect(self.comprar_antibioticos)
        self.bttn_terminar_compra.clicked.connect(self.terminar_compra)

    def comprar_pc(self):
        self.ventana = menu_productos_control.Mpc(self.factura)
        self.ventana.show()

    def comprar_antibioticos(self,):
        self.ventana = menu_antibioticos.Mant(self.factura)
        self.ventana.show()

    def terminar_compra(self):
        self.cliente.asociar(self.factura)
        print(self.cliente.facturas)
        self.hide()
        self.ventana = factura_creada.Factura_creada(self.factura)
        self.ventana.show()