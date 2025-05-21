# pila.py
class Pila:
    def __init__(self):
        self.items = []

        # Retorna True si la pila está vacía
    def esta_vacia(self):
        return len(self.items) == 0

        # Agrega un elemento al tope de la pila
    def apilar(self, item):
        self.items.append(item)

        # Elimina y retorna el elemento del tope de la pila (último que entró)
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

        # Retorna el número de elementos en la pila
    def tamaño(self):
        return len(self.items)