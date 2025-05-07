from Pan import Pan

class Bandeja:
    def __init__(self):
        self.panes = []

    def agregar_pan(self, tipo):
        self.panes.append(Pan(tipo))

    def vender_pan(self):
        if not self.panes:
            print("No hay panes para vender.")
        else:
            vendido = self.panes.pop()
            print(f"Se vendió: {vendido}")

    def ver_pan_listo(self):
        if not self.panes:
            print("No hay panes disponibles.")
        else:
            print(f"Listo para vender: {self.panes[-1]}")

    def mostrar_bandeja(self):
        if not self.panes:
            print("La bandeja está vacía.")
        else:
            print("Bandeja de panes (de arriba hacia abajo):")
            for i, pan in enumerate(reversed(self.panes)):
                print(f"[{i}] {pan}")
