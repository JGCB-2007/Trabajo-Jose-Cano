# Importamos las clases necesarias
import re
from Estudiante import Estudiante
from listaenlazada import ListaEnlazada
from validaciones import validaciones  # Importamos la función de validaciones

# Función para pedir un estudiante con validaciones
def pedir_estudiante(ids_usados):
    while True:
        # Pedir carnet (ID) y validar que no se repita
        while True:
            carnet = input("Carnet (ID): ")

            if not carnet.isdigit() or len(carnet) < 5:
                print(" El carnet debe ser numérico y tener al menos 5 dígitos.")
                continue

            # Verificar si el carnet ya está registrado
            if carnet in ids_usados:
                print(" Este carnet ya fue registrado. Intente con otro.")
                continue  # Pedir un carnet nuevo
            else:
                ids_usados.add(carnet)  # Añadir carnet al conjunto de IDs usados
                break  # Si todo está bien, salir del ciclo

        # Pedir nombres y validar
        while True:
            nombres = input("Nombres: ")
            if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombres):
                print(" Nombre inválido. Solo se permiten letras y espacios.")
                continue
            break

        # Pedir apellidos y validar
        while True:
            apellidos = input("Apellidos: ")
            if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", apellidos):
                print("Apellido inválido. Solo se permiten letras y espacios.")
                continue
            break

        # Validar peso, estatura, sexo y promedio
        while True:
            try:
                peso = float(input("Peso (kg): "))
                if peso <= 0:
                    print(" El peso debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("Ingrese un número válido para el peso.")

        while True:
            try:
                estatura = float(input("Estatura (m): "))
                if estatura <= 0 or estatura > 3:
                    print(" La estatura debe ser un número positivo y menor que 3 metros.")
                    continue
                break
            except ValueError:
                print(" Ingrese un número válido para la estatura.")

        while True:
            sexo = input("Sexo (M/F): ").upper()
            if sexo not in ['M', 'F']:
                print(" Sexo inválido. Debe ser 'M' o 'F'.")
                continue
            break

        while True:
            try:
                promedio = float(input("Promedio: "))
                if promedio < 0 or promedio > 100:
                    print(" El promedio debe estar entre 0 y 100.")
                    continue
                break
            except ValueError:
                print(" Ingrese un número válido para el promedio.")

        # Llamamos a la función de validaciones
        error = validaciones(carnet, nombres, apellidos, peso, estatura, sexo, promedio)
        if error:
            print(error)
        else:
            # Si todo es correcto, crear y devolver el objeto Estudiante
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
    ids_usados = set()  # Conjunto para llevar control de los IDs (carnets) ya registrados

    while True:
        mostrar_menu()  # Mostramos el menú de opciones
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para ingresar un nuevo estudiante
            estudiante = pedir_estudiante(ids_usados)
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
                print(" Campo no válido. Intente de nuevo.")
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
