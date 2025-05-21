# Este archivo define la estructura de un nodo con prioridad
class NodoPrioridad:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre          
        self.prioridad = prioridad    
        self.siguiente = None         