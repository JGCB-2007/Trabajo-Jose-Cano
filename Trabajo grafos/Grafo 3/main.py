# archivo: main.py
from grafo import Grafo

def leer_opcion():
    print("\n--- Menú de Operaciones ---")
    print("1. Agregar vértices")
    print("2. Agregar aristas")
    print("3. Ver vecinos de un vértice")
    print("4. Verificar si existe una arista")
    print("5. Recorrido BFS")
    print("6. Recorrido DFS")
    print("7. Verificar si el grafo es conexo")
    print("8. Encontrar camino entre dos vértices")
    print("9. Mostrar grafo")
    print("0. Salir")
    return input("Seleccione una opción: ")

def leer_vertice(mensaje):
    return input(mensaje).strip()

def leer_lista_vertices():
    entrada = input("Ingrese los vértices separados por espacios: ")
    return entrada.strip().split()

def leer_aristas():
    print("Ingrese las aristas en formato: u v [peso]. Vacío para terminar.")
    aristas = []
    while True:
        linea = input("Arista: ").strip()
        if not linea:
            break
        partes = linea.split()
        if len(partes) < 2:
            print("Formato incorrecto. Debe ser: u v [peso]")
            continue
        u, v = partes[0], partes[1]
        peso = int(partes[2]) if len(partes) > 2 else 1
        aristas.append((u, v, peso))
    return aristas

if __name__ == "__main__":
    tipo = input("¿Grafo dirigido? (s/n): ").lower()
    grafo = Grafo(es_dirigido=(tipo == 's'))

    while True:
        opcion = leer_opcion()

        if opcion == '1':
            vertices = leer_lista_vertices()
            for v in vertices:
                grafo.agregar_vertice(v)
            print("Vértices agregados.")

        elif opcion == '2':
            aristas = leer_aristas()
            for u, v, peso in aristas:
                grafo.agregar_arista(u, v, peso)
            print("Aristas agregadas.")

        elif opcion == '3':
            v = leer_vertice("Vértice: ")
            vecinos = grafo.obtener_vecinos(v)
            print(f"Vecinos de {v}: {vecinos if vecinos else 'No existe o sin vecinos'}")

        elif opcion == '4':
            u = leer_vertice("Vértice origen: ")
            v = leer_vertice("Vértice destino: ")
            existe = grafo.existe_arista(u, v)
            print(f"Existe arista entre {u} y {v}: {'Sí' if existe else 'No'}")

        elif opcion == '5':
            inicio = leer_vertice("Inicio BFS: ")
            recorrido = grafo.bfs(inicio)
            print("BFS orden:", recorrido)

        elif opcion == '6':
            inicio = leer_vertice("Inicio DFS: ")
            recorrido = grafo.dfs(inicio)
            print("DFS orden:", recorrido)

        elif opcion == '7':
            try:
                print("Conexo" if grafo.es_conexo() else "No conexo")
            except ValueError as e:
                print("Error:", e)

        elif opcion == '8':
            inicio = leer_vertice("Inicio: ")
            fin = leer_vertice("Destino: ")
            camino = grafo.encontrar_camino(inicio, fin)
            print("Camino:", " -> ".join(camino) if camino else "No hay camino")

        elif opcion == '9':
            grafo.mostrar_grafo()

        elif opcion == '0':
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida.")
