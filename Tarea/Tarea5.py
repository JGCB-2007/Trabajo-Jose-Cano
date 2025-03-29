while True:  
    import math

    print("=" * 50)
    print("CÁLCULO DE SUPERFICIES")
    print("=" * 50)
    print("1. Cuadrado       lado * lado")
    print("2. Círculo        pi * radio * radio")
    print("3. Rectángulo     base * altura")
    print("4. Trapecio       (base1 + base2) * altura / 2")
    print("5. Triángulo      (base * altura) / 2")
    print("=" * 50)

    opcion = int(input("Seleccione una opción (1-5): "))

    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado * lado
    elif opcion == 2:
        radio = float(input("Ingrese el radio del círculo: "))
        area = math.pi * radio * radio
    elif opcion == 3:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
    elif opcion == 4:
        base1 = float(input("Ingrese la base mayor del trapecio: "))
        base2 = float(input("Ingrese la base menor del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        area = (base1 + base2) * altura / 2
    elif opcion == 5:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
    else:
        print("Opción inválida.")
        exit()

    print(f"El área calculada es: {area:.2f}")
    repetir= input("¿Quieres repetir el programa? (si/no):").strip().lower()
    if repetir == "no":
        print("Se acabooo")
        break