import re
from CajaMedicamento import CajaMedicamentos

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE MEDICAMENTOS ---")
    print("1. Agregar medicamento")
    print("2. Surtir medicamento")
    print("3. Ver medicamento superior")
    print("4. Mostrar todos los medicamentos")
    print("5. Salir")

def solicitar_nombre():
    while True:
        nombre = input("Nombre del medicamento: ").strip()
        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", nombre):
            return nombre
        else:
            print(" Nombre inválido. Use solo letras y espacios.")

def solicitar_lote():
    while True:
        lote = input("Número de lote (4 dígitos): ").strip()
        if re.fullmatch(r"\d{4}", lote):
            return lote
        else:
            print(" Lote inválido. Debe tener exactamente 4 dígitos.")

def main():
    caja = CajaMedicamentos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = solicitar_nombre()
            lote = solicitar_lote()
            caja.apilar_medicamento(nombre, lote)
            print(" Medicamento agregado correctamente.")

        elif opcion == "2":
            caja.surtir_medicamento()

        elif opcion == "3":
            caja.ver_superior()

        elif opcion == "4":
            caja.mostrar_todos()

        elif opcion == "5":
            print(" Saliendo del sistema.")
            break

        else:
            print(" Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
