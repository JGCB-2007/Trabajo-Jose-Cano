# Contiene la lógica para verificar si los paréntesis están balanceados

from Pila import Pila  # Importamos la clase Pila

def esta_balanceado(cadena):
    pila = Pila()

    # Diccionario para saber qué paréntesis cierra a cuál
    pares = {')': '(', ']': '[', '}': '{'}

    # Recorremos cada carácter de la cadena
    for caracter in cadena:
        if caracter in "({[":
            pila.apilar(caracter)
        elif caracter in ")}]":
            if pila.esta_vacia():
                return False
            tope = pila.desapilar()
            if tope != pares[caracter]:
                return False

    # Al final, si la pila quedó vacía, está balanceado
    return pila.esta_vacia()