# Contiene la implementación de una lista enlazada y función para buscar un valor

from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  

    def agregar(self, valor):
        """Agrega un nuevo nodo al final de la lista"""
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def buscar(self, valor):
        """Busca un valor en la lista enlazada"""
        actual = self.cabeza
        posicion = 0

        while actual:
            if actual.valor == valor:
                return posicion  
            actual = actual.siguiente
            posicion += 1

        return -1  

    def mostrar(self):
        """Devuelve una lista con los valores actuales"""
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
        return valores