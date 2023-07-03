import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class Factura_creada(QMainWindow):
    def __init__(self,factura):
        super(Factura_creada,self).__init__()
        uic.loadUi("contenedores/gui/la_factura_creada.ui",self)
        self.id_factura.setText(factura.codigo)
        self.pushButton.clicked.connect(self.aceptar)

    def aceptar(self):
        self.hide()