import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from crud import ICrud

class Succesful(QMainWindow):
    def __init__(self):
        super(Succesful,self).__init__()
        uic.loadUi("contenedores/gui/exito_registrado.ui",self)
        self.boton_aceptar.clicked.connect(self.aceptar)

    def aceptar(self):
        print(ICrud.ICrud.lista_clientes)
        self.hide()
