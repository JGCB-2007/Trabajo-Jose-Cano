def Convbinario(numero):
    if numero == 0:
        return [0]

    pila = []

    # Convertir el número a binario usando división sucesiva
    while numero > 0:
        residuo = numero % 2
        pila.append(residuo)
        numero = numero // 2

    binario = []

    # Extraer los bits en orden correcto (desde la pila)
    while pila:
        binario.append(pila.pop())

    return binario

# Pedir número al usuario
numero = int(input("Ingrese un número entero para convertir a binario: "))

# Convertir y mostrar resultado
resultado = Convbinario(numero)
print(f"El número en binario es: {resultado}")
