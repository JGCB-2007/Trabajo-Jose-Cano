# Definimos la clase Estudiante
class Estudiante:
    # Método constructor: inicializa los atributos del estudiante
    def __init__(self, carnet, nombres, apellidos, peso, estatura, sexo, promedio):
        self.carnet = carnet          # Identificador único del estudiante
        self.nombres = nombres        # Nombres del estudiante
        self.apellidos = apellidos    # Apellidos del estudiante
        self.peso = peso              # Peso del estudiante en kilogramos
        self.estatura = estatura      # Estatura del estudiante en metros
        self.sexo = sexo              # Sexo del estudiante ('M' o 'F')
        self.promedio = promedio      # Promedio académico del estudiante

    # Método especial que define cómo se representará el estudiante como texto
    def __str__(self):
        # Devuelve una representación amigable del estudiante cuando se imprima
        return (f"{self.carnet} - {self.nombres} {self.apellidos}, "
                f"Peso: {self.peso}kg, Estatura: {self.estatura}m, "
                f"Sexo: {self.sexo}, Promedio: {self.promedio}")
