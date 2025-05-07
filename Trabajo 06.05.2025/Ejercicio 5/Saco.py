class Saco:
    def __init__(self, producto, peso):
        self.producto = producto
        self.peso = peso  # en kg

    def __str__(self):
        return f"Saco de {self.producto} - {self.peso} kg"
