# validaciones.py
import re

def validaciones(carnet, nombres, apellidos, peso, estatura, sexo, promedio):
    # Validar ID (Carnet)
    if not carnet.isdigit() or len(carnet) < 5:
        return " ID inválido. El carnet debe ser numérico y tener al menos 5 dígitos."
    
    # Validar Nombres y Apellidos (solo letras y espacios)
    if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombres):
        return " Nombre inválido. Solo se permiten letras y espacios."
    
    if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", apellidos):
        return " Apellido inválido. Solo se permiten letras y espacios."
    
    # Validar Peso (debe ser un número positivo)
    if peso <= 0:
        return " Peso inválido. Debe ser un número positivo."
    
    # Validar Estatura (debe ser un número positivo y menor que 3 metros)
    if estatura <= 0 or estatura > 3:
        return "Estatura inválida. Debe ser un número positivo y menor que 3 metros."
    
    # Validar Sexo (solo M o F)
    if sexo not in ['M', 'F']:
        return " Sexo inválido. Debe ser 'M' o 'F'."
    
    # Validar Promedio (debe estar entre 0 y 10)
    if promedio < 0 or promedio > 10:
        return "Promedio inválido. Debe estar entre 0 y 10."
    
    # Si todas las validaciones son correctas
    return None
