class Cola:
    def __init__(self, tamaño):
        self.items = [None] * tamaño
        self.frente = 0
        self.final = 0
        self.tamaño = tamaño

    def encolar(self, item):
        if self.final < self.tamaño:
            self.items[self.final] = item
            self.final += 1
        else:
            print("Cola llena.")

    def desencolar(self):
        if not self.esta_vacia():
            item = self.items[self.frente]
            self.frente += 1
            return item
        return None

    def esta_vacia(self):
        return self.frente == self.final

    def longitud(self):
        return self.final - self.frente

    def __str__(self):
        return str(self.items[self.frente:self.final])
