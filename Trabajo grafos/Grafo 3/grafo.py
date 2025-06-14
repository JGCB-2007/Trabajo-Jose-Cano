# archivo: grafo.py
from collections import deque

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

    def bfs(self, inicio):
        if inicio not in self.adyacencia:
            return []
        visitados = set()
        orden = []
        cola = deque([inicio])
        while cola:
            actual = cola.popleft()
            if actual not in visitados:
                visitados.add(actual)
                orden.append(actual)
                vecinos = [v for v, _ in self.adyacencia[actual]]
                cola.extend([v for v in vecinos if v not in visitados])
        return orden

    def dfs(self, inicio):
        if inicio not in self.adyacencia:
            return []
        visitados = set()
        orden = []

        def recorrer(v):
            visitados.add(v)
            orden.append(v)
            for vecino, _ in self.adyacencia[v]:
                if vecino not in visitados:
                    recorrer(vecino)

        recorrer(inicio)
        return orden

    def es_conexo(self):
        if not self.adyacencia:
            return True
        if self.es_dirigido:
            raise ValueError("es_conexo solo aplica a grafos no dirigidos.")
        inicio = next(iter(self.adyacencia))
        visitados = set()
        cola = deque([inicio])
        while cola:
            actual = cola.popleft()
            if actual not in visitados:
                visitados.add(actual)
                vecinos = [v for v, _ in self.adyacencia[actual]]
                cola.extend([v for v in vecinos if v not in visitados])
        return len(visitados) == len(self.adyacencia)

    def encontrar_camino(self, inicio, fin):
        if inicio not in self.adyacencia or fin not in self.adyacencia:
            return []
        padres = {}
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)
        while cola:
            actual = cola.popleft()
            if actual == fin:
                break
            for vecino, _ in self.adyacencia[actual]:
                if vecino not in visitados:
                    padres[vecino] = actual
                    visitados.add(vecino)
                    cola.append(vecino)
        if fin not in padres and inicio != fin:
            return []
        camino = [fin]
        while camino[-1] != inicio:
            camino.append(padres[camino[-1]])
        camino.reverse()
        return camino

    def mostrar_grafo(self):
        for v in self.adyacencia:
            vecinos = ', '.join(f"{dest} (peso {peso})" for dest, peso in self.adyacencia[v])
            print(f"{v} -> {vecinos}")
