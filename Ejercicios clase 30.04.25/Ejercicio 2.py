def ordena(pila):
    # Lista temporal para almacenar los datos
    temporal = []

    # Extraemos todos los elementos de la pila
    while pila:
        temporal.append(pila.pop())

    # Ordenamos de mayor a menor
    temporal.sort(reverse=True)

    # Volvemos a armar la pila ordenada
    pila_ordenada = []
    for num in temporal:
        pila_ordenada.append(num)

    return pila_ordenada

# Pedimos al usuario la cantidad de números a ingresar
n = int(input("¿Cuántos números desea ingresar en la pila?: "))
pila = []

# Cargamos la pila desde el usuario
for i in range(n):
    num = int(input(f"Ingrese el número #{i+1}: "))
    pila.append(num)

# Mostramos la pila original
print("Pila original:", pila)

# Ordenamos la pila de mayor (fondo) a menor (tope)
pila_ordenada = ordena(pila)

# Mostramos el resultado
print("Pila ordenada (mayor al fondo, menor arriba):", pila_ordenada)
