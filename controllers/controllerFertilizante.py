from crud import impCrudFertilizante

class ControllerFertilizante:

    implementacion = impCrudFertilizante.ImpCrudFertilizante()

    @classmethod
    def crear(self,**kwargs):
        return self.implementacion.crear(**kwargs)