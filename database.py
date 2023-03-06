class Vehiculo:
    def __init__(self, VIN, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        self.VIN = VIN
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
    
class Vehiculos:
    lista = []
    @staticmethod
    def buscar(VIN):
        for vehiculo in Vehiculos.lista:
            if vehiculo.VIN == VIN:
                return vehiculo
    @staticmethod
    def agregar(VIN,color,ruedas):
        vehiculo = Vehiculo(VIN,color,ruedas)
        Vehiculos.lista.append(vehiculo)
    @staticmethod
    def modificar(VIN,color,ruedas):
        vehiculo = Vehiculos.buscar(VIN)
        if vehiculo != None:
            vehiculo.color = color
            vehiculo.ruedas = ruedas
