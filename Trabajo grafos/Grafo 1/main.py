from grafo import Grafo

def menu():
    print("\n--- Menú del Grafo ---")
    print("1. Agregar vértice")
    print("2. Agregar arista")
    print("3. Mostrar vecinos de un vértice")
    print("4. Verificar si existe una arista")
    print("5. Mostrar grafo completo")
    print("6. Salir")

def leer_vertice(mensaje):
    while True:
        v = input(mensaje).strip()
        if v == "":
            print("El nombre del vértice no puede estar vacío. Intenta de nuevo.")
        else:
            return v

def leer_entero(mensaje, default=1):
    entrada = input(mensaje).strip()
    if entrada == "":
        return default
    try:
        return int(entrada)
    except ValueError:
        print("Entrada inválida. Se usará el valor por defecto:", default)
        return default

def main():
    tipo = input("¿Deseas un grafo dirigido? (s/n): ").strip().lower()
    while tipo not in ['s', 'n']:
        print("Entrada no válida. Escribe 's' para sí o 'n' para no.")
        tipo = input("¿Deseas un grafo dirigido? (s/n): ").strip().lower()

    grafo = Grafo(es_dirigido=(tipo == 's'))

    while True:
        menu()
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == '1':
            v = leer_vertice("Ingrese el nombre del vértice: ")
            if v in grafo.adyacencia:
                print(f"El vértice '{v}' ya existe.")
            else:
                grafo.agregar_vertice(v)
                print(f"Vértice '{v}' agregado correctamente.")

        elif opcion == '2':
            u = leer_vertice("Vértice origen: ")
            v = leer_vertice("Vértice destino: ")
            peso = leer_entero("Peso (ENTER para usar 1): ")
            grafo.agregar_arista(u, v, peso)
            print(f"Arista '{u} -> {v}' con peso {peso} agregada.")

        elif opcion == '3':
            v = leer_vertice("Ingrese el vértice: ")
            vecinos = grafo.obtener_vecinos(v)
            if vecinos:
                print(f"Vecinos de '{v}': {vecinos}")
            else:
                if v in grafo.adyacencia:
                    print(f"El vértice '{v}' no tiene vecinos.")
                else:
                    print(f"El vértice '{v}' no existe.")

        elif opcion == '4':
            u = leer_vertice("Vértice origen: ")
            v = leer_vertice("Vértice destino: ")
            if grafo.existe_arista(u, v):
                print(f"Sí existe la arista de '{u}' a '{v}'.")
            else:
                print(f"No existe la arista de '{u}' a '{v}'.")

        elif opcion == '5':
            print("=== Representación del grafo ===")
            grafo.mostrar_grafo()

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor selecciona un número del 1 al 6.")

if __name__ == "__main__":
    main()

