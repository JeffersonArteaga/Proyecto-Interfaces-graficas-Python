from crud import impCrudProductoPlaga

class ControllerProductoPlaga:

    implementacion = impCrudProductoPlaga.ImpCrudProductoPlaga()

    @classmethod
    def crear(self,**kwargs):
        return self.implementacion.crear(**kwargs)