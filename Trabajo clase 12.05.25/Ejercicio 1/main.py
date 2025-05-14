from cola import Cola
from menu import mostrar_menu

# Función principal que ejecuta el sistema de la clínica
def ejecutar_sistema():
    cola_clinica = Cola()  # Se crea una cola vacía

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            # Validar que el nombre no esté vacío
            while True:
                nombre = input("Ingrese el nombre del paciente: ").strip()
                while not cola_clinica.validar_nombre(nombre):
                    print("  Nombre inválido. Solo se permiten letras y espacios.")
                    nombre = input("¿Qué usuario envía el documento?: ").strip()
                cola_clinica.insertar(nombre)
                break
                
        elif opcion == "2":
            cola_clinica.eliminar()

        elif opcion == "3":
            cola_clinica.imprimir()

        elif opcion == "4":
            print("Saliendo del sistema. ¡Gracias!")
            break

        else:
            print("  Opción inválida. Intente nuevamente.")

if __name__ == "__main__":  # Inicia el programa si se ejecuta directamente
    ejecutar_sistema()
