import time  # ← nuevo import

def binary_search(arr, target):
    """Realiza una búsqueda binaria en una lista ordenada."""
    left = 0
    right = len(arr) - 1
    paso = 1
    inicio = time.time()  #  tiempo inicial

    print("\n--- INICIO DEL PROCEDIMIENTO DE BÚSQUEDA BINARIA ---")

    while left <= right:
        mid = (left + right) // 2
        print(f"\nPaso {paso}:")
        print(f"  Izquierda (left) = {left}")
        print(f"  Derecha (right) = {right}")
        print(f"  Medio (mid) = {mid}")
        print(f"  Comparando: arr[{mid}] = {arr[mid]} con objetivo = {target}")

        if arr[mid] == target:
            fin = time.time()
            print(f"\nElemento encontrado en la posición {mid}.")
            print(f" Tiempo de ejecución: {fin - inicio:.6f} segundos")
            return mid
        elif arr[mid] < target:
            print(f" {arr[mid]} < {target}. Buscar en la mitad derecha.")
            left = mid + 1
        else:
            print(f" {arr[mid]} > {target}. Buscar en la mitad izquierda.")
            right = mid - 1

        paso += 1

    fin = time.time()
    print("\n Elemento no encontrado en la lista.")
    print(f" Tiempo de ejecución: {fin - inicio:.6f} segundos")
    return -1
