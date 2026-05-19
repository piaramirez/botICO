"""
================================================================
FUNCIONES AUXILIARES - PROYECTO chatbotICO
================================================================
Fecha: 18 de mayo de 2026
Escuela: Universidad Nacional Autónoma de México (UNAM) 
         Facultad de Estudios Superiores Aragón
Grupo: 2907
Materia: Inteligencia Artificial
Docente: MARTIN ROMERO UGALDE
Estudiante: Ramírez Alcántara Pedro Antonio
            Victor Flores Felix Omar

MÓDULO DE UTILERÍAS

DESCRIPCIÓN:
============
Este módulo contiene funciones auxiliares reutilizables en todo el
proyecto BotICO. Proporciona herramientas para:
- Limpieza y normalización de texto (procesamiento de lenguaje natural)
- Validación de datos de entrada del usuario
- Manejo de fechas y timestamps

FUNCIONALIDADES PRINCIPALES:
=============================
1. limpiar_texto(): Normaliza texto para matching difuso
2. validar_nombre(): Valida nombres de usuario en registro
3. obtener_timestamp(): Genera timestamps para mensajes
================================================================
"""

import re
from datetime import datetime


def limpiar_texto(texto):
    """
    Limpia y normaliza una cadena de texto para facilitar su procesamiento.
    
    Esta función es fundamental para el sistema de matching difuso (NLP básico)
    que permite al bot entender consultas escritas en texto libre aunque
    contengan errores tipográficos, mayúsculas inconsistentes o puntuación.
    
    PROCESO DE LIMPIEZA:
    1. Convertir todo el texto a minúsculas (elimina diferencias por mayúsculas)
    2. Eliminar signos de puntuación y caracteres especiales
    3. Eliminar espacios al inicio y final (strip)
    
    SÍMBOLOS ELIMINADOS:
    - Signos de interrogación: ¿ ?
    - Signos de exclamación: ¡ !
    - Puntuación básica: . , ; : ( ) [ ] { }
    
    Args:
        texto (str): Cadena de texto a limpiar (puede contener mayúsculas,
                    acentos, signos de puntuación, etc.)
    
    Returns:
        str: Texto limpio en minúsculas, sin puntuación y sin espacios extras.
             Ideal para comparaciones y búsqueda de palabras clave.
    
    Ejemplos:
        >>> limpiar_texto("¡Hola! ¿Cómo estás?")
        "hola como estas"
        
        >>> limpiar_texto("REINSCRIPCIÓN, POR FAVOR.")
        "reinscripcion por favor"
        
        >>> limpiar_texto("  Servicio   Social  ")
        "servicio   social"  # Mantiene espacios entre palabras
    
    NOTA:
        Este limpiador NO elimina acentos diacríticos (á, é, í, ó, ú, ü).
        Para eliminarlos se necesitaría usar unicodedata.normalize().
        En español, las búsquedas suelen ser tolerantes a acentos.
    """
    # Convertir a minúsculas (normalización de mayúsculas)
    texto = texto.lower()
    
    # Eliminar signos de puntuación y caracteres especiales
    # El patrón [¿¡!?.,;:()\[\]{}] encuentra cualquier carácter dentro de los corchetes
    # Los corchetes dobles [[]] son necesarios para incluir [ y ] como literales
    texto = re.sub(r'[¿¡!?.,;:()\[\]{}]', '', texto)
    
    # Eliminar espacios al inicio y final
    return texto.strip()


def validar_nombre(nombre):
    """
    Valida que el nombre ingresado por el usuario sea aceptable.
    
    Esta función se utiliza durante el proceso de registro para garantizar
    que el usuario proporcione un nombre válido antes de continuar.
    
    CRITERIOS DE VALIDACIÓN:
    - El nombre no puede estar vacío
    - El nombre debe tener al menos 2 caracteres (después de limpiar espacios)
    - Se permite cualquier carácter (letras, números, símbolos)
    
    Args:
        nombre (str): Nombre ingresado por el usuario (puede contener espacios)
    
    Returns:
        tuple: (bool, str) donde:
            - bool: True si el nombre es válido, False en caso contrario
            - str: Mensaje de error (vacío si es válido)
    
    Ejemplos:
        >>> validar_nombre("Pedro")
        (True, "")
        
        >>> validar_nombre("A")  # Solo un carácter
        (False, "⚠️ El nombre debe tener al menos 2 caracteres")
        
        >>> validar_nombre("  ")  # Solo espacios
        (False, "⚠️ El nombre debe tener al menos 2 caracteres")
        
        >>> validar_nombre("María José")
        (True, "")
    
    NOTAS DE USO:
        - Esta validación es básica y no verifica que el nombre sea "real"
        - Se permite cualquier Unicode (acentos, eñes, caracteres especiales)
        - Los espacios en blanco se ignoran para el conteo de caracteres
        - El mensaje de error está formateado con emoji ⚠️ para UI amigable
    """
    # Eliminar espacios al inicio y final para validación
    nombre_limpio = nombre.strip()
    
    # Verificar que no esté vacío y tenga al menos 2 caracteres
    if not nombre_limpio or len(nombre_limpio) < 2:
        return False, "⚠️ El nombre debe tener al menos 2 caracteres"
    
    # Nombre válido
    return True, ""


def obtener_timestamp():
    """
    Devuelve la hora actual formateada para mostrar en los mensajes del chat.
    
    Esta función genera un timestamp legible para humanos que se muestra
    junto a cada mensaje en la interfaz de usuario.
    
    FORMATO DE SALIDA:
    - HH:MM en formato 24 horas (00:00 a 23:59)
    - Sin segundos ni fecha (solo hora y minuto)
    
    Returns:
        str: Hora actual en formato "HH:MM"
    
    Ejemplos:
        Si son las 2:30:45 PM → "14:30"
        Si son las 9:05:00 AM → "09:05"
        Si es medianoche → "00:00"
    
    NOTAS:
        - Utiliza la hora del sistema donde se ejecuta la aplicación
        - El formato es consistente con el diseño de la UI
        - Los mensajes del bot y del usuario muestran el mismo formato
        - La función es pura (no modifica estado global)
    
    VENTAJAS:
        - Simple y legible para el usuario
        - No ocupa mucho espacio en la burbuja del chat
        - Suficiente para contexto conversacional
    """
    return datetime.now().strftime("%H:%M")