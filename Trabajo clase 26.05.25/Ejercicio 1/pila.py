class Pila:
    def __init__(self, tamaño):
        self.items = [None] * tamaño
        self.tope = 0
        self.tamaño = tamaño

    def apilar(self, item):
        if self.tope < self.tamaño:
            self.items[self.tope] = item
            self.tope += 1
        else:
            print("Pila llena.")

    def desapilar(self):
        if not self.esta_vacia():
            self.tope -= 1
            return self.items[self.tope]
        return None

    def esta_vacia(self):
        return self.tope == 0

    def __str__(self):
        return str(self.items[self.tope - 1::-1])
