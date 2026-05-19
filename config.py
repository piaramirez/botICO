"""
================================================================
CONFIGURACIÓN GLOBAL DEL SISTEMA - PROYECTO chatbotICO
================================================================
Fecha: 18 de mayo de 2026
Escuela: Universidad Nacional Autónoma de México (UNAM)
         Facultad de Estudios Superiores Aragón
Grupo: 2907
Materia: Inteligencia Artificial
Docente: MARTIN ROMERO UGALDE
Estudiante: Ramírez Alcántara Pedro Antonio
            Victor Flores Felix Omar
================================================================

Este módulo contiene toda la configuración global del sistema BotICO,
incluyendo:
- Paleta de colores institucionales de la UNAM
- Constantes de la aplicación (nombre, institución)
- Umbrales para algoritmos de matching difuso
- Configuración de archivos de log
"""

# ==============================
# 1. PALETA DE COLORES INSTITUCIONALES UNAM
# ==============================
# Los colores están basados en la identidad visual de la UNAM
# y la FES Aragón, adaptados para una interfaz moderna y accesible.

AZUL_UNAM = "#003366"
"""
Color azul institucional de la UNAM (tono principal).
Usado como fondo principal de la aplicación.
Representa: Identidad, confianza, seriedad académica.
"""

AZUL_UNAM_CLARO = "#0a2f5a"
"""
Variante más clara del azul institucional.
Usado para encabezados (headers) y elementos de fondo secundarios.
"""

AZUL_UNAM_MEDIO = "#1a4a7a"
"""
Variante media del azul institucional.
Usado para burbujas de chat del bot (bot_bubble).
Representa: Neutralidad, profesionalismo.
"""

DORADO_UNAM = "#d4af37"
"""
Color dorado institucional de la UNAM.
Usado para:
- Burbujas de chat del usuario (user_bubble)
- Títulos (titulo)
- Botones (boton_fondo)
Representa: Excelencia, prestigio, calidez.
"""

VERDE_UNAM = "#88b04b"
"""
Color verde complementario.
Usado para indicadores de estado (estado).
Representa: Éxito, conexión activa, positividad.
"""

BLANCO = "#ffffff"
"""
Color blanco puro.
Usado para texto del bot y contraste sobre fondos oscuros.
"""

NEGRO = "#1e1e2e"
"""
Color gris oscuro casi negro.
Usado para texto del usuario sobre fondos claros (dorado).
Más suave que el negro puro (#000000) para mejor legibilidad.
"""

# ==============================
# 2. DICCIONARIO DE COLORES PRINCIPAL
# ==============================
COLORS = {
    # Fondos
    "fondo": AZUL_UNAM,           # Fondo general de la aplicación
    "header": AZUL_UNAM_CLARO,    # Fondo de barras de título/header
    
    # Burbujas de chat
    "bot_bubble": AZUL_UNAM_MEDIO,   # Burbuja del bot (mensajes entrantes)
    "user_bubble": DORADO_UNAM,      # Burbuja del usuario (mensajes salientes)
    
    # Indicadores
    "estado": VERDE_UNAM,         # Color para indicador de estado (conectado/escribiendo)
    
    # Textos
    "titulo": DORADO_UNAM,        # Color para títulos y encabezados importantes
    "texto_bot": BLANCO,          # Texto dentro de las burbujas del bot
    "texto_user": NEGRO,          # Texto dentro de las burbujas del usuario
    
    # Botones
    "boton_fondo": DORADO_UNAM,   # Fondo de botones
    "boton_texto": AZUL_UNAM,     # Texto dentro de botones
}
"""
Diccionario central de colores para toda la interfaz.
Cada clave representa un elemento UI específico, facilitando:
- Cambios globales de tema
- Mantenimiento del código
- Consistencia visual en toda la aplicación
"""

# ==============================
# 3. INFORMACIÓN DE LA APLICACIÓN
# ==============================
NOMBRE_APP = "BotICO"
"""
Nombre comercial del chatbot.
ICO: Ingeniería en Computación.
"""

INSTITUCION = "FES Aragón - Ingeniería en Computación"
"""
Nombre completo de la institución educativa.
Se muestra en ventanas, headers y documentación.
"""

# ==============================
# 4. CONFIGURACIÓN DE ALGORITMOS
# ==============================
SIMILARITY_THRESHOLD = 70
"""
Umbral de similitud para algoritmos de matching difuso (ej: thefuzz).
Rango: 0-100
- Valores > 70: Coincidencia aceptable
- Valores < 70: Considerar como no coincidente
Se usa para:
  - Comparación de preguntas del usuario con la base de conocimiento
  - Matching de intenciones no exactas
  - Tolerancia a errores tipográficos
"""

# ==============================
# 5. CONFIGURACIÓN DE ARCHIVOS
# ==============================
LOG_FILE = "conversaciones.log"
"""
Nombre del archivo de log donde se almacenan las conversaciones.
Formato: Texto plano (.log)
Contenido:
  - Timestamp de cada mensaje
  - Remitente (usuario/bot)
  - Contenido del mensaje
  - Metadatos de la sesión

Uso:
  - Depuración del sistema
  - Análisis de conversaciones
  - Entrenamiento futuro del bot
  - Cumplimiento de políticas de datos
"""

# ==============================
# NOTAS DE USO
# ==============================
"""
EJEMPLO DE IMPORTACIÓN:
-----------------------
from config import COLORS, NOMBRE_APP, SIMILARITY_THRESHOLD

# Usar colores en tkinter
label = tk.Label(ventana, text="Hola", bg=COLORS["fondo"], fg=COLORS["texto_bot"])

# Usar umbral de similitud
if porcentaje_similitud >= SIMILARITY_THRESHOLD:
    respuesta = buscar_respuesta(pregunta)

EXTENSIÓN FUTURA:
----------------
Para agregar más configuraciones:
1. Temas claro/oscuro
2. Idiomas (internacionalización)
3. URLs de API
4. Timeouts de conexión
5. Rutas de bases de datos
"""