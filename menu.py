import os
import helpers
import database as db


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar los clientes ")
        print("[2] Buscar un cliente   ")
        print("[3] Añadir un cliente   ")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los clientes...\n")
            for vehiculo in db.Vehiculos.lista:
                print(vehiculo)

        elif opcion == '2':
            print("Buscando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "VIN (17 char)").upper() #######
            vehiculo = db.Vehiculos.buscar(VIN)
            print(vehiculo) if vehiculo else print("Cliente no encontrado.")

        elif opcion == '3':
            print("Añadiendo un vehiculo...\n")

            VIN = None
            while True:
                VIN = helpers.leer_texto(3, 3, "VIN (17 char)").upper() #######
                if helpers.vin_valido(VIN, db.Vehiculos.lista):
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize() #######
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize() #######
            db.Vehiculos.crear(dni, nombre, apellido)
            print("Vehiculo añadido correctamente.")

        elif opcion == '4':
            print("Modificando un vehiculo...\n")
            dni = helpers.leer_texto(3, 3, "VIN (17 char)").upper() #######
            vehiculo = db.Vehiculos.buscar(VIN)
            if vehiculo:
                color = helpers.leer_texto(
                    2, 30, f"Nombre (de 2 a 30 chars) [{vehiculo.color}]").capitalize()
                ruedas = helpers.leer_texto(
                    2, 30, f"Apellido (de 2 a 30 chars) [{vehiculo.ruedas}]").capitalize()
                db.Vehiculos.modificar(vehiculo.VIN, nombre, apellido)
                print("Vehículo modificado correctamente.")
            else:
                print("Vehículo no encontrado.")

        elif opcion == '5':
            print("Borrando un cliente...\n")
            VIN = helpers.leer_texto(3, 3, "DNI (17 char)").upper()
            print("Vehículo borrado correctamente.") if db.Vehiculos.borrar(
                dni) else print("Vehículo no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")
