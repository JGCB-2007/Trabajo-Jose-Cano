# modulo_burbuja.py
import time  # ← nuevo import

def validar_entrada(texto):
    entrada = input(texto)
    elementos = entrada.split(',')
    numeros = []
    for elem in elementos:
        elem = elem.strip()
        if not elem.isdigit():
            print(f"Error: '{elem}' no es un número válido.")
            return None
        numeros.append(int(elem))
    return numeros

def burbuja_con_pasos(lista):
    n = len(lista)
    inicio = time.time()  #iniciar tiempo

    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                print(f"Comparando {lista[j]} y {lista[j+1]}: intercambio")
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
                print(f"Estado actual de la lista: {lista}")
            else:
                print(f"Comparando {lista[j]} y {lista[j+1]}: no intercambio")
        if not intercambio:
            print("No se realizaron intercambios en esta pasada. La lista está ordenada.")
            break

    fin = time.time()  # fin del tiempo
    print(f" Tiempo de ejecución: {fin - inicio:.6f} segundos")
    return lista
