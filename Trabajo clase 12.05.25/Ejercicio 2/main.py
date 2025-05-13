# main.py

from cola_impresora import ColaImpresion
from menu import mostrar_menu

def ejecutar():
    impresora = ColaImpresion()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            nombre = input("Nombre del documento: ").strip()
            usuario = input("Usuario que envía el documento: ").strip()
            try:
                paginas = int(input("Número de páginas: "))
            except ValueError:
                print(" Número de páginas inválido.")
                continue

            impresora.agregar_documento(nombre, usuario, paginas)

        elif opcion == "2":
            impresora.procesar_documento()

        elif opcion == "3":
            impresora.mostrar_cola()

        elif opcion == "4":
            impresora.mostrar_actual()

        elif opcion == "5":
            print(" Saliendo del sistema de impresión.")
            break

        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    ejecutar()
