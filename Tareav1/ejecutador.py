# Importamos las clases necesarias
from Estudiante import Estudiante
from listaenlazada import ListaEnlazada

# Creamos un conjunto para llevar control de los IDs (carnets) ya registrados
ids_usados = set()

# Función para pedir los datos de un nuevo estudiante
def pedir_estudiante():
    while True:
        carnet = input("Carnet (ID): ")
        # Validamos que el carnet no se haya registrado antes
        if carnet in ids_usados:
            print("⚠️ Este carnet ya fue registrado. Intente con otro.")
        else:
            ids_usados.add(carnet)  # Registramos el nuevo carnet
            break

    # Solicitamos el resto de los datos del estudiante
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (m): "))
    sexo = input("Sexo (M/F): ")
    promedio = float(input("Promedio: "))

    # Devolvemos un objeto Estudiante con los datos ingresados
    return Estudiante(carnet, nombres, apellidos, peso, estatura, sexo, promedio)

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Ingresar nuevo estudiante")
    print("2. Mostrar estudiantes ordenados")
    print("3. Salir")

# Función principal del programa
def main():
    estudiantes_guardados = []  # Lista para almacenar los estudiantes ingresados

    while True:
        mostrar_menu()  # Mostramos el menú de opciones
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para ingresar un nuevo estudiante
            estudiante = pedir_estudiante()
            estudiantes_guardados.append(estudiante)
            print(" Estudiante agregado correctamente.")

        elif opcion == "2":
            # Opción para mostrar estudiantes ordenados
            if not estudiantes_guardados:
                print(" No hay estudiantes registrados.")
                continue  # Regresa al menú si no hay estudiantes

            # Validación para escoger un campo correcto de ordenamiento
            campos_validos = ['carnet', 'nombres', 'apellidos', 'peso', 'estatura', 'sexo', 'promedio']
            parametro = input(f"Ingrese el campo por el cual ordenar {campos_validos}: ").strip().lower()

            while parametro not in campos_validos:
                print("Campo no válido. Intente de nuevo.")
                parametro = input(f"Ingrese el campo por el cual ordenar {campos_validos}: ").strip().lower()

            # Creamos una nueva lista enlazada ordenada según el campo elegido
            lista = ListaEnlazada(parametro)
            for estudiante in estudiantes_guardados:
                lista.insertar_ordenado(estudiante)

            print(f"\n Estudiantes ordenados por '{parametro}':\n")
            lista.mostrar()  # Mostramos los estudiantes ordenados

        elif opcion == "3":
            # Opción para salir del programa
            print(" Saliendo del programa...")
            break

        else:
            # Caso de opción inválida
            print(" Opción no válida.")

# Verifica que el archivo se esté ejecutando directamente
if __name__ == "__main__":
    main()
