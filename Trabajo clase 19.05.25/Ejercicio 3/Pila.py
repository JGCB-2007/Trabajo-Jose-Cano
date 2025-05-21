# Este módulo define la estructura de una pila (LIFO)
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

        # Agrega un elemento al tope de la pila
    def apilar(self, item):
        self.items.append(item)


        # Elimina y retorna el último elemento agregado (top)
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None 

        # Retorna el elemento en la cima sin eliminarlo
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

        # Retorna la cantidad de elementos en la pila
    def tamaño(self):
        return len(self.items)