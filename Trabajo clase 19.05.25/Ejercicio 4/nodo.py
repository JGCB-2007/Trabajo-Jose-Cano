# Este archivo define la clase NodoCancion que representa una canción en la lista enlazada
class NodoCancion:
    def __init__(self, nombre):
        self.nombre = nombre  
        self.siguiente = None  
        self.anterior = None   