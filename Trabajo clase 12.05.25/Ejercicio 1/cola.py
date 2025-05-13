# cola.py

import re
from nodo import Nodo

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def insertar(self, dato):
        if not self.validar_nombre(dato):
            print("Nombre inválido. Use solo letras y espacios.")
            return

        nuevo = Nodo(dato)
        if self.final is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        print(f" Paciente '{dato}' registrado correctamente.")

    def eliminar(self):
        if self.frente is None:
            print(" La cola está vacía. No hay pacientes para atender.")
            return
        eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print(f" Paciente '{eliminado}' ha sido atendido.")

    def imprimir(self):
        if self.frente is None:
            print(" No hay pacientes en espera.")
        else:
            print("\n Lista de pacientes en espera:")
            actual = self.frente
            i = 1
            while actual is not None:
                print(f"{i}. {actual.dato}")
                actual = actual.siguiente
                i += 1

    def validar_nombre(self, nombre):
        return re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", nombre.strip()) is not None
