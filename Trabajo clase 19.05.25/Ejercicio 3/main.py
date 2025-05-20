# Módulo principal que pide al usuario una cadena y verifica los paréntesis

from Vereficador import esta_balanceado 

def main():
    cadena = input("Ingrese una cadena con paréntesis: ")

    if esta_balanceado(cadena):
        print(" Los paréntesis están balanceados.")
    else:
        print(" Los paréntesis NO están balanceados.")
if __name__ == "__main__":
    main()
