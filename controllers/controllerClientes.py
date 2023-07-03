from crud import ImpCrudCliente

class ControllerClientes:

    impcrudcliente = ImpCrudCliente.ImpCrudCliente()

    @classmethod
    def crear(self,**kwargs):
        return self.impcrudcliente.crear(**kwargs)

    @classmethod
    def guardar(self,**kwargs):
        return self.impcrudcliente.guardar(**kwargs)

    @classmethod
    def buscar(self,cc):
        return self.impcrudcliente.buscar(cc)