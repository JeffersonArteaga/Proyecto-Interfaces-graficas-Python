from modelo import cliente as cliente
from crud import ICrud as ICrud

class ImpCrudCliente(ICrud.ICrud):
  
  def crear(self, **kwargs):
    return cliente.Cliente(kwargs['id_cliente'],kwargs['nombre_cliente'])

  def guardar(self, **kwargs):
    ICrud.ICrud.lista_clientes.append(kwargs['cliente'])

  def buscar(self,cc):
    busqueda = []
    lista = ICrud.ICrud.lista_clientes
    for cliente in lista:
      if (cliente.cc == cc):
        busqueda.append(True)
        busqueda.append(cliente)
        return busqueda
    busqueda.append(False)
    busqueda.append(0)
    return busqueda
  
  def relacion(self, **kwargs):
    cliente = kwargs['uno']
    cliente.cuentas = kwargs['muchos']
    return cliente
  
  def mostrar(self, **kwargs):
    pass
