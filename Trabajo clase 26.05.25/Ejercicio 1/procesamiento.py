from cola import Cola
from pila import Pila

def procesar_cola(cola_original, cantidad):
    pila_resultado = Pila(cantidad)
    cola_final = Cola(cantidad)

    for i in range(cantidad):
        valor = cola_original.desencolar()
        if i % 2 == 0:
            cola_final.encolar(valor)
        else:
            pila_resultado.apilar(valor)

    return cola_final, pila_resultado
