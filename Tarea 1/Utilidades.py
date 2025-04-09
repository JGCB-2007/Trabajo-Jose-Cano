# Utilidades.py
# Autor:Jose Cano y Freddy Perarla
# Fecha: 2025-04-09
# Versión: 1.0

#Imprime el menu
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Registrar nuevo estudiante")
    print("2. Agregar calificación a un estudiante")
    print("3. Mostrar información de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")

#Sirve para verificar que un valor sea un entero positivo
def validar_entero_positivo(valor):
    try:
        numero = int(valor)
        if numero > 0:
            return numero
        else:
            print("El número debe ser positivo.")
    except ValueError:
        print("Debe ingresar un número entero.")
    return None

#Busca un estudiante por su nombre dentro de una lista. 
def buscar_estudiante(nombre, lista_estudiantes):
    for estudiante in lista_estudiantes:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante
    return None
