class Antibiotico:

    def __init__(self,dosis, tipo, precio):
        self.__nombre_producto = "Antibiotico"
        self.__dosis = dosis
        self.__tipo = tipo
        self.__precio = precio

    @property
    def dosis(self):
        return self.__dosis

    @property
    def tipo(self):
        return self.__tipo

    @property
    def precio(self):
        return self.__precio

    def __str__(self):
        texto = "Nombre del producto: {0} \nDosis: {1} \nTipo: {2} \nPrecio: {3}\n"
        return texto.format(self.__nombre_producto, self.__dosis, self.__tipo, self.__precio)



