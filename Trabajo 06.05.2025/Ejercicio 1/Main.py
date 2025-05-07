from Documento import Documento
from Pila_Documento import Pila_Documento

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar documento")
    print("2. Marcar documentos como revisados (en orden)")
    print("3. Eliminar documento individual")
    print("4. Eliminar TODOS los documentos revisados")
    print("5. Mostrar pila")
    print("6. Salir")

def main():
    pila = Pila_Documento()

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            while True:
                descripcion = input("\nIngrese la descripción del documento (o 'salir' para volver al menú): ").strip()
                if descripcion.lower() == "salir":
                    break
                if descripcion:
                    pila.push(Documento(descripcion))
                else:
                    print(" Descripción vacía. Intente nuevamente.")

        elif opcion == "2":
            if not pila.pila:
                print(" No hay documentos para revisar.")
                continue

            while True:
                pila.mostrar_pendientes()
                entrada = input("\nIngrese los índices a marcar como revisados (ej: 0 1 2) o 'salir': ").strip()
                if entrada.lower() == "salir":
                    break

                indices = entrada.split()
                if not indices:
                    print(" No ingresaste ningún índice.")
                    continue

                try:
                    indices = [int(i) for i in indices]
                except ValueError:
                    print(" Solo se permiten números.")
                    continue

                esperado = list(range(indices[0], indices[0] + len(indices)))
                if indices != esperado:
                    print("Los índices deben estar en orden consecutivo (ej: 0 1 2).")
                    continue

                for i in indices:
                    real_index = len(pila.pila) - 1 - i
                    if real_index < 0 or real_index >= len(pila.pila):
                        print(f"Índice inválido: {i}.")
                        break
                    if not pila.validar_orden_revisado(real_index):
                        print(f" No puedes marcar el documento {i} sin haber marcado los anteriores.")
                        break
                    pila.marcar_como_revisado(real_index)

        elif opcion == "3":
            if not pila.pila:
                print(" No hay documentos para eliminar.")
                continue
            while True:
                pila.mostrar_pendientes()
                confirmar = input("\n¿Deseas eliminar el documento en la cima? (s/n o 'salir'): ").strip().lower()
                if confirmar == "salir":
                    break
                elif confirmar == "s":
                    cima = len(pila.pila) - 1
                    pila.eliminar(cima)
                elif confirmar == "n":
                    continue
                else:
                    print(" Opción inválida.")

        elif opcion == "4":
            while True:
                confirmar = input("\n¿Eliminar TODOS los documentos revisados? (s/n o 'salir'): ").strip().lower()
                if confirmar == "salir":
                    break
                elif confirmar == "s":
                    pila.eliminar_revisados()
                    break
                elif confirmar == "n":
                    break
                else:
                    print(" Opción inválida.")

        elif opcion == "5":
            pila.mostrar_pendientes()

        elif opcion == "6":
            print(" Saliendo del sistema.")
            break

        else:
            print(" Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
