from cola import Cola
from procesamiento import procesar_cola

def main():
    n = int(input("¿Cuántos elementos desea ingresar en la cola? "))
    cola_original = Cola(n)

    print("Ingrese los elementos uno por uno:")
    for i in range(n):
        valor = int(input(f"Elemento {i + 1}: "))
        cola_original.encolar(valor)

    cola_resultado, pila_resultado = procesar_cola(cola_original, n)

    print("\nCola con posiciones pares:", cola_resultado)
    print("\nPila con posiciones impares:", pila_resultado)

if __name__ == "__main__":
    main()
