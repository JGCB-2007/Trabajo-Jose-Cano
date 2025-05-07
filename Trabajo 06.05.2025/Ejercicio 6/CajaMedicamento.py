from Medicamento import Medicamento

class CajaMedicamentos:
    def __init__(self):
        self.pila = []

    def apilar_medicamento(self, nombre, lote):
        self.pila.append(Medicamento(nombre, lote))  # PUSH

    def surtir_medicamento(self):
        if not self.pila:
            print(" No hay medicamentos para surtir.")
        else:
            med = self.pila.pop()  # POP
            print(f" Medicamento surtido: {med}")

    def ver_superior(self):
        if not self.pila:
            print(" No hay medicamentos en la caja.")
        else:
            print(f" Medicamento en la parte superior: {self.pila[-1]}")  # PEEK

    def mostrar_todos(self):
        if not self.pila:
            print(" La caja está vacía.")
        else:
            print("\n Medicamentos apilados (último arriba):")
            for i, med in enumerate(reversed(self.pila)):
                print(f"[{i}] {med}")
