from crud import impCrudAntibioticos

class ControllerAntibiotico:

    implementacion = impCrudAntibioticos.ImpCrudAntibioticos()

    @classmethod
    def crear(self,dosis,tipo,precio):
        return self.implementacion.crear(dosis,tipo,precio)