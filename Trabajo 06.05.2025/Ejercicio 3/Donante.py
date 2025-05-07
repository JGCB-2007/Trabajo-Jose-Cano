class Donante:
    def __init__(self, nombre, tipo_sangre):
        self.nombre = nombre
        self.tipo_sangre = tipo_sangre

    def __str__(self):
        return f"{self.nombre} ({self.tipo_sangre})"
