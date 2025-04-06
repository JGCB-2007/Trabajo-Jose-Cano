def pedir_datos():
    nombre = input("Ingrese el nombre del estudiante: ")
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante: "))
            return nombre, nota
        except ValueError:
            print("⚠️ Error: Ingrese una nota válida (número).")