from RegistroDonantes import RegistroDonantes

def mostrar_menu():
    print("\n--- REGISTRO DE DONANTES - HOSPITAL DE ESTELÍ ---")
    print("1. Registrar donante")
    print("2. Revertir último registro")
    print("3. Ver donante en proceso")
    print("4. Ver todos los donantes registrados")
    print("5. Salir")

def main():
    registro = RegistroDonantes()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre del donante: ").strip()
            tipo_sangre = input("Ingrese el tipo de sangre (A+, O-, etc.): ").strip()
            if nombre and tipo_sangre:
                registro.registrar_donante(nombre, tipo_sangre)
                print(f"Donante {nombre} registrado con tipo de sangre {tipo_sangre}.")
            else:
                print("Datos inválidos. Por favor, intente de nuevo.")

        elif opcion == "2":
            registro.revertir_ultimo()

        elif opcion == "3":
            registro.mostrar_donante_actual()

        elif opcion == "4":
            registro.mostrar_todos()

        elif opcion == "5":
            print("Saliendo del sistema de registro.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
