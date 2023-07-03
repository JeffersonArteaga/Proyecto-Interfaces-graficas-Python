class ProductoCtrl:

    def __init__(self, registro_ICA, nombre_producto, frec_aplicacion, precio_producto):
        self.__registro_ICA = registro_ICA
        self.__nombre_producto = nombre_producto
        self.__frec_aplicacion = frec_aplicacion
        self.__precio_producto = precio_producto

    @property
    def registro(self):
        return self.__registro_ICA

    @property
    def nombre_producto(self):
        return self.__nombre_producto

    @property
    def frec_aplicacion(self):
        return self.__frec_aplicacion

    @property
    def precio_producto(self):
        return self.__precio_producto