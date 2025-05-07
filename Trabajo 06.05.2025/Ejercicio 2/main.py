from Bandeja import Bandeja

def mostrar_menu():
    print("\n--- MENÚ DE PANADERÍA ---")
    print("1. Agregar pan a la bandeja")
    print("2. Vender pan (último en entrar)")
    print("3. Ver pan listo para vender")
    print("4. Mostrar todos los panes en la bandeja")
    print("5. Salir")

def main():
    bandeja = Bandeja()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            tipo = input("Ingrese el tipo de pan (ej. Baguette, Integral, Dulce): ").strip()
            if tipo:
                bandeja.agregar_pan(tipo)
                print(f"Se agregó: Pan de {tipo}")
            else:
                print("Debe ingresar un tipo de pan válido.")

        elif opcion == "2":
            bandeja.vender_pan()

        elif opcion == "3":
            bandeja.ver_pan_listo()

        elif opcion == "4":
            bandeja.mostrar_bandeja()

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
