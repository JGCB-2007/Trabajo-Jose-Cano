# Menú principal para agregar valores, buscar y mostrar la lista enlazada

from lista_enlazada import ListaEnlazada

def main():
    lista = ListaEnlazada()

    while True:
        print("\n Lista Enlazada - Menú:")
        print("1. Agregar valor")
        print("2. Buscar valor")
        print("3. Mostrar lista")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = input("Ingrese el valor a agregar: ")
            lista.agregar(valor)
            print(f" Valor '{valor}' agregado.")
        elif opcion == "2":
            valor = input("Ingrese el valor a buscar: ")
            posicion = lista.buscar(valor)
            if posicion != -1:
                print(f" Valor '{valor}' encontrado en la posición {posicion}.")
            else:
                print(f" Valor '{valor}' no se encuentra en la lista.")
        elif opcion == "3":
            valores = lista.mostrar()
            print(" Contenido de la lista:", valores if valores else "La lista está vacía.")
        elif opcion == "4":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
