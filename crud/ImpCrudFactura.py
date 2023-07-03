from modelo import factura as factura
from crud import ICrud as ICrud

class ImpCrudFactura(ICrud.ICrud):
  
  def crear(self, **kwargs):
    return factura.Factura(kwargs['fecha'])
  
  def relacion(self, **kwargs):
    factura = kwargs['uno']
    factura.productos = kwargs['muchos']
    return factura
  
  def mostrar(self, **kwargs):
    pass