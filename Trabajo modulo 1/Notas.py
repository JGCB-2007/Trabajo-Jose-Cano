from ModuloEstudiante import Estudiante
from ModuloNota import pedir_datos

def main():
    nombre, nota = pedir_datos()
    alumno = Estudiante(nombre, nota)
    alumno.imprimir_datos()
    alumno.verificar_aprobacion()

if __name__ == "__main__":
    main()