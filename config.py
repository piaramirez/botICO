# config.py - Configuración global del sistema

# Colores institucionales UNAM
AZUL_UNAM = "#003366"
AZUL_UNAM_CLARO = "#0a2f5a"
AZUL_UNAM_MEDIO = "#1a4a7a"
DORADO_UNAM = "#d4af37"
VERDE_UNAM = "#88b04b"
BLANCO = "#ffffff"
NEGRO = "#1e1e2e"

COLORS = {
    "fondo": AZUL_UNAM,
    "header": AZUL_UNAM_CLARO,
    "bot_bubble": AZUL_UNAM_MEDIO,
    "user_bubble": DORADO_UNAM,
    "estado": VERDE_UNAM,
    "titulo": DORADO_UNAM,
    "texto_bot": BLANCO,
    "texto_user": NEGRO,
    "boton_fondo": DORADO_UNAM,
    "boton_texto": AZUL_UNAM,
}

NOMBRE_APP = "BotICO"
INSTITUCION = "FES Aragón - Ingeniería en Computación"

# Umbral para matching difuso (si usas thefuzz después)
SIMILARITY_THRESHOLD = 70

# Archivo de log
LOG_FILE = "conversaciones.log"