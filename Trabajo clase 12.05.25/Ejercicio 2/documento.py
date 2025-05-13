# documento.py

class Documento:
    def __init__(self, nombre, usuario, paginas):
        self.nombre = nombre
        self.usuario = usuario
        self.paginas = paginas

class Nodo:
    def __init__(self, documento):
        self.documento = documento
        self.siguiente = None
