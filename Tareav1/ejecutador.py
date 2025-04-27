from Estudiante import Estudiante
from listaenlazada import ListaEnlazada

ids_usados = set()

def pedir_estudiante():
    while True:
        carnet = input("Carnet (ID): ")
        if carnet in ids_usados:
            print("⚠️ Este carnet ya fue registrado. Intente con otro.")
        else:
            ids_usados.add(carnet)
            break

    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (m): "))
    sexo = input("Sexo (M/F): ")
    promedio = float(input("Promedio: "))
    return Estudiante(carnet, nombres, apellidos, peso, estatura, sexo, promedio)

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Ingresar nuevo estudiante")
    print("2. Mostrar estudiantes ordenados")
    print("3. Salir")

def main():
    estudiantes_guardados = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante = pedir_estudiante()
            estudiantes_guardados.append(estudiante)
            print("✅ Estudiante agregado correctamente.")
        elif opcion == "2":
            if not estudiantes_guardados:
                print("⚠️ No hay estudiantes registrados.")
                continue

            campos_validos = ['carnet', 'nombres', 'apellidos', 'peso', 'estatura', 'sexo', 'promedio']
            parametro = input(f"Ingrese el campo por el cual ordenar {campos_validos}: ").strip().lower()

            while parametro not in campos_validos:
                print("Campo no válido. Intente de nuevo.")
                parametro = input(f"Ingrese el campo por el cual ordenar {campos_validos}: ").strip().lower()

            lista = ListaEnlazada(parametro)
            for estudiante in estudiantes_guardados:
                lista.insertar_ordenado(estudiante)

            print(f"\n📋 Estudiantes ordenados por '{parametro}':\n")
            lista.mostrar()
        elif opcion == "3":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
