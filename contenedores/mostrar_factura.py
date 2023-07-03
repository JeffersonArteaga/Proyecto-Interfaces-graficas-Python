
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import Qt

class Mostrar(QMainWindow):
    def __init__(self,cliente):
        super().__init__()
        uic.loadUi("contenedores/gui/mostrar_factura.ui",self)
        self.cliente = cliente
        self.campo_cc.setText(self.cliente.cc)
        self.campo_cliente.setText(self.cliente.nombre)

        facturas = self.cliente.facturas

        for factura in facturas:
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item_0.setText(0, "id factura: "+str(factura.codigo))
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1.setText(0, "fecha factura:" +str(factura.fecha))
            item_2 = QtWidgets.QTreeWidgetItem(item_0)
            item_2.setText(0, "productos: ")
            for producto in factura.antibioticos:
                item_3 = QtWidgets.QTreeWidgetItem(item_2)
                item_3.setText(0,producto.__str__())
            for producto in factura.productos_control:
                item_3 = QtWidgets.QTreeWidgetItem(item_2)
                item_3.setText(0,producto.__str__())


        
       
        