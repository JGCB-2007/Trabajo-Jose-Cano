while True:
    numero = input("Ingrese un número de tres cifras: ")
    
    if len(numero) != 3 or not numero.isdigit():
        print("Por favor, ingrese un número válido de tres cifras.")
        continue
    
    if numero == numero[::-1]:
        print(f"El número {numero} es igual al revés.")
    else:
        print(f"El número {numero} no es igual al revés.")
    
    repetir = input("¿Quieres probar otro número? (si/no): ").strip().lower()
    if repetir == "no":
        print("Se acabó.")
        break
