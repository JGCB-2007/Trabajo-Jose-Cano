from cola_impresora import ColaImpresion
from menu import mostrar_menu
from validaciones import validar_nombre_usuario, validar_paginas

def ejecutar():
    impresora = ColaImpresion()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            # Validar nombre del documento
            nombre = input("Escribe el nombre del documento: ").strip()
            while not nombre:
                print(" El nombre del documento no puede estar vacío.")
                nombre = input("Escribe el nombre del documento: ").strip()

            # Validar nombre del usuario
            usuario = input("¿Qué usuario envía el documento?: ").strip()
            while not validar_nombre_usuario(usuario):
                print("  Nombre inválido. Solo se permiten letras y espacios.")
                usuario = input("¿Qué usuario envía el documento?: ").strip()

            # Validar número de páginas
            while True:
                paginas_input = input("Digite el número de páginas: ").strip()
                if not paginas_input.isdigit():
                    print("  Entrada inválida. Debe ingresar solo números enteros.")
                    continue

                paginas = int(paginas_input)
                if not validar_paginas(paginas):
                    print("  El número de páginas debe ser mayor que cero.")
                    continue
                break

            impresora.agregar_documento(nombre, usuario, paginas)
#muestra la informacion ya puesta en cola impresion
        elif opcion == "2":
            impresora.procesar_documento()
        elif opcion == "3":
            impresora.mostrar_cola()
        elif opcion == "4":
            impresora.mostrar_actual()
        elif opcion == "5":
            print("  Saliendo del sistema de impresión.")
            break
        else:
            print("  Opción inválida.")

if __name__ == "__main__":
    ejecutar()
