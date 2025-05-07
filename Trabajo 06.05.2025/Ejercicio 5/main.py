import re
from CamionPila import CamionPila

def mostrar_menu():
    print("\n--- GESTIÓN DE SACOS EN EL CAMIÓN ---")
    print("1. Apilar un saco")
    print("2. Descargar el último saco")
    print("3. Ver el saco que está encima")
    print("4. Mostrar todos los sacos cargados")
    print("5. Salir")

def solicitar_producto():
    while True:
        producto = input("Nombre del producto: ").strip()
        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", producto):
            return producto
        else:
            print(" Nombre inválido. Solo se permiten letras y espacios. Intente de nuevo.")

def solicitar_peso():
    while True:
        try:
            peso = float(input("Peso del saco (kg): ").strip())
            if peso > 0:
                return peso
            else:
                print(" El peso debe ser mayor a 0.")
        except ValueError:
            print(" Entrada inválida. Debe ingresar un número.")

def main():
    camion = CamionPila()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            producto = solicitar_producto()
            peso = solicitar_peso()
            camion.apilar_saco(producto, peso)
            print(f"Saco de {producto} apilado correctamente.")

        elif opcion == "2":
            camion.descargar_saco()

        elif opcion == "3":
            camion.ver_saco_encima()

        elif opcion == "4":
            camion.mostrar_sacos()

        elif opcion == "5":
            print("Saliendo del sistema de carga del camión.")
            break

        else:
            print(" Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
