# Ejecutador.py
# Autor:Jose Cano y Freddy Perarla
# Fecha: 2025-04-09
# Versión: 1.0

from Estudiante import Estudiante
import Utilidades

def main():
    #se guardan todos los estudiantes
    estudiantes = []
    
    #bucle infinito hasta elegir la opcion 5
    while True:
        Utilidades.mostrar_menu()
        opcion = input("Seleccione una opción: ")

        #Agrega a los estudiantes
        if opcion == "1":
            nombre = input("Nombre del estudiante: ").strip()
            edad = None
            while edad is None:
                edad = Utilidades.validar_entero_positivo(input("Edad: "))
            carrera = input("Carrera: ").strip()
            estudiante = Estudiante(nombre, edad, carrera)
            estudiantes.append(estudiante)
            print("✅ Estudiante registrado con éxito.")

        #Agrega las notas
        elif opcion == "2":
            nombre = input("Nombre del estudiante: ").strip()
            estudiante = Utilidades.buscar_estudiante(nombre, estudiantes)
            if estudiante:
                try:
                    nota = float(input("Ingrese la calificación: "))
                    estudiante.agregar_calificacion(nota)
                except ValueError:
                    print("Ingrese un número válido.")
            else:
                print(" Estudiante no encontrado.")

        #Muestra la info del estudiante
        elif opcion == "3":
            nombre = input("Nombre del estudiante: ").strip()
            estudiante = Utilidades.buscar_estudiante(nombre, estudiantes)
            if estudiante:
                estudiante.mostrar_info()
            else:
                print("Estudiante no encontrado.")

        #Muestran todos los estudiante
        elif opcion == "4":
            if estudiantes:
                for e in estudiantes:
                    e.mostrar_info()
            else:
                print(" No hay estudiantes registrados.")

        #Sale del programa
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
#Ejecuta el codigo main solo si estas dentro del ejecutador
if __name__ == "__main__":
    main()
