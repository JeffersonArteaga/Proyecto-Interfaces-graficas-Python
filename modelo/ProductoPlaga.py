from modelo import ProductoControl as PtoCtrl

class ProductoPlaga(PtoCtrl.ProductoCtrl):
    def __init__(self, registro_ICA, nombre_producto, frec_aplicacion, precio_producto):
        super().__init__(registro_ICA, nombre_producto, frec_aplicacion, precio_producto)

    def __str__(self):
        texto = "Registro ICA: {0} \nNombre del producto: {1} \nPeriodo de carencia: {2} \nPrecio: {3}"
        return texto.format(self.registro, self.nombre_producto, self.frec_aplicacion, self.precio_producto)
    

