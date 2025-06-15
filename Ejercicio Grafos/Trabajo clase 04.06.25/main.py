from arbol import ArbolBin

def main():
    tree = ArbolBin()
    print("Ingrese valores para insertar en el árbol. Escriba 'fin' para terminar.")
    while True:
        entrada = input("Valor: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            tree.insert(numero)
        except ValueError:
            print("Por favor ingrese un número válido.")

    print("\nRecorrido Inorden:")
    tree.recorrido_inorden()

    print("Recorrido Preorden:")
    tree.recorrido_preorden()

    print("Recorrido Postorden:")
    tree.recorrido_postorden()

    try:
        buscar_valor = int(input("\nIngrese un valor a buscar en el árbol: "))
        if tree.buscar(buscar_valor):
            print(f"{buscar_valor} fue encontrado en el árbol.")
        else:
            print(f"{buscar_valor} no se encuentra en el árbol.")
    except ValueError:
        print("Valor inválido para búsqueda.")

if __name__ == "__main__":  # También estaba mal escrito en tu código original
    main()
