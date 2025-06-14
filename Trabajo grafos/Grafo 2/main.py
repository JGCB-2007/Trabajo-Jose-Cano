from grafo import Grafo

def menu():
    print("\n--- Menú del Grafo ---")
    print("1. Agregar vértice(s)")
    print("2. Agregar arista")
    print("3. Mostrar vecinos de un vértice")
    print("4. Verificar si existe una arista")
    print("5. Mostrar grafo completo")
    print("6. BFS (Búsqueda en amplitud)")
    print("7. DFS (Búsqueda en profundidad)")
    print("8. Salir")

def leer_vertice(mensaje):
    while True:
        v = input(mensaje).strip()
        if v:
            return v
        print("Entrada vacía. Intente de nuevo.")

def leer_multiples_vertices(mensaje):
    entrada = input(mensaje).strip()
    if ',' in entrada:
        vertices = [v.strip() for v in entrada.split(',')]
    else:
        vertices = [v.strip() for v in entrada.split()]
    return list(dict.fromkeys([v for v in vertices if v != ""]))

def leer_entero(mensaje, default=1):
    entrada = input(mensaje).strip()
    if entrada == "":
        return default
    try:
        return int(entrada)
    except ValueError:
        print("Entrada inválida. Usando valor por defecto:", default)
        return default

def main():
    tipo = input("¿Deseas un grafo dirigido? (s/n): ").strip().lower()
    while tipo not in ['s', 'n']:
        tipo = input("Entrada inválida. ¿Deseas un grafo dirigido? (s/n): ").strip().lower()

    grafo = Grafo(es_dirigido=(tipo == 's'))

    while True:
        menu()
        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == '1':
            vertices = leer_multiples_vertices("Ingrese uno o más vértices (separados por espacio o coma): ")
            for v in vertices:
                if v in grafo.adyacencia:
                    print(f"El vértice '{v}' ya existe.")
                else:
                    grafo.agregar_vertice(v)
                    print(f"Vértice '{v}' agregado.")

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
                print(f"El vértice '{v}' no tiene vecinos o no existe.")

        elif opcion == '4':
            u = leer_vertice("Vértice origen: ")
            v = leer_vertice("Vértice destino: ")
            print(f"¿Existe la arista de '{u}' a '{v}'?: {grafo.existe_arista(u, v)}")

        elif opcion == '5':
            print("=== Representación del grafo ===")
            grafo.mostrar_grafo()

        elif opcion == '6':
            inicio = leer_vertice("Vértice de inicio para BFS: ")
            resultado = grafo.bfs(inicio)
            if resultado:
                print("Orden de visita BFS:", resultado)
            else:
                print(f"El vértice '{inicio}' no existe o no tiene conexiones.")

        elif opcion == '7':
            inicio = leer_vertice("Vértice de inicio para DFS: ")
            resultado = grafo.dfs(inicio)
            if resultado:
                print("Orden de visita DFS:", resultado)
            else:
                print(f"El vértice '{inicio}' no existe o no tiene conexiones.")

        elif opcion == '8':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
