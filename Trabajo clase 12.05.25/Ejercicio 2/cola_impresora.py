# cola_impresora.py

from documento import Nodo, Documento

class ColaImpresion:
    def __init__(self):
        self.frente = None
        self.final = None
        self.documento_actual = None

    def agregar_documento(self, nombre, usuario, paginas):
        if not nombre or not usuario or paginas <= 0:
            print(" Datos inválidos. Verifique nombre, usuario y páginas.")
            return

        nuevo_documento = Documento(nombre, usuario, paginas)
        nuevo_nodo = Nodo(nuevo_documento)

        if self.final is None:
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

        print(f" Documento '{nombre}' de '{usuario}' agregado a la cola ({paginas} páginas).")

    def procesar_documento(self):
        if self.frente is None:
            print(" No hay documentos en la cola.")
            return

        self.documento_actual = self.frente.documento
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None

        doc = self.documento_actual
        print(f" Imprimiendo: '{doc.nombre}' de {doc.usuario} ({doc.paginas} páginas)")

    def mostrar_cola(self):
        if self.frente is None:
            print(" La cola de impresión está vacía.")
        else:
            print("\n Documentos en espera:")
            actual = self.frente
            i = 1
            while actual is not None:
                d = actual.documento
                print(f"{i}. {d.nombre} - {d.usuario} - {d.paginas} páginas")
                actual = actual.siguiente
                i += 1

    def mostrar_actual(self):
        if self.documento_actual:
            d = self.documento_actual
            print(f" Documento en impresión: '{d.nombre}' - {d.usuario} - {d.paginas} páginas")
        else:
            print(" No se está imprimiendo ningún documento actualmente.")
