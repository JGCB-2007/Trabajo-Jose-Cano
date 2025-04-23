class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def longitudLista(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def esta_vacia(self):
        return self.cabeza is None

    def imprimir_ultimo(self):
        if not self.cabeza:
            print("La lista está vacía")
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        print("Último valor de la lista:", actual.valor)

if __name__ == "__main__":
    lista = ListaEnlazada()

    n = int(input("¿Cuántos valores desea insertar al final? "))
    for _ in range(n):
        valor = int(input("Ingrese un valor: "))
        lista.insertar_final(valor)

    m = int(input("¿Cuántos valores desea insertar al inicio? "))
    for _ in range(m):
        valor = int(input("Ingrese un valor: "))
        lista.insertar_inicio(valor)

    lista.imprimir()
    print("Longitud de la lista:", lista.longitudLista())
    print("¿La lista está vacía?", lista.esta_vacia())
    lista.imprimir_ultimo()
