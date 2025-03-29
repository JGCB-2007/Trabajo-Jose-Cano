while True:
    vehiculo = input("Ingrese el tipo de vehículo (bicicleta, moto, carro, camion): ").lower()

    if vehiculo == "bicicleta":
        print("El importe a pagar es: 100 córdobas")
    elif vehiculo == "moto" or vehiculo == "carro":
        km = float(input("Ingrese la cantidad de kilómetros recorridos: "))
        total = km * 30
        print(f"El importe a pagar es: {total} córdobas")
    elif vehiculo == "camion":
        km = float(input("Ingrese la cantidad de kilómetros recorridos: "))
        toneladas = float(input("Ingrese la cantidad de toneladas: "))
        total = (km * 30) + (toneladas * 25)
        print(f"El importe a pagar es: {total} córdobas")
    else:
        print("Tipo de vehículo no válido.")

    repetir = input("¿Quieres repetir el programa? (Si/No): ").strip().lower()
    if repetir == "no":
        print("Se acabó.")
        break 
