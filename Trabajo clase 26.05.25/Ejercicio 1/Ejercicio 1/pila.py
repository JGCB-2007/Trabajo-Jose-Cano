from nodo import Nodo

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def desapilar(self):
        if self.esta_vacia():
            return None
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        return valor

    def esta_vacia(self):
        return self.cima is None

    def ver_pila(self):
        actual = self.cima
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos
