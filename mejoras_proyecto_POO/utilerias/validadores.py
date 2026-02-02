"""Módulo con funciones de validación reutilizables"""

def validar_cadena_no_vacia(valor: str, nombre_campo: str = "valor") -> str:
    """Valida que una cadena no esté vacía"""
    if not valor or not valor.strip():
        raise ValueError(f"{nombre_campo} no puede estar vacío")
    return valor.strip()

def validar_numero_positivo(valor: int, nombre_campo: str = "valor") -> int:
    """Valida que un número sea positivo"""
    if valor <= 0:
        raise ValueError(f"{nombre_campo} debe ser un número positivo")
    return valor

def validar_opcion_menu(opcion: str, opciones_validas: list) -> bool:
    """Valida si una opción de menú es válida"""
    return opcion in opciones_validas