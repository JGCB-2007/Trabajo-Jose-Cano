def crear_matriz_adyacencia():
    print("=== Construcción de Matriz de Adyacencia ===")
    
    while True:
        try:
            n = int(input("Ingrese el número de nodos del grafo (mínimo 2): "))
            if n < 2:
                print("Debe haber al menos 2 nodos. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
    
    while True:
        try:
            m = int(input("Ingrese el número de aristas: "))
            if m < 0:
                print("El número de aristas no puede ser negativo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    # Inicializar matriz de n x n con ceros
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    print("\nIngrese las aristas en formato: nodo_origen nodo_destino")
    print(f"(números del 0 al {n - 1})")

    for i in range(m):
        while True:
            try:
                u, v = map(int, input(f"Arista {i + 1}: ").split())
                if u < 0 or u >= n or v < 0 or v >= n:
                    print(f"Los nodos deben estar entre 0 y {n - 1}. Intente de nuevo.")
                    continue
                if u == v:
                    print("No se permiten bucles (aristas de un nodo a sí mismo).")
                    continue
                if matriz[u][v] == 1:
                    print("Esa arista ya fue ingresada. Intente con otra.")
                    continue
                matriz[u][v] = 1
                matriz[v][u] = 1  # Grafo no dirigido
                break
            except ValueError:
                print("Formato incorrecto. Ingrese dos números separados por espacio.")
    
    print("\n=== Matriz de Adyacencia ===")
    print("   " + " ".join(str(i) for i in range(n)))
    for i in range(n):
        print(f"{i}: " + " ".join(str(matriz[i][j]) for j in range(n)))

if __name__ == "__main__":
    crear_matriz_adyacencia()
