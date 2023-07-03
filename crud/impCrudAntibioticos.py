from crud import ICrud
from modelo import Antibiotico

class ImpCrudAntibioticos(ICrud.ICrud):

  

    def crear(self,dosis,tipo,precio):
        return Antibiotico.Antibiotico(dosis,tipo,precio)

    def relacion(self,**Kwargs):
        pass
    def mostrar(self, **kwargs):
        pass