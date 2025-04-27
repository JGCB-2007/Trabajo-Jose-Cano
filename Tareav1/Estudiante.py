class Estudiante:
    def __init__(self, carnet, nombres, apellidos, peso, estatura, sexo, promedio):
        self.carnet = carnet
        self.nombres = nombres
        self.apellidos = apellidos
        self.peso = peso
        self.estatura = estatura
        self.sexo = sexo
        self.promedio = promedio

    def __str__(self):
        return f"{self.carnet} - {self.nombres} {self.apellidos}, Peso: {self.peso}kg, Estatura: {self.estatura}m, Sexo: {self.sexo}, Promedio: {self.promedio}"
