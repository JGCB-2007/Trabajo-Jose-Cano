import re

#Valida que el nombre solo tenga letras y espacios
def validar_nombre_usuario(usuario):
    return re.fullmatch(r'[A-Za-zÁÉÍÓÚáéíóúÑñ ]+', usuario.strip()) is not None

    #Valida que el número de páginas sea un entero positivo.

def validar_paginas(paginas):

    return isinstance(paginas, int) and paginas > 0
