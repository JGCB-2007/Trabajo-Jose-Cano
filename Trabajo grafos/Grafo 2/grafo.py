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

    def mostrar_grafo(self):
        for vertice, vecinos in self.adyacencia.items():
            print(f"{vertice} -> {vecinos}")

    def bfs(self, inicio):
        if inicio not in self.adyacencia:
            return []

        visitados = set()
        orden_visita = []
        cola = deque([inicio])

        while cola:
            actual = cola.popleft()
            if actual not in visitados:
                visitados.add(actual)
                orden_visita.append(actual)
                vecinos = [vecino for vecino, _ in self.adyacencia[actual]]
                cola.extend([v for v in vecinos if v not in visitados])

        return orden_visita

    def dfs(self, inicio):
        if inicio not in self.adyacencia:
            return []

        visitados = set()
        orden_visita = []

        def dfs_recursivo(v):
            visitados.add(v)
            orden_visita.append(v)
            for vecino, _ in self.adyacencia[v]:
                if vecino not in visitados:
                    dfs_recursivo(vecino)

        dfs_recursivo(inicio)
        return orden_visita
