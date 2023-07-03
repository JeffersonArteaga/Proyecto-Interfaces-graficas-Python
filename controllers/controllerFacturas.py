from crud import ImpCrudFactura

class ControllerFacturas:

    implementacion = ImpCrudFactura.ImpCrudFactura()

    @classmethod
    def crear(self,**Kwargs):
        return self.implementacion.crear(**Kwargs)
