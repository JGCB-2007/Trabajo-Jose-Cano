from nodo import Nodo

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, valor):
        nuevo = Nodo(valor)
        if self.esta_vacia():
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    def esta_vacia(self):
        return self.frente is None

    def ver_cola(self):
        actual = self.frente
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos
