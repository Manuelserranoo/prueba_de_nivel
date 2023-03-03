from coche import Coche

class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return Coche.__str__(self) + ", {} kilogramos".format(self.carga)