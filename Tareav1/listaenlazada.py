from nodo import Nodo

class ListaEnlazada:
    def __init__(self, clave_orden):
        self.cabeza = None
        self.clave_orden = clave_orden

    def insertar_ordenado(self, estudiante):
        nuevo_nodo = Nodo(estudiante)
        valor_nuevo = getattr(estudiante, self.clave_orden)

        if self.cabeza is None or getattr(self.cabeza.estudiante, self.clave_orden) > valor_nuevo:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while (actual.siguiente is not None and
                   getattr(actual.siguiente.estudiante, self.clave_orden) <= valor_nuevo):
                actual = actual.siguiente

            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.estudiante)
            actual = actual.siguiente
