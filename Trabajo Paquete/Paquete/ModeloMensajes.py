def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def mostrar_resultado(operacion, resultado):
    print(f"El resultado de la {operacion} es: {resultado}")

def preguntar_repetir():
    while True:
        respuesta = input("¿Quieres realizar otra operación? (s/n): ").strip().lower()
        if respuesta in ["s", "n"]:
            return respuesta == "s"
        print("Error: Responde con 's' para sí o 'n' para no.")