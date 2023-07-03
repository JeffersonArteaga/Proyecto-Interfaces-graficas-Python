class Cliente:

    def __init__(self, id_cliente, nombre_cliente):
        self.__id_cliente = id_cliente
        self.__nombre_cliente = nombre_cliente
        self.__facturas_cliente = []

    @property
    def cc(self):
        return self.__id_cliente

    @property
    def nombre(self):
        return self.__nombre_cliente

    @property
    def facturas(self):
        return self.__facturas_cliente

    @facturas.setter
    def facturas(self,factura):
        self.__facturas_cliente.append(factura)

    def asociar(self,factura):
        self.facturas.append(factura)



