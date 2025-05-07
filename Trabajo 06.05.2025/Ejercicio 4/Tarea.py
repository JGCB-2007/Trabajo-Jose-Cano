class Tarea:
    def __init__(self, estudiante, titulo):
        self.estudiante = estudiante
        self.titulo = titulo

    def __str__(self):
        return f"Tarea: '{self.titulo}' de {self.estudiante}"
