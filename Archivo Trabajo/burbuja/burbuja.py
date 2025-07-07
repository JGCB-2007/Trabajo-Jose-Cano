# modulo_burbuja.py
def validar_entrada(texto):
    """
    Valida que la entrada del usuario sea una lista de números separados por comas.
    Retorna la lista de enteros si es válida, o None si no.
    """
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
    """
    Ordena la lista usando el método de burbuja,
    mostrando todos los pasos cuando se realiza un intercambio.
    """
    n = len(lista)
    for i in range(n-1):
        intercambio = False
        for j in range(n-1-i):
            if lista[j] > lista[j+1]:
                # Mostrar comparación antes del intercambio
                print(f"Comparando {lista[j]} y {lista[j+1]}: intercambio")
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True
                print(f"Estado actual de la lista: {lista}")
            else:
                print(f"Comparando {lista[j]} y {lista[j+1]}: no intercambio")
        if not intercambio:
            print("No se realizaron intercambios en esta pasada. La lista está ordenada.")
            break
    return lista
