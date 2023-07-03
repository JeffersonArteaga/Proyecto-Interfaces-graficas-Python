import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from contenedores import ingrese_todos_los_campos, compra_exitosa, menu_compra
from controllers import controllerAntibiotico

class Mant(QMainWindow):
    def __init__(self,factura):
        super(Mant,self).__init__()
        uic.loadUi("contenedores/gui/menu_antibioticos.ui",self)
        self.factura = factura
        self.bttn_comprar.clicked.connect(self.comprar)

    def comprar(self):
        tipo_antibiotico = self.tipo_antibiotico.itemText(self.tipo_antibiotico.currentIndex())
        dosis_a = self.dosis.text()
        precio_a = self.precio_producto.text()
        if (len(tipo_antibiotico) == 0 or len(dosis_a) == 0 or len(precio_a) == 0):
            self.ventana = ingrese_todos_los_campos.Error()
            self.ventana.show()
        else:
            controller_antibiotico = controllerAntibiotico.ControllerAntibiotico()
            producto = controller_antibiotico.crear(dosis_a, tipo_antibiotico, precio_a)
            
            self.factura.asociar_antibioticos(producto)
            self.hide()
            self.ventana = compra_exitosa.Compra_exitosa()
            self.ventana.show()