# Este archivo permite al usuario interactuar con la cola de prioridad

from cola_prioridad import ColaPrioridad

def main():
    cola = ColaPrioridad()

    while True:
        print("\n Cola de Prioridad - Menú:")
        print("1. Agregar elemento")
        print("2. Desencolar elemento (mayor prioridad)")
        print("3. Mostrar cola")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del elemento: ").strip()
            if not nombre:
                print("Error: El nombre no puede estar vacío.")
                continue  # Vuelve al menú principal sin pedir prioridad

            try:
                prioridad = int(input("Ingrese su prioridad (entero, menor = más alta): "))
                cola.encolar(nombre, prioridad)
                print(f" Elemento '{nombre}' agregado con prioridad {prioridad}.")
            except ValueError:
                print("Prioridad inválida. Debe ser un número entero.")
           

        elif opcion == "2":
            nodo = cola.desencolar()
            if nodo:
                print(f" Elemento desencolado: {nodo.nombre} (Prioridad: {nodo.prioridad})")
            else:
                print(" La cola está vacía.")
        elif opcion == "3":
            elementos = cola.mostrar()
            if elementos:
                print("\n Elementos en la cola:")
                for i, (nombre, prioridad) in enumerate(elementos, 1):
                    print(f"{i}. {nombre} (Prioridad: {prioridad})")
            else:
                print(" La cola está vacía.")
        elif opcion == "4":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()