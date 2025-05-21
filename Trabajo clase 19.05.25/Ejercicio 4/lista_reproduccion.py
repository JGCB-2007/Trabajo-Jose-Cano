# Define la clase ListaReproduccion para manejar la lista enlazada de canciones

from nodo import NodoCancion

class ListaReproduccion:
    def __init__(self):
        self.inicio = None      
        self.actual = None         

    def agregar_cancion(self, nombre):
        nueva = NodoCancion(nombre)
        if self.inicio is None:
            self.inicio = nueva
            self.actual = nueva
        else:
            temp = self.inicio
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nueva
            nueva.anterior = temp

    def eliminar_cancion(self, nombre):
        temp = self.inicio
        while temp:
            if temp.nombre == nombre:
                if temp == self.inicio:
                    self.inicio = temp.siguiente
                    if self.inicio:
                        self.inicio.anterior = None
                else:
                    temp.anterior.siguiente = temp.siguiente
                    if temp.siguiente:
                        temp.siguiente.anterior = temp.anterior
                if self.actual == temp:
                    self.actual = temp.siguiente if temp.siguiente else temp.anterior
                return True
            temp = temp.siguiente
        return False

    def reproducir_siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return self.actual.nombre
        return None

    def reproducir_anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            return self.actual.nombre
        return None

    def mostrar_lista(self):
        canciones = []
        temp = self.inicio
        while temp:
            cancion = temp.nombre
            if temp == self.actual:
                cancion += " (en reproducción)"
            canciones.append(cancion)
            temp = temp.siguiente
        return canciones