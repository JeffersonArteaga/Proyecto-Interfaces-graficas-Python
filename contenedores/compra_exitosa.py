import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class Compra_exitosa(QMainWindow):
    def __init__(self):
        super(Compra_exitosa,self).__init__()
        uic.loadUi("contenedores/gui/compra_exitosa.ui",self)
        self.bttn_aceptar.clicked.connect(self.aceptar)

    def aceptar(self):
        self.hide()
