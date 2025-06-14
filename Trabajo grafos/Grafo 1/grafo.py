# grafo.py

class Grafo:
    def __init__(self, es_dirigido=False):
        self.es_dirigido = es_dirigido
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.adyacencia[u].append((v, peso))
        if not self.es_dirigido:
            self.adyacencia[v].append((u, peso))

    def obtener_vecinos(self, vertice):
        return self.adyacencia.get(vertice, [])

    def existe_arista(self, u, v):
        return any(vecino == v for vecino, _ in self.adyacencia.get(u, []))

    def mostrar_grafo(self):
        for vertice in self.adyacencia:
            print(f"{vertice} -> {self.adyacencia[vertice]}")
