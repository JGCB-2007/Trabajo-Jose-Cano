# main.py

from binary_search import binary_search

def pedir_lista_numeros():
    while True:
        entrada = input("Ingrese una lista de números enteros ordenados, separados por comas: ")
        try:
            numeros = [int(num.strip()) for num in entrada.split(",")]
            if numeros != sorted(numeros):
                print("La lista debe estar ordenada de menor a mayor.")
            else:
                return numeros
        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.strip().lstrip("-").isdigit():
            return int(entrada)
        else:
            print("Por favor, ingrese un número entero válido.")

def main():
    datos = pedir_lista_numeros()
    objetivo = pedir_entero("Ingrese el número a buscar: ")

    resultado = binary_search(datos, objetivo)

    if resultado != -1:
        print(f"Elemento encontrado en la posición {resultado} (índice base 0).")
    else:
        print("Elemento no encontrado en la lista.")

if __name__ == "__main__":
    main()
