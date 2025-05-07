import re
from PilaTareas import PilaTareas

def mostrar_menu():
    print("\n--- REVISIÓN DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Revisar última tarea entregada")
    print("3. Ver próxima tarea a revisar")
    print("4. Mostrar todas las tareas pendientes")
    print("5. Salir")

def main():
    pila = PilaTareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            estudiante = input("Nombre del estudiante: ").strip()
            # Validación: solo letras y espacios
            if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", estudiante):
                print("Nombre inválido. Solo se permiten letras y espacios.")
                continue

            titulo = input("Título de la tarea: ").strip()
            if estudiante and titulo:
                pila.agregar_tarea(estudiante, titulo)
                print(f"Tarea agregada: '{titulo}' de {estudiante}")
            else:
                print("Datos incompletos. Intente de nuevo.")

        elif opcion == "2":
            pila.revisar_tarea()

        elif opcion == "3":
            pila.ver_siguiente_tarea()

        elif opcion == "4":
            pila.mostrar_tareas()

        elif opcion == "5":
            print("Saliendo del sistema de revisión de tareas.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
