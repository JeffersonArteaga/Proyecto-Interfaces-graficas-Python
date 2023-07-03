import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class Error(QMainWindow):
    def __init__(self):
        super(Error,self).__init__()
        uic.loadUi("contenedores/gui/ingrese_todos_los_campos.ui",self)
        self.bttn_aceptar.clicked.connect(self.aceptar)

    def aceptar(self):
        self.hide()