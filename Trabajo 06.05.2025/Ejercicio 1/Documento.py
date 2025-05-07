class Documento:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.revisado = False

    def marcar_revisado(self):
        self.revisado = True

    def __str__(self):
        estado = " Revisado" if self.revisado else " Pendiente"
        return f"{self.descripcion} - {estado}"
