from nodo import Nodo

# Definimos la clase ListaEnlazada
class ListaEnlazada:
    # Constructor: recibe la clave por la cual se va a ordenar la lista
    def __init__(self, clave_orden):
        self.cabeza = None              
        self.clave_orden = clave_orden  
    # Método para insertar un estudiante en orden
    def insertar_ordenado(self, estudiante):
        nuevo_nodo = Nodo(estudiante)  
        valor_nuevo = getattr(estudiante, self.clave_orden)  # Obtenemos el valor del atributo usado para ordenar

        # Caso 1: La lista está vacía o el nuevo estudiante debe ir al principio
        if self.cabeza is None or getattr(self.cabeza.estudiante, self.clave_orden) > valor_nuevo:
            nuevo_nodo.siguiente = self.cabeza  
            self.cabeza = nuevo_nodo          
        else:
            # Caso 2: Buscar la posición correcta para insertar
            actual = self.cabeza
            while (actual.siguiente is not None and
                   #se extrae el valor del campo del estudiante que se usará para ordenar, mediante getattr(estudiante, self.clave_orden).
                   getattr(actual.siguiente.estudiante, self.clave_orden) <= valor_nuevo):
                actual = actual.siguiente  # Avanzamos en la lista hasta encontrar el lugar adecuado

            # Insertamos el nuevo nodo en la posición correcta
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    # Método para mostrar todos los estudiantes en la lista
    def mostrar(self):
        actual = self.cabeza  # Comenzamos desde el primer nodo
        while actual is not None:
            print(actual.estudiante) 
            actual = actual.siguiente  
