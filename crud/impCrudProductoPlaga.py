from crud import ICrud
from modelo import ProductoPlaga

class ImpCrudProductoPlaga:
    def crear(self, **kwargs):
        return ProductoPlaga.ProductoPlaga(kwargs['registro_ICA'], kwargs['nombre_producto'], kwargs['frec_aplicacion'],kwargs['precio_producto'])
  
    def relacion(self, **kwargs):
        pass
        
    def mostrar(self, **kwargs):
        pass