import re
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto


def vin_valido(VIN, lista):
    if not re.match('[0-9]{2}[A-Z]$', VIN):
        print("VIN incorrecto, debe cumplir el formato.")
        return False
    for vehiculo in lista:
        if vehiculo.VIN == VIN:
            print("VIN utilizado por otro vehículo.")
            return False
    return True
