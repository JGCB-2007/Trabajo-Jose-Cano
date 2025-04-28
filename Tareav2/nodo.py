# Definimos la clase Nodo
class Nodo:
    # Constructor: recibe un objeto 'estudiante'
    def __init__(self, estudiante):
        self.estudiante = estudiante  # Guarda el estudiante dentro del nodo
        self.siguiente = None          # Apunta al siguiente nodo en la lista (por defecto no apunta a nadie)
