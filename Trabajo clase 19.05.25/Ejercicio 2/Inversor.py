# Este archivo contiene la función que invierte una frase usando la clase Pila
from Pila import Pila 

    # Crea una nueva instancia de Pila
def invertir_frase(frase):
    pila_palabras = Pila()
    palabras = frase.split()

    # Apila cada palabra en la pila
    for palabra in palabras:
        pila_palabras.apilar(palabra)

    # Extrae las palabras de la pila en orden inverso
    frase_invertida = []
    while not pila_palabras.esta_vacia():
        frase_invertida.append(pila_palabras.desapilar())

    # Une las palabras invertidas en una sola cadena y la retorna
    return ' '.join(frase_invertida)