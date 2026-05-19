"""
================================================================
SISTEMA DE MENÚ PRINCIPAL - PROYECTO chatbotICO
================================================================
Fecha: 18 de mayo de 2026
Escuela: Universidad Nacional Autónoma de México (UNAM) 
         Facultad de Estudios Superiores Aragón
Grupo: 2907
Materia: Inteligencia Artificial
Docente: MARTIN ROMERO UGALDE
Estudiante: Ramírez Alcántara Pedro Antonio
            Victor Flores Felix Omar

DESCRIPCIÓN:
============
Este es el módulo principal del chatbot BotICO, un asistente virtual
especializado en información académica y administrativa para alumnos
de la FES Aragón - Ingeniería en Computación (ICO).

FUNCIONALIDADES PRINCIPALES:
=============================
- Registro de usuarios (nuevo ingreso / regular)
- Interfaz gráfica con burbujas de chat
- Sistema de menús contextuales por tipo de usuario
- Integración con sistemas oficiales UNAM (TramiFES, SIAE, SIEFC)
- Procesamiento de lenguaje natural básico
- Respuestas automatizadas para trámites y dudas frecuentes
- Apertura de enlaces oficiales y documentos PDF
================================================================
*NOTA IMPORTANTE:* 
El proyecto utiliza un sistema de matching por palabras clave 
implementado manualmente (NLP básico) que no requiere librerías 
externas adicionales como thefuzz o python-Levenshtein como 
se había considerado inicialmente.
"""

import tkinter as tk
import webbrowser
from auth import AuthManager
from ui import UI
from menus import MenuSystem
from config import COLORS, NOMBRE_APP
from utils import limpiar_texto


class BotICO:
    """
    Clase principal del chatbot BotICO.
    
    Esta clase orquesta toda la funcionalidad del sistema incluyendo:
    - Gestión de la ventana principal
    - Control de estado del usuario (nombre, tipo)
    - Procesamiento de mensajes y comandos
    - Navegación entre menús y submenús
    - Integración con navegador web para enlaces externos
    - Flujo conversacional con preguntas de continuidad
    
    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación
        nombre_usuario (str): Nombre del usuario registrado
        es_nuevo_ingreso (bool): True si es nuevo alumno, False si es regular
        ui (UI): Objeto de interfaz de usuario para el chat
    """
    
    def __init__(self):
        """
        Inicializa la aplicación BotICO.
        
        Configura la ventana principal con dimensiones, título y colores,
        establece el estado inicial del usuario y lanza el proceso de registro.
        """
        # ========== CONFIGURACIÓN DE VENTANA PRINCIPAL ==========
        self.ventana = tk.Tk()
        self.ventana.title(NOMBRE_APP)                    # Título de la ventana
        self.ventana.geometry("800x650")                  # Tamaño inicial
        self.ventana.configure(bg=COLORS["fondo"])        # Color de fondo institucional
        self.ventana.minsize(700, 550)                    # Tamaño mínimo (evita deformación)
        
        # ========== VARIABLES DE ESTADO ==========
        self.nombre_usuario = ""          # Se llena después del registro
        self.es_nuevo_ingreso = None      # Se llena después del registro
        self.ui = None                    # Referencia a la interfaz de usuario
        
        # ========== CONFIGURACIÓN INICIAL ==========
        self.centrar_ventana()            # Posicionar en centro de pantalla
        self.mostrar_registro()           # Iniciar proceso de autenticación
    
    def centrar_ventana(self):
        """
        Centra la ventana principal en la pantalla del usuario.
        
        Calcula las coordenadas X e Y restando la mitad del tamaño de la ventana
        a la mitad del tamaño de la pantalla, luego aplica la nueva posición.
        """
        self.ventana.update_idletasks()   # Actualizar geometría antes de calcular
        
        # Calcular posición central
        x = (self.ventana.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (650 // 2)
        
        # Aplicar nueva posición (formato "+X+Y" mantiene el tamaño)
        self.ventana.geometry(f"+{x}+{y}")
    
    def mostrar_registro(self):
        """
        Muestra la ventana de registro/autenticación.
        
        Utiliza AuthManager para crear una ventana modal que solicita:
        - Nombre del usuario (mínimo 2 caracteres)
        - Tipo de alumno (Nuevo Ingreso / Regular)
        
        Define un callback interno 'after_registro' que se ejecuta cuando
        el registro es exitoso y construye la interfaz principal.
        """
        def after_registro(nombre, es_nuevo):
            """
            Callback ejecutado tras un registro exitoso.
            
            Args:
                nombre (str): Nombre del usuario registrado
                es_nuevo (bool): True si es nuevo ingreso, False si es regular
            """
            # Guardar datos del usuario
            self.nombre_usuario = nombre
            self.es_nuevo_ingreso = es_nuevo
            
            # Construir interfaz principal del chat
            self.construir_interfaz()
        
        # Crear ventana de registro (modal, bloqueante)
        AuthManager(self.ventana, after_registro).solicitar_registro()
    
    def construir_interfaz(self):
        """
        Instancia la interfaz de usuario y configura el saludo inicial.
        
        El flujo de bienvenida es diferente según el tipo de usuario:
        
        PARA NUEVO INGRESO:
        - Saludo personalizado
        - Información de fechas de inscripción
        - Botón para ver requisitos de convocatoria
        - Botones específicos para trámites de primer ingreso
        
        PARA ALUMNO REGULAR:
        - Saludo personalizado
        - Menú principal completo (trámites, actividades, FAQs, etc.)
        """
        # Crear interfaz de chat (UI)
        self.ui = UI(self.ventana, self.procesar_mensaje, self.es_nuevo_ingreso)
        
        # Establecer nombre de usuario en la interfaz
        self.ui.set_nombre_usuario(self.nombre_usuario)
        
        # ========== FLUJO PARA NUEVO INGRESO ==========
        if self.es_nuevo_ingreso:
            # Mensajes de bienvenida específicos para nuevos alumnos
            self.ui.agregar_mensaje_bot(
                MenuSystem.mensaje_bienvenida_nuevo(self.nombre_usuario)
            )
            self.ui.agregar_mensaje_bot(
                MenuSystem.mensaje_fechas_inscripcion()
            )
            
            # Botón especial para ver requisitos en PDF
            self.ui.agregar_boton_en_chat(
                "📄 Ver Requisitos Convocatoria", 
                self.mostrar_requisitos_pdf
            )
            
            # Botones contextuales para nuevo ingreso
            self.ui.actualizar_botones(MenuSystem.get_botones_nuevo_ingreso())
        
        # ========== FLUJO PARA ALUMNO REGULAR ==========
        else:
            # Saludo para alumnos regulares
            self.ui.agregar_mensaje_bot(
                MenuSystem.mensaje_bienvenida_regular(self.nombre_usuario)
            )
            
            # Menú principal completo
            self.ui.actualizar_botones(MenuSystem.get_botones_principales())
    
    def procesar_mensaje(self, mensaje):
        """
        Procesa el mensaje enviado por el usuario (texto o comando de botón).
        
        Esta función es el núcleo del sistema de respuestas. Maneja:
        1. Comandos de menú (tramites, actividades, etc.)
        2. Submenús anidados (titulación, deportes, etc.)
        3. Acciones específicas (servicio social, inscripciones)
        4. Procesamiento de texto libre con NLP básico
        
        Args:
            mensaje (str): Contenido del mensaje o identificador de comando
        """
        
        # ========== MENÚ PRINCIPAL DE TRÁMITES ==========
        if mensaje == "tramites":
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_submenu_tramites())
            
            # Crear botones dinámicamente para cada opción del submenú
            for texto, cmd in MenuSystem.get_botones_submenu_tramites():
                self.ui.agregar_boton_en_chat(
                    texto, 
                    lambda c=cmd: self.procesar_mensaje(c)  # Capturar valor actual
                )
            return
        
        # ========== SUBMENÚ ESPECÍFICO DE TITULACIÓN ==========
        if mensaje == "submenu_titulacion":
            self.ui.agregar_mensaje_bot("📜 Procesos de Titulación:")
            
            for texto, cmd in MenuSystem.get_botones_titulacion():
                self.ui.agregar_boton_en_chat(
                    texto, 
                    lambda c=cmd: self.procesar_mensaje(c)
                )
            return
        
        # ========== GESTIÓN DE CONSTANCIAS ==========
        if mensaje == "tramite_constancias":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_constancias_texto())
            self.ui.agregar_boton_en_chat("🌐 TramiFES", self.abrir_tramifes)
            self.preguntar_continuidad()  # Preguntar si necesita más ayuda
            return
        
        # ========== SERVICIO SOCIAL ==========
        if mensaje == "servicio_social":
            self.action_servicio_social()
            return
        
        # ========== OPCIONES DE TITULACIÓN ==========
        if mensaje == "tramite_normatividad":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_normatividad_texto())
            self.preguntar_continuidad()
            return
            
        if mensaje == "tramite_registro_titulacion":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_registro_titulacion_texto())
            self.preguntar_continuidad()
            return
            
        if mensaje == "tramite_protesta_diplomados":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_protesta_diplomados_texto())
            self.ui.agregar_boton_en_chat("📝 Forms", self.abrir_forms)
            self.preguntar_continuidad()
            return
            
        if mensaje == "tramite_seguimiento_dgae":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_seguimiento_dgae_texto())
            self.ui.agregar_boton_en_chat("🌐 DGAE", self.abrir_siae)
            return
            
        if mensaje == "tramite_faqs_titulacion":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_faqs_titulacion_texto())
            self.preguntar_continuidad()
            return
        
        # ========== ACTIVIDADES EXTRACURRICULARES ==========
        if mensaje == "actividades":
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_actividades())
            
            for texto, cmd in MenuSystem.get_botones_actividades():
                self.ui.agregar_boton_en_chat(texto, lambda c=cmd: self.procesar_mensaje(c))
            return
        
        # ========== SUBMENÚ DE DEPORTES ==========
        if mensaje == "actividades_deportes":
            self.ui.agregar_mensaje_bot("⚽ Deportes FES Aragón:")
            
            for texto, cmd in MenuSystem.get_botones_deportes():
                self.ui.agregar_boton_en_chat(texto, lambda c=cmd: self.procesar_mensaje(c))
            return
        
        # ========== DICCIONARIO DE INFORMACIÓN DE DEPORTES ==========
        # Mapea comandos de deportes a funciones que devuelven el texto informativo
        deportes = {
            "deporte_futbol_asociacion": MenuSystem.deporte_futbol_asociacion_texto,
            "deporte_futbol_rapido": MenuSystem.deporte_futbol_rapido_texto,
            "deporte_basquetbol": MenuSystem.deporte_basquetbol_texto,
            "deporte_voleibol": MenuSystem.deporte_voleibol_texto,
            "deporte_taekwondo": MenuSystem.deporte_taekwondo_texto,
            "deporte_karate": MenuSystem.deporte_karate_texto,
            "deporte_gimnasio": MenuSystem.deporte_gimnasio_texto,
            "deporte_luchas": MenuSystem.deporte_luchas_texto,
            "deporte_ajedrez": MenuSystem.deporte_ajedrez_texto,
            "deporte_atletismo": MenuSystem.deporte_atletismo_texto,
            "deporte_beisbol": MenuSystem.deporte_beisbol_texto,
            "deporte_rugby": MenuSystem.deporte_rugby_texto,
            "deporte_tenis_mesa": MenuSystem.deporte_tenis_mesa_texto,
            "deporte_gimnasia": MenuSystem.deporte_gimnasia_texto,
            "deporte_todos": MenuSystem.deporte_todos_texto,
            "deporte_costos": MenuSystem.deporte_costos_texto,
            "deporte_contacto": MenuSystem.deporte_contacto_texto,
        }
        
        # Procesar comandos de deportes
        if mensaje in deportes:
            self.ui.agregar_mensaje_bot(deportes[mensaje]())
            
            # Agregar botón SIEFC para consultas de costos y contactos
            if mensaje in ["deporte_costos", "deporte_contacto"]:
                self.ui.agregar_boton_en_chat("💻 SIEFC", self.abrir_siefc)
            
            self.preguntar_continuidad()
            return
        
        # ========== ACTIVIDADES CULTURALES ==========
        if mensaje == "actividades_culturales":
            self.ui.agregar_mensaje_bot(
                "🎨 Talleres culturales: Consulta en Extensión Universitaria."
            )
            self.preguntar_continuidad()
            return
        
        # ========== INTERCAMBIO ACADÉMICO ==========
        if mensaje == "actividades_intercambio":
            self.ui.agregar_mensaje_bot(MenuSystem.faq_intercambio_alumnos_texto())
            self.preguntar_continuidad()
            return
        
        # ========== CENTRO DE IDIOMAS (CLE) ==========
        if mensaje == "actividades_idiomas":
            self.ui.agregar_mensaje_bot(
                "🌐 Centro de Lenguas CLE\n📧 cle.aragon@unam.mx"
            )
            self.ui.agregar_boton_en_chat(
                "🌐 CLE UNAM", 
                lambda: webbrowser.open("https://cle.unam.mx")
            )
            self.preguntar_continuidad()
            return
        
        # ========== INSCRIPCIONES ==========
        if mensaje == "inscripciones_nuevo":
            self.mostrar_inscripcion_nuevo()
            return
            
        if mensaje == "inscripciones":
            self.action_inscripcion_regulares()
            return
        
        # ========== PORTAL DE HORARIOS ==========
        if mensaje == "horarios":
            self.ui.agregar_mensaje_bot("🕒 Portal de Horarios:")
            self.ui.agregar_boton_en_chat(
                "📅 Horarios", 
                lambda: webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/")
            )
            self.ui.agregar_boton_en_chat(
                "📝 Extraordinarios", 
                lambda: webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/extras.php")
            )
            self.ui.agregar_boton_en_chat(
                "📜 Finales", 
                lambda: webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/finales.php")
            )
            return
        
        # ========== CONTACTOS Y DIRECTORIO ==========
        if mensaje == "contactos":
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_contactos())
            return
        
        # ========== PREGUNTAS FRECUENTES (FAQ) ==========
        if mensaje in ["preguntas_nuevo", "preguntas"]:
            self.mostrar_faqs_completo()
            return
        
        # ========== PROCESAMIENTO DE TEXTO LIBRE ==========
        # Agregar mensaje del usuario al chat
        self.ui.agregar_mensaje_usuario(mensaje)
        
        # Normalizar texto (minúsculas, sin acentos, sin espacios extras)
        texto = limpiar_texto(mensaje)
        
        # ========== COMANDOS DE SALIDA ==========
        if texto in ["salir", "adios", "exit", "bye"]:
            self.ui.agregar_mensaje_bot("👋 ¡Hasta pronto! ¡Goya!")
            self.ventana.after(1500, self.ventana.quit)  # Cerrar después de 1.5 seg
            return
        
        # ========== AYUDA GENERAL ==========
        if texto in ["menu", "menú", "ayuda"]:
            self.ui.agregar_mensaje_bot("Usa los botones o escribe tu duda.")
            return
        
        # ========== PALABRAS CLAVE PARA RESPUESTAS DIRECTAS ==========
        # ALTAS Y BAJAS
        if any(p in texto for p in ["altas y bajas", "altas", "bajas", 
                                     "periodo de altas", "ajustar horario", 
                                     "no alcance cupo"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_concepto_altas_bajas_texto())
            self.ui.agregar_boton_en_chat("🌐 TramiFES", self.abrir_tramifes)
            self.preguntar_continuidad()
            return
        
        # DEPORTES (disparar submenú de deportes)
        if any(p in texto for p in ["deportes", "deporte", "gimnasio", "futbol", 
                                     "basquet", "taekwondo", "karate", "voleibol", 
                                     "atletismo", "beisbol", "ajedrez"]):
            self.procesar_mensaje("actividades_deportes")
            return
        
        # SERVICIO SOCIAL
        if any(p in texto for p in ["servicio social", "liberacion servicio", "sass"]):
            self.action_servicio_social()
            return
        
        # CONSTANCIAS Y DOCUMENTOS
        if any(p in texto for p in ["constancia", "tira", "historial", 
                                     "kardex", "boleta"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_constancias_texto())
            self.ui.agregar_boton_en_chat("🌐 TramiFES", self.abrir_tramifes)
            return
        
        # CALENDARIO Y FECHAS
        if any(p in texto for p in ["calendario", "fechas", "asueto", 
                                     "puente", "vacaciones"]):
            self.ui.agregar_mensaje_bot("📅 Calendario oficial FES Aragón:")
            self.ui.agregar_boton_en_chat("📅 Ver Calendario", self.abrir_calendario)
            return
        
        # REINSCRIPCIÓN Y PAGOS
        if any(p in texto for p in ["reinscripcion", "pago", "cuota", 
                                     "scotiabank", "santander", "bbva", "tramifes"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_reinscripcion_texto())
            self.ui.agregar_boton_en_chat("🌐 TramiFES", self.abrir_tramifes)
            return
        
        # CREDENCIAL ESTUDIANTIL
        if any(p in texto for p in ["credencial", "resello", "reposicion"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_credencial_texto())
            return
        
        # EXÁMENES EXTRAORDINARIOS
        if any(p in texto for p in ["extraordinario", "extra", "reprobe", "oposicion"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_horarios_extraordinarios_texto())
            self.ui.agregar_boton_en_chat(
                "🌐 Ver Extras", 
                lambda: webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/extras.php")
            )
            return
        
        # SUSPENSIÓN / BAJA TEMPORAL
        if any(p in texto for p in ["suspension", "baja temporal", "gracia", "congelar"]):
            self.ui.agregar_mensaje_bot(MenuSystem.tram_suspension_texto())
            return
        
        # RECTIFICACIÓN DE CALIFICACIONES
        if any(p in texto for p in ["rectificacion", "aclaracion", "revalidacion"]):
            self.ui.agregar_mensaje_bot(MenuSystem.tram_rectificacion_texto())
            return
        
        # CAMBIO DE CARRERA O SISTEMA
        if any(p in texto for p in ["cambio carrera", "cambio sistema", "suayed"]):
            self.ui.agregar_mensaje_bot(MenuSystem.tram_cambio_carrera_sistema_texto())
            return
        
        # PERMUTAS Y SEGURO MÉDICO
        if any(p in texto for p in ["permuta", "imss", "seguro", "medico"]):
            self.ui.agregar_mensaje_bot(
                MenuSystem.tram_permutas_texto() + "\n\n" + MenuSystem.tram_seguro_texto()
            )
            return
        
        # CALIFICACIONES Y PROMEDIO
        if any(p in texto for p in ["calificacion", "calificaciones", "siae", 
                                     "notas", "promedio"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_calificaciones_texto())
            self.ui.agregar_boton_en_chat("🌐 SIAE", self.abrir_siae)
            return
        
        # INTERCAMBIO (palabras clave adicionales)
        if any(p in texto for p in ["intercambio", "movilidad", "dgeci", "extranjero"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_intercambio_alumnos_texto())
            return
        
        # RECUPERACIÓN DE CONTRASEÑA
        if any(p in texto for p in ["olvide contrasena", "no puedo entrar", 
                                     "bloqueado", "recuperar"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_olvido_contrasena_texto())
            return
        
        # TITULACIÓN (redirigir al menú de trámites)
        if any(p in texto for p in ["titulacion", "titulación", "egreso", 
                                     "normatividad", "seguimiento dgae"]):
            self.procesar_mensaje("tramites")
            return
        
        # ========== RESPUESTA POR DEFECTO ==========
        # Si ninguna palabra clave coincide, mostrar mensaje genérico
        self.ui.agregar_mensaje_bot(MenuSystem.mensaje_no_entendido())
    
    def mostrar_faqs_completo(self):
        """
        Muestra un índice completo de preguntas frecuentes con botones interactivos.
        
        Cada botón del índice despliega la información correspondiente cuando
        es presionado, permitiendo al usuario explorar las FAQs de manera
        organizada por categorías numeradas del 1 al 15.
        """
        self.ui.agregar_mensaje_bot("❓ ÍNDICE COMPLETO DE PREGUNTAS FRECUENTES ❓")
        
        # ========== CREAR BOTONES PARA CADA SECCIÓN ==========
        # Cada botón usa lambda para capturar el texto específico de la FAQ
        
        # 1. Contraseña
        self.ui.agregar_boton_en_chat(
            "🔑 1. Olvidé mi Contraseña", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_olvido_contrasena_texto())
        )
        
        # 2. Reinscripción
        self.ui.agregar_boton_en_chat(
            "🔄 2. Reinscripción y Pagos", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_reinscripcion_texto())
        )
        
        # 3. Constancias
        self.ui.agregar_boton_en_chat(
            "📄 3. Constancias e Historial", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_constancias_texto())
        )
        
        # 4. Credencial
        self.ui.agregar_boton_en_chat(
            "🪪 4. Credencial y Resellos", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_credencial_texto())
        )
        
        # 5. Extraordinarios
        self.ui.agregar_boton_en_chat(
            "📝 5. Exámenes Extraordinarios", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_horarios_extraordinarios_texto())
        )
        
        # 6. Suspensión
        self.ui.agregar_boton_en_chat(
            "🛑 6. Suspensión de Estudios", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.tram_suspension_texto())
        )
        
        # 7. Rectificación
        self.ui.agregar_boton_en_chat(
            "🔄 7. Rectificación de Notas", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.tram_rectificacion_texto())
        )
        
        # 8. Cambio de carrera
        self.ui.agregar_boton_en_chat(
            "🔀 8. Cambio de Carrera/Sistema", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.tram_cambio_carrera_sistema_texto())
        )
        
        # 9. Egresados
        self.ui.agregar_boton_en_chat(
            "🎓 9. Egresados y Certificados", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_egresados_texto())
        )
        
        # 10. Permutas y Seguro
        self.ui.agregar_boton_en_chat(
            "🤝 10. Permutas y Seguro IMSS", 
            lambda: self.ui.agregar_mensaje_bot(
                MenuSystem.tram_permutas_texto() + "\n\n" + MenuSystem.tram_seguro_texto()
            )
        )
        
        # 11. Deportes
        self.ui.agregar_boton_en_chat(
            "⚽ 11. Actividades Deportivas", 
            lambda: self.procesar_mensaje("actividades_deportes")
        )
        
        # 12. Intercambio
        self.ui.agregar_boton_en_chat(
            "✈️ 12. Intercambio Académico", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_intercambio_alumnos_texto())
        )
        
        # 13. Calificaciones
        self.ui.agregar_boton_en_chat(
            "📊 13. Consulta de Calificaciones", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_calificaciones_texto())
        )
        
        # 14. Horarios
        self.ui.agregar_boton_en_chat(
            "🕒 14. Portal de Horarios", 
            lambda: self.ui.agregar_mensaje_bot("🕒 Usa el botón de Horarios en el menú principal")
        )
        
        # 15. Altas y Bajas
        self.ui.agregar_boton_en_chat(
            "🔄 15. Altas y Bajas", 
            lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_concepto_altas_bajas_texto())
        )
    
    # ========== MÉTODOS DE ACCIÓN ESPECÍFICOS ==========
    
    def action_servicio_social(self):
        """
        Muestra información completa sobre Servicio Social.
        
        Incluye:
        - Porcentaje de avance requerido
        - Duración y horarios
        - Proceso de liberación
        - Enlaces directos al sistema SASS y correo de contacto
        """
        self.ui.agregar_mensaje_bot(MenuSystem.tramite_servicio_social_texto())
        self.ui.agregar_boton_en_chat(
            "💻 Sistema SASS", 
            lambda: webbrowser.open("https://cedco2.aragon.unam.mx/servsocial/")
        )
        self.ui.agregar_boton_en_chat(
            "📧 Correo SS", 
            lambda: webbrowser.open("mailto:serviciosocial@aragon.unam.mx")
        )
        self.preguntar_continuidad()
    
    def action_inscripcion_regulares(self):
        """
        Informa sobre el proceso de reinscripción para alumnos regulares.
        
        Muestra fechas clave y enlaces a TramiFES y calendario académico.
        """
        self.ui.agregar_mensaje_bot(MenuSystem.faq_inscripcion_regulares_texto())
        self.ui.agregar_boton_en_chat("🌐 TramiFES", self.abrir_tramifes)
        self.ui.agregar_boton_en_chat("📅 Calendario", self.abrir_calendario)
    
    def mostrar_inscripcion_nuevo(self):
        """
        Despliega el flujo informativo para inscripción de primer ingreso.
        
        Incluye:
        - Enlace al sistema PIIANITE
        - Carta compromiso en PDF
        - Instrucciones específicas para nuevos alumnos
        """
        self.ui.agregar_mensaje_bot(MenuSystem.mensaje_inscripciones())
        self.ui.agregar_boton_en_chat(
            "🌐 PIIANITE", 
            lambda: webbrowser.open("http://132.248.44.93:8080/PIIANI/")
        )
        self.ui.agregar_boton_en_chat(
            "📄 Carta Compromiso", 
            lambda: webbrowser.open("http://132.248.44.93:8080/PIIANI/doc/CARTA_COMPROMISO_GEN_2026-2.pdf")
        )
    
    def mostrar_requisitos_pdf(self):
        """
        Muestra opciones para consultar requisitos de ingreso.
        
        Ofrece dos modalidades:
        - Pase Reglamentado (alumnos de bachillerato UNAM)
        - Concurso de Selección (externos)
        """
        self.ui.agregar_mensaje_bot("Selecciona tu ingreso:")
        self.ui.agregar_boton_en_chat(
            "📜 Pase Reglamentado", 
            lambda: webbrowser.open("https://www.dgae.unam.mx/Pase2026/index.html")
        )
        self.ui.agregar_boton_en_chat(
            "📝 Concurso", 
            lambda: webbrowser.open("https://www.dgae-siae.unam.mx")
        )
    
    # ========== NAVEGACIÓN WEB ==========
    
    def abrir_tramifes(self):
        """Abre el portal TramiFES de la FES Aragón para trámites escolares."""
        webbrowser.open("https://tramifes.aragon.unam.mx/")
        self.preguntar_continuidad()
    
    def abrir_siefc(self):
        """Abre el sistema SIEFC para actividades físico-deportivas y culturales."""
        webbrowser.open("https://lovelace.aragon.unam.mx/siefc/")
        self.preguntar_continuidad()
    
    def abrir_siae(self):
        """Abre el sistema SIAE de la DGAE para consulta de calificaciones."""
        webbrowser.open("https://www.dgae-siae.unam.mx")
        self.preguntar_continuidad()
    
    def abrir_forms(self):
        """Abre formulario de Microsoft Forms para protesta de diplomados."""
        webbrowser.open("https://forms.office.com/pages/responsepage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAN__mF8m8FUQzZJTjdUTVdMUFA5VDQyVTZLWVRDVTRCNS4u")
    
    def abrir_calendario(self):
        """Abre el calendario académico oficial en PDF."""
        webbrowser.open("https://aragon.unam.mx/fes-aragon/public_html/documents/nuestra_facultad/calendario-2026-ll.pdf")
        self.preguntar_continuidad()
    
    # ========== FLUJO DE CIERRE Y REPETICIÓN ==========
    
    def preguntar_continuidad(self):
        """
        Pregunta al usuario si desea realizar otra consulta.
        
        Agrega botones "Sí" y "No, salir" para mantener la conversación
        activa o permitir la salida controlada del sistema.
        """
        self.ui.agregar_mensaje_bot("¿Te puedo ayudar en algo más?")
        self.ui.agregar_boton_en_chat("👍 Sí", self.continuar)
        self.ui.agregar_boton_en_chat("🛑 No, salir", self.salir)
    
    def continuar(self):
        """
        Restaura el menú principal según el perfil del usuario.
        
        Permite al usuario continuar con nuevas consultas después de
        haber completado una interacción específica.
        """
        if self.es_nuevo_ingreso:
            self.ui.actualizar_botones(MenuSystem.get_botones_nuevo_ingreso())
        else:
            self.ui.actualizar_botones(MenuSystem.get_botones_principales())
    
    def salir(self):
        """
        Despide al usuario y cierra la aplicación.
        
        Muestra un mensaje de despedida personalizado y cierra la ventana
        después de 1.5 segundos para dar tiempo a leer el mensaje.
        """
        self.ui.agregar_mensaje_bot("👋 ¡Gracias por usar BotICO! ¡Goya!")
        self.ventana.after(1500, self.ventana.quit)  # Cierre diferido
    
    def run(self):
        """
        Inicia el bucle principal de la interfaz gráfica.
        
        Este método debe ser llamado después de inicializar la aplicación
        para comenzar a procesar eventos de la ventana.
        """
        self.ventana.mainloop()


# ========== PUNTO DE ENTRADA PRINCIPAL ==========
if __name__ == "__main__":
    """
    Punto de entrada del script.
    
    Crea una instancia de la aplicación BotICO y ejecuta su bucle principal.
    Esto solo se ejecuta cuando el script se corre directamente (no al importarlo).
    """
    app = BotICO()   # Crear instancia de la aplicación
    app.run()        # Iniciar la interfaz gráfica