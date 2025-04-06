class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print(f"\nNombre del estudiante: {self.nombre}")
        print(f"Nota: {self.nota}")

    def verificar_aprobacion(self):
        if self.nota >= 70:
            print("✅ El estudiante ha aprobado.")
        else:
            print("❌ El estudiante no ha aprobado.")
