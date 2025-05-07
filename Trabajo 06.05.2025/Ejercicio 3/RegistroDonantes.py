from Donante import Donante

class RegistroDonantes:
    def __init__(self):
        self.pila = []

    def registrar_donante(self, nombre, tipo_sangre):
        self.pila.append(Donante(nombre, tipo_sangre))

    def revertir_ultimo(self):
        if not self.pila:
            print("No hay donantes para revertir.")
        else:
            eliminado = self.pila.pop()
            print(f"Se ha revertido el registro de: {eliminado}")

    def mostrar_donante_actual(self):
        if not self.pila:
            print("No hay donantes en proceso.")
        else:
            print(f"Donante actual en proceso: {self.pila[-1]}")

    def mostrar_todos(self):
        if not self.pila:
            print("No hay donantes registrados.")
        else:
            print("Lista de donantes (último arriba):")
            for i, donante in enumerate(reversed(self.pila)):
                print(f"[{i}] {donante}")
