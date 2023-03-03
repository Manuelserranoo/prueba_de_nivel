from database import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        Vehiculo.__init__(self,color,ruedas,tipo)
        self.tipo = tipo
        def __str__(self):
            return Vehiculo.__str__(self) + ", {}".format(self.tipo)