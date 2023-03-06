import csv
import config

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
    def crear(VIN,color,ruedas):
        vehiculo = Vehiculo(VIN,color,ruedas)
        Vehiculos.lista.append(vehiculo)
    @staticmethod
    def modificar(VIN, color, ruedas):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.VIN == VIN:
                Vehiculos.lista[indice].color = color
                Vehiculos.lista[indice].ruedas = ruedas
                Vehiculos.guardar()
                return Vehiculos.lista[indice]
    @staticmethod
    def borrar(VIN):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.VIN == VIN:
                vehiculo = Vehiculos.lista.pop(indice)
                Vehiculos.guardar()
                return vehiculo

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Vehiculos.lista:
                writer.writerow((vehiculo.VIN, vehiculo.color, vehiculo.ruedas))
