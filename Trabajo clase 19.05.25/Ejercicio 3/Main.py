# Módulo principal que pide al usuario una cadena y verifica los paréntesis

from Vereficador import esta_balanceado

def main():
    while True:
        cadena = input("Ingrese una cadena de texto con paréntesis: ").strip()
        if not cadena:
            print("La cadena ingresada no es válida.")
        else:
            if esta_balanceado(cadena):
                print("Los paréntesis están balanceados.")
            else:
                print("Los paréntesis NO están balanceados.")
        
        continuar = input("¿Desea verificar otra cadena? (s/n): ").strip().lower()
        if continuar != 's':
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()
