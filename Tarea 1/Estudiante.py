# Estudiante.py
# Autor:Jose Cano y Freddy Perarla
# Fecha: 2025-04-09
# Versión: 1.0


class Estudiante:
    #Este es el contrusctor se ejecuta automaticamente
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    #Agrega las calificaciones entre 0-100
    def agregar_calificacion(self, nota):
        if 0 <= nota <= 100:
            self.calificaciones.append(nota)
        else:
            print("La calificación debe estar entre 0 y 100.")
    #Aca se calcula el promedio, si no hay nota se devuelve 0
    def promedio(self):
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

#Muestra la nota del estudiantes en dos decimales 
    def mostrar_info(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.promedio():.2f}\n")
