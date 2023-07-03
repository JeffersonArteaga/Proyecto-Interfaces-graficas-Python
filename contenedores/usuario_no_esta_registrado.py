import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class Usuario_no_esta(QMainWindow):
    def __init__(self):
        super(Usuario_no_esta,self).__init__()
        uic.loadUi("contenedores/gui/estanot.ui",self)
        self.bttn_aceptar.clicked.connect(self.aceptar)

    def aceptar(self):
        self.hide()