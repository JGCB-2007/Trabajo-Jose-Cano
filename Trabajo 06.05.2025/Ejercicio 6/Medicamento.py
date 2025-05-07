class Medicamento:
    def __init__(self, nombre, lote):
        self.nombre = nombre
        self.lote = lote

    def __str__(self):
        return f"{self.nombre} (Lote {self.lote})"
