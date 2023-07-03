from crud import ICrud
from modelo import ProductoFertilizante

class ImpCrudFertilizante:

    def crear(self, **kwargs):
        return ProductoFertilizante.Fertilizante(kwargs['registro_ICA'], kwargs['nombre_producto'], kwargs['frec_aplicacion'],kwargs['precio_producto'])
  
    def relacion(self, **kwargs):
        pass
        
    def mostrar(self, **kwargs):
        pass