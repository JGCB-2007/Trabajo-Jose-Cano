from Saco import Saco

class CamionPila:
    def __init__(self):
        self.pila = []

    def apilar_saco(self, producto, peso):
        self.pila.append(Saco(producto, peso))  # push

    def descargar_saco(self):
        if not self.pila:
            print("No hay sacos para descargar.")
        else:
            saco = self.pila.pop()  # pop
            print(f"Saco descargado: {saco}")

    def ver_saco_encima(self):
        if not self.pila:
            print("No hay sacos cargados.")
        else:
            print(f"Saco encima: {self.pila[-1]}")  # peek

    def mostrar_sacos(self):
        if not self.pila:
            print("No hay sacos en el camión.")
        else:
            print("Sacos apilados (último arriba):")
            for i, saco in enumerate(reversed(self.pila)):
                print(f"[{i}] {saco}")
