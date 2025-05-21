# main.py
# Este archivo permite al usuario interactuar con la lista de reproducción

from lista_reproduccion import ListaReproduccion

def main():
    lista = ListaReproduccion()

    while True:
        print("\n Lista de Reproducción - Menú:")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente canción")
        print("4. Reproducir canción anterior")
        print("5. Mostrar lista de reproducción")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                nombre = input("Ingrese el nombre de la canción: ")
                if nombre:
                    lista.agregar_cancion(nombre)
                    print(f" Canción '{nombre}' agregada.")
                    break
                else:
                    print("El nombre de la canción no puede estar en blanco. Intente de nuevo.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre de la canción a eliminar: ")
            if lista.eliminar_cancion(nombre):
                print(f" Canción '{nombre}' eliminada.")
            else:
                print(" Canción no encontrada.")
        elif opcion == "3":
            siguiente = lista.reproducir_siguiente()
            if siguiente:
                print(f" Reproduciendo: {siguiente}")
            else:
                print(" No hay siguiente canción.")
        elif opcion == "4":
            anterior = lista.reproducir_anterior()
            if anterior:
                print(f" Reproduciendo: {anterior}")
            else:
                print(" No hay canción anterior.")
        elif opcion == "5":
            canciones = lista.mostrar_lista()
            if canciones:
                print("\nLista de reproducción:")
                for i, cancion in enumerate(canciones, 1):
                    print(f"{i}. {cancion}")
            else:
                print(" La lista está vacía.")
        elif opcion == "6":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()