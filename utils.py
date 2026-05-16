# utils.py - Funciones auxiliares
import re
from datetime import datetime

def limpiar_texto(texto):
    """Limpia el texto: minúsculas, sin signos de puntuación"""
    texto = texto.lower()
    texto = re.sub(r'[¿¡!?.,;:()\[\]{}]', '', texto)
    return texto.strip()

def validar_nombre(nombre):
    """Valida que el nombre no esté vacío y tenga al menos 2 caracteres"""
    if not nombre or len(nombre.strip()) < 2:
        return False, "⚠️ El nombre debe tener al menos 2 caracteres"
    return True, ""

def obtener_timestamp():
    """Devuelve la hora actual en formato HH:MM"""
    return datetime.now().strftime("%H:%M")