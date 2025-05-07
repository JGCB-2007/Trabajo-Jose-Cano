from Tarea import Tarea

class PilaTareas:
    def __init__(self):
        self.pila = []

    def agregar_tarea(self, estudiante, titulo):#push
        self.pila.append(Tarea(estudiante, titulo))

    def revisar_tarea(self):#pop
        if not self.pila:
            print("No hay tareas para revisar.")
        else:
            tarea = self.pila.pop()
            print(f"Se ha revisado: {tarea}")

    def ver_siguiente_tarea(self):#peek
        if not self.pila:
            print("No hay tareas en espera.")
        else:
            print(f"Siguiente tarea a revisar: {self.pila[-1]}")

    def mostrar_tareas(self):
        if not self.pila:
            print("No hay tareas registradas.")
        else:
            print("Tareas pendientes (última arriba):")
            for i, tarea in enumerate(reversed(self.pila)):
                print(f"[{i}] {tarea}")
