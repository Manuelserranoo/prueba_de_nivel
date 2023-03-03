from bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self,color,rueda,tipo,velocidad,cilindrada):
        Bicicleta.__init_(self,color,rueda,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Bicicleta.__str__(self)+",{} km/h, {}cc".format(self.velocidad, self.cilindrada)