# Este archivo ejecuta el programa e interactúa con el usuario
from Inversor import invertir_frase  # Importamos la función desde inversor.py

def main():
    while True:
        frase = input("Ingrese una frase: ").strip()
        if not frase:
            print("La frase ingresada no es válida.")
        else:
            frase_invertida = invertir_frase(frase)
            print("Frase invertida:", frase_invertida)
            
            continuar = input("¿Desea invertir otra frase>? (s/n): ").strip().lower()
            if continuar != 's':
                print("Programa finalizado.")
                break

if __name__ == "__main__":
    main()