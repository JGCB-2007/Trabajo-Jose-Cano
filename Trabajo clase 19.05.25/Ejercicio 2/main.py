# Este archivo ejecuta el programa e interactúa con el usuario
from Inversor import invertir_frase  # Importamos la función desde inversor.py

def main():
    frase = input("Ingrese una frase: ")
    frase_invertida = invertir_frase(frase)
    print("Frase invertida:", frase_invertida)

if __name__ == "__main__":
    main()
