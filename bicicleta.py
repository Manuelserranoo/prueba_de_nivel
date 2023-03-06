from database import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self,VIN,color,ruedas,tipo):
        super().__init__(self,VIN,color,ruedas)
        self.tipo = tipo
        def __str__(self):
            return Vehiculo.__str__(self) + ", {}".format(self.tipo)