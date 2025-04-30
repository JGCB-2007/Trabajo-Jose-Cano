def separarParImpar(pila):
    pila_pares = []
    pila_impares = []

    # Separar los números en pares e impares
    while pila:
        numero = pila.pop()
        if numero % 2 == 0:
            pila_pares.append(numero)
        else:
            pila_impares.append(numero)

    nueva_pila = []

    # Primero agregamos los pares (del fondo al tope)
    while pila_pares:
        nueva_pila.append(pila_pares.pop())

    # Luego los impares (del fondo al tope)
    while pila_impares:
        nueva_pila.append(pila_impares.pop())

    return nueva_pila


# Pedir al usuario cuántos elementos quiere en la pila
n = int(input("¿Cuántos números deseas ingresar en la pila?: "))
pila = []

# Ingresar los números
for i in range(n):
    num = int(input(f"Ingrese el número #{i+1}: "))
    pila.append(num)

# Mostrar la pila original
print("Pila original:", pila)

# Separar pares e impares
resultado = separarParImpar(pila)

# Mostrar resultado
print("Pila separada (pares al fondo, impares arriba):", resultado)
