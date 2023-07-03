import random

class Factura():
    def __init__(self,fecha):
        self.__antibioticos = []
        self.__productos_control = []
        self.__fecha = fecha
        self.__id = str(random.randint(100000000,199999999))

    @property
    def productos_control(self):
        return self.__productos_control

    @property
    def antibioticos(self):
        return self.__antibioticos

    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def codigo(self):
        return self.__id

    def asociar_productos_control(self,producto):
        self.productos_control.append(producto)

    def asociar_antibioticos(self,producto):
        self.antibioticos.append(producto)
    