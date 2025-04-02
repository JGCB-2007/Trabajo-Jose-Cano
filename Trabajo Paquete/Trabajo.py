import Paquete as mp

while True:
    num1 = mp.pedir_numero("Ingresa el primer número: ")
    num2 = mp.pedir_numero("Ingresa el segundo número: ")

    print("\nOperaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Todas")

    opcion = input("Elige una operación (1-4): ")

    if opcion == "1":
        resultado = mp.sumar(num1, num2)
        mp.mostrar_resultado("suma", resultado)
    elif opcion == "2":
        resultado = mp.restar(num1, num2)
        mp.mostrar_resultado("resta", resultado)
    elif opcion == "3":
        resultado = mp.multiplicar(num1, num2)
        mp.mostrar_resultado("multiplicación", resultado)
    elif opcion == "4":
        resultado = mp.dividir(num1, num2)
        mp.mostrar_resultado("división", resultado)
        
    elif opcion == "5":
        resultado = mp.sumar(num1, num2)
        mp.mostrar_resultado("suma", resultado)
        
        resultado = mp.restar(num1, num2)
        mp.mostrar_resultado("resta", resultado)
        
        resultado = mp.multiplicar(num1, num2)
        mp.mostrar_resultado("multiplicación", resultado)
        
        resultado = mp.dividir(num1, num2)
        mp.mostrar_resultado("división", resultado)
        
    else:
        print("Opción no válida. Inténtalo de nuevo.")

    if not mp.preguntar_repetir():
        print("¡Hasta luego!")
        break
