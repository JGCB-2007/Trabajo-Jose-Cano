# main.py
from burbuja import validar_entrada, burbuja_con_pasos

def main():
    while True:
        numeros = validar_entrada("Ingrese números separados por comas (ejemplo: 5, 3, 8, 1): ")
        if numeros is not None:
            break
        print("Por favor, ingrese una lista válida de números.")
    
    print(f"Lista inicial: {numeros}")
    lista_ordenada = burbuja_con_pasos(numeros)
    print(f"Lista ordenada: {lista_ordenada}")

if __name__ == "__main__":
    main()
