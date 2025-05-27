from cola import Cola
from pila import Pila

def main():
    cola_original = Cola()
    pila = Pila()

    entrada = input("Ingrese los elementos separados por comas (pueden ser letras o números):\n> ")
    elementos = [e.strip() for e in entrada.split(",")]

    # Encolar todos los elementos
    for elemento in elementos:
        cola_original.encolar(elemento)

    # Separación: pares se reencolan, impares se apilan
    tamaño = len(elementos)
    for i in range(tamaño):
        valor = cola_original.desencolar()
        if i % 2 == 0:
            cola_original.encolar(valor)
        else:
            pila.apilar(valor)

    # Mostrar resultados
    print("\nResultado final:")
    print("Cola (pares):", cola_original.ver_cola())
    print("Pila (impares):", pila.ver_pila())

if __name__ == "__main__":
    main()
