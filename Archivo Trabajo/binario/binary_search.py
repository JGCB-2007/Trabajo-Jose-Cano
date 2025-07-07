
# search/binary_search.py

def binary_search(arr, target):
    """Realiza una búsqueda binaria en una lista ordenada y muestra el procedimiento paso a paso."""
    left = 0
    right = len(arr) - 1
    paso = 1  # Contador de pasos

    print("\n--- INICIO DEL PROCEDIMIENTO DE BÚSQUEDA BINARIA ---")

    while left <= right:
        mid = (left + right) // 2
        print(f"\nPaso {paso}:")
        print(f"  Izquierda (left) = {left}")
        print(f"  Derecha (right) = {right}")
        print(f"  Medio (mid) = {mid}")
        print(f"  Comparando: arr[{mid}] = {arr[mid]} con objetivo = {target}")

        if arr[mid] == target:
            print(f"\n Elemento encontrado en la posición {mid}.\n")
            return mid
        elif arr[mid] < target:
            print(f" El valor {arr[mid]} es menor que {target}. Buscar en la mitad derecha.")
            left = mid + 1
        else:
            print(f" El valor {arr[mid]} es mayor que {target}. Buscar en la mitad izquierda.")
            right = mid - 1

        paso += 1

    print("\nElemento no encontrado en la lista.\n")
    return -1
