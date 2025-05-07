from Documento import Documento

class Pila_Documento:
    def __init__(self):
        self.pila = []

    def push(self, documento):
        self.pila.append(documento)
        print(f" Documento agregado: {documento.descripcion}")

    def eliminar(self, index):
        if 0 <= index < len(self.pila):
            eliminado = self.pila.pop(index)
            print(f"Documento eliminado: {eliminado.descripcion}")
        else:
            print("Índice no válido para eliminar.")

    def eliminar_revisados(self):
        originales = len(self.pila)
        self.pila = [doc for doc in self.pila if not doc.revisado]
        eliminados = originales - len(self.pila)
        print(f" Se eliminaron {eliminados} documento(s) revisado(s).")

    def mostrar_pendientes(self):
        if not self.pila:
            print(" No hay documentos en la pila.")
            return

        print("\n Documentos en la pila (de arriba hacia abajo):")
        for i, doc in enumerate(reversed(self.pila)):
            estado = "Listo" if doc.revisado else "Esperando"
            print(f"[{i}] {doc.descripcion} - {estado}")

    def marcar_como_revisado(self, index):
        if 0 <= index < len(self.pila):
            if not self.pila[index].revisado:
                self.pila[index].marcar_revisado()
                print(f" Documento marcado como revisado: {self.pila[index].descripcion}")
            else:
                print(f"ℹ Documento ya estaba revisado: {self.pila[index].descripcion}")
        else:
            print(" Índice no válido.")

    def validar_orden_revisado(self, index):
        """
        Permite marcar como revisado solo si todos los documentos más nuevos (más arriba en la pila)
        ya han sido revisados.
        """
        for i in range(index + 1, len(self.pila)):
            if not self.pila[i].revisado:
                return False
        return True
