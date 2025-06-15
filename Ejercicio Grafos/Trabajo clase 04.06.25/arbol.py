from nodo import Nodo

class ArbolBin:
    def __init__(self):  # También corregí _init_
        self.raiz = None

    def insert(self, valor):
        self.raiz = self._insertarecursiva(self.raiz, valor)

    def _insertarecursiva(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.left = self._insertarecursiva(nodo.left, valor)
        else:
            nodo.right = self._insertarecursiva(nodo.right, valor)
        return nodo

    def buscar(self, valor):
        return self._buscarecursiva(self.raiz, valor)

    def _buscarecursiva(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscarecursiva(nodo.left, valor)
        else:
            return self._buscarecursiva(nodo.right, valor)

    def recorrido_inorden(self):
        self._inorden(self.raiz)
        print()

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.left)
            print(nodo.valor, end=' ')
            self._inorden(nodo.right)

    def recorrido_preorden(self):
        self._preorden(self.raiz)
        print()

    def _preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=' ')
            self._preorden(nodo.left)
            self._preorden(nodo.right)

    def recorrido_postorden(self):
        self._postorden(self.raiz)
        print()

    def _postorden(self, nodo):
        if nodo:
            self._postorden(nodo.left)
            self._postorden(nodo.right)
            print(nodo.valor, end=' ')
