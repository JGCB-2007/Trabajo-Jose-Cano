# Este archivo contiene la implementación de una cola de prioridad

from nodo import NodoPrioridad

class ColaPrioridad:
    def __init__(self):
        self.frente = None 

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, nombre, prioridad):
        nuevo = NodoPrioridad(nombre, prioridad)
        if self.esta_vacia() or prioridad < self.frente.prioridad:
            nuevo.siguiente = self.frente
            self.frente = nuevo
        else:
            actual = self.frente
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente

            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    def desencolar(self):
        if self.esta_vacia():
            return None
        nodo = self.frente
        self.frente = self.frente.siguiente
        return nodo

    def mostrar(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.append((actual.nombre, actual.prioridad))
            actual = actual.siguiente
        return elementos