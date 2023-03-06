from database import Vehiculo
from database import Vehiculos
import config 
import csv

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)
    
class Coches(Vehiculo):
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
