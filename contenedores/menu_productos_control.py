import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from contenedores import compra_exitosa, ingrese_todos_los_campos
from controllers import controllerProductoPlaga, controllerFertilizante
import random

class Mpc(QMainWindow):
    def __init__(self,factura):
        super(Mpc,self).__init__()
        uic.loadUi("contenedores/gui/mpc.ui",self)
        self.factura = factura
        self.bttn_comprar.clicked.connect(self.comprar)

    def comprar(self):
        tipo_producto = self.tipo_producto_control.itemText(self.tipo_producto_control.currentIndex())
        frecuencia = self.frec_aplicacion.text()
        precio = self.precio_producto.text()
        registro = random.randint(100000, 199999)

        if (len(tipo_producto) == 0 or len(frecuencia) == 0 or len(precio) == 0):
            self.ventana = ingrese_todos_los_campos.Error()
            self.ventana.show()
        else:
            if (tipo_producto == "Control de plagas"):
                controller_plaga = controllerProductoPlaga.ControllerProductoPlaga()
                producto = controller_plaga.crear(registro_ICA = registro, nombre_producto = "Control de plagas", frec_aplicacion = frecuencia, precio_producto = precio)
                
            else:
                controller_fertilizante = controllerFertilizante.ControllerFertilizante()
                producto = controller_fertilizante.crear(registro_ICA = registro, nombre_producto = "Control de fertilizantes", frec_aplicacion = frecuencia, precio_producto = precio)
                pass

            self.factura.asociar_productos_control(producto)
            self.hide()
            self.ventana = compra_exitosa.Compra_exitosa()
            self.ventana.show()

        