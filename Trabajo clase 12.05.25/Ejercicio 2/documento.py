# Clase que representa un documento a imprimir
class Documento:
    def __init__(self, nombre, usuario, paginas):
        self.nombre = nombre
        self.usuario = usuario
        self.paginas = paginas

# Clase Nodo para la cola de impresión
class Nodo:
    def __init__(self, documento):
        self.documento = documento
        self.siguiente = None
