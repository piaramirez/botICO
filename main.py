# main.py - Punto de entrada principal del chatbot escolar
"""
Módulo Core Principal - Chatbot Escolar Inteligente para ICO (BotICO).

Este módulo inicializa el ciclo de vida de la aplicación utilizando la librería 
Tkinter. Implementa una máquina de soporte semántico basada en tokens textuales
para resolver intenciones estudiantiles distribuidas por perfiles (Nuevo Ingreso / Regulares).

Arquitectura del Sistema:
    - Inicialización de Ventana y Geometría síncrona.
    - Control de autenticación y Registro de estados vía AuthManager.
    - Motor Parser de Categorías por evaluación de texto libre libre de walls.
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
    Controlador Principal de la aplicación BotICO.
    
    Gestiona el flujo lógico entre el sistema de autenticación inicial,
    la construcción dinámica de widgets gráficos de la UI y la interceptación
    semántica de las consultas del alumno.
    """
    def __init__(self):
        """Inicializa la raíz de Tkinter, variables de sesión y centra la UI."""
        self.ventana = tk.Tk()
        self.ventana.title(NOMBRE_APP)
        self.ventana.geometry("800x650")
        self.ventana.configure(bg=COLORS["fondo"])
        self.ventana.minsize(700, 550)
        
        self.nombre_usuario = ""
        self.es_nuevo_ingreso = None
        self.ui = None
        
        self.centrar_ventana()
        self.mostrar_registro()
    
    def centrar_ventana(self):
        """Calcula el offset síncrono de la pantalla para centrar la ventana principal."""
        self.ventana.update_idletasks()
        x = (self.ventana.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (650 // 2)
        self.ventana.geometry(f"+{x}+{y}")
    
    def mostrar_registro(self):
        """Instancia la pasarela de autenticación interceptando los datos del alumno."""
        def after_registro(nombre, es_nuevo):
            self.nombre_usuario = nombre
            self.es_nuevo_ingreso = es_nuevo
            self.construir_interfaz()
        
        AuthManager(self.ventana, after_registro).solicitar_registro()
    
    def construir_interfaz(self):
        """Construye los frames de la UI y despliega los banners de bienvenida condicionales."""
        self.ui = UI(self.ventana, self.procesar_mensaje, self.es_nuevo_ingreso)
        self.ui.set_nombre_usuario(self.nombre_usuario)
        
        if self.es_nuevo_ingreso:
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_bienvenida_nuevo(self.nombre_usuario))
            
            texto_inicial = (
                "╔══════════════════════════════════════════════════════════════════╗\n"
                "║                    📅 FECHAS DE INSCRIPCIÓN - ICO                ║\n"
                "╠══════════════════════════════════════════════════════════════════╣\n"
                "║  🗓️ SEMESTRE 2026-2:                                             ║\n"
                "║     • Registro en línea: 20 - 25 de enero                        ║\n"
                "║     • Inicio de clases: 3 de febrero 2026                        ║\n"
                "║     • Altas y bajas: 4, 5 y 6 de febrero 2026                    ║\n"
                "╚══════════════════════════════════════════════════════════════════╝"
            )
            self.ui.agregar_mensaje_bot(texto_inicial)
            
            self.ui.agregar_mensaje_bot("BotICO: Como eres de Nuevo Ingreso, aquí tienes el acceso a tu proceso:")
            self.ui.agregar_boton_en_chat(
                texto_boton="📄 Ver Requisitos de Convocatoria 2026-1",
                comando=self.mostrar_requisitos_pdf
            )
            
            self.ui.agregar_mensaje_bot("📌 Elige una opción o escribe tu duda:")
            self.ui.actualizar_botones(MenuSystem.get_botones_nuevo_ingreso())
        else:
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_bienvenida_regular(self.nombre_usuario))
            self.ui.actualizar_botones(MenuSystem.get_botones_principales())
    
    def process_mensaje_directo(self, categoria, mensaje):
        """Inyecta la respuesta cruda de categorías estáticas en la caja de diálogo."""
        respuesta = self.obtener_respuesta_por_categoria(categoria, mensaje)
        self.ui.agregar_mensaje_bot(respuesta)

    def procesar_mensaje(self, mensaje):
        """
        Motor Parser principal de mensajes. Evalúa y distribuye intenciones semánticas.
        
        Args:
            mensaje (str): Cadena de texto libre ingresada por el usuario o comando de botón.
        """
        # ==========================================================================
        # 1. INTERCEPTACIÓN DE CALLBACKS DEL SUBMENÚ INTERACTIVO DE TRÁMITES
        # ==========================================================================
        if mensaje == "tramite_normatividad":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_normatividad_texto())
            self.ventana.after(1000, self.preguntar_continuidad)
            return
        elif mensaje == "tramite_registro_titulacion":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_registro_titulacion_texto())
            self.ventana.after(1000, self.preguntar_continuidad)
            return
        elif mensaje == "tramite_protesta_diplomados":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_protesta_diplomados_texto())
            self.ui.agregar_boton_en_chat(texto_boton="📝 Llenar Microsoft Forms", comando=self.abrir_forms_titulacion)
            self.ventana.after(1000, self.preguntar_continuidad)
            return
        elif mensaje == "tramite_seguimiento_dgae":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_seguimiento_dgae_texto())
            self.ui.agregar_boton_en_chat(texto_boton="🌐 Portal Oficial DGAE SIAE", comando=self.abrir_siae_web)
            return
        elif mensaje == "tramite_faqs_titulacion":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_faqs_titulacion_texto())
            self.ventana.after(1000, self.preguntar_continuidad)
            return

        # Registra el mensaje que el usuario acaba de escribir o presionar en la UI
        self.ui.agregar_mensaje_usuario(mensaje)
        
        # Limpieza estándar del string para evaluaciones consistentes
        texto_limpio = limpiar_texto(mensaje)
        
        # Comprobación global de comandos de salida de la sesión
        if texto_limpio in ["salir", "adios", "exit", "chao", "bye", "cerrar"]:
            self.ui.agregar_mensaje_bot("👋 ¡Gracias por usar BotICO! Hasta pronto. ¡Goya!")
            self.ventana.after(1500, self.ventana.quit)
            return
        
        # Comprobación global para re-desplegar opciones de ayuda o menús principales
        if texto_limpio in ["menu", "menú", "ayuda", "opciones", "help", "inicio"]:
            if self.es_nuevo_ingreso:
                self.ui.agregar_mensaje_bot("📋 Opciones: Convocatoria, Horarios, Contactos, Preguntas Frecuentes, Calendario")
            else:
                self.ui.agregar_mensaje_bot("📋 Opciones: Inscripciones, Horarios, Trámites, Contactos, Actividades, Calendario")
            return
        
        # ==========================================================================
        # 2. CANDADO DE CONTROL DE TRÁMITES Y INTENCIONES DE EGRESO (TEXTO LIBRE)
        # ==========================================================================
        if texto_limpio in ["tramites", "trámites", "tramite", "trámite", "titulacion", "titulación", "egreso", "egresados", "normatividad", "seguimiento", "fotos", "diplomados", "carpeta fisica"]:
            self.action_tramites_menu()
            return

        # Pasa el mensaje al evaluador NLP para clasificar la intención por palabras clave
        categoria = self.evaluar_categoria(mensaje)
        
        # ========== INTERCEPTACIÓN GLOBAL: CALENDARIO ESCOLAR ==========
        if categoria == "calendario" or any(p in texto_limpio for p in ["calendario oficial", "agenda unam", "fechas de asueto", "cuando salimos de vacaciones", "puentes"]):
            self.ui.agregar_mensaje_bot("BotICO: Aquí tienes el acceso directo al calendario oficial de la FES Aragón:")
            self.ui.agregar_boton_en_chat(texto_boton="📅 Ver Calendario Oficial 2026-II", comando=self.abrir_calendario)
            return

        # ========== MULTI-INTERCEPTACIÓN POR TEXTO LIBRE GENERAL ==========
        
        # Intención Especial: Pérdida u Olvido de Contraseña, Accesos Bloqueados en Sistemas
        if any(p in texto_limpio for p in ["olvide mi contrasena", "olvide mi clave", "no puedo entrar", "bloqueado", "recuperar contrasena", "no me deja entrar", "perdi mi contrasena", "no me acuerdo de mi clave", "restablecer contrasena", "cuenta bloqueada", "no entra al siae", "falla trami", "clave temporal", "no recuerdo el pass", "password", "contrasenia"]):
            self.action_faq_olvido_contrasena()
            return

        # 1. Intención: Reinscripción, Fechas, Cuotas, Pagos, Dónde/Cómo/Cuándo Inscribirse
        if any(p in texto_limpio for p in ["donde me inscribo", "como me inscribo", "cuando me inscribo", "inscripcion nuevo ingreso", "pago cuota", "ordinario", "reinscripcion", "reinscribirme", "scotiabank", "santander", "bbva", "ficha de deposito", "adeudo biblioteca", "fundacion unam", "cuanto cuesta la inscripcion", "banco convenio", "donde pagar", "pagos", "cuota", "cajas", "costo", "referencia bancaria", "donde pago", "pagar inscripción", "hacer el pago", "50 centavos", "cien pesos", "minimo 100", "piiani", "piianite"]):
            if self.es_nuevo_ingreso:
                self.mostrar_inscripcion_nuevo_ingreso()
            else:
                self.action_inscripcion_regulares()
            return
            
        # 2. Intención: Explicación del concepto de Altas y Bajas
        if any(p in texto_limpio for p in ["que son altas y bajas", "para que sirven las altas", "ajustar horario", "no alcance cupo", "dar de alta", "dar de baja", "concepto de altas", "altas y bajas trami"]):
            self.action_faq_concepto_altas_bajas()
            return

        # 3. Intención: Modificación de carga, Sorteo y Plataforma de Horarios en Cómputo
        if any(p in texto_limpio for p in ["altas y bajas", "sorteo", "cambiar materia", "trami", "tramifes", "mi cita", "que dia me toca", "mover materia", "permutar grupo", "meter materia", "dar de baja una clase", "cupo en grupos"]):
            self.action_faq_horarios_menu()
            return
            
        # 4. Intención: Constancias Escolares, Tiras de Materias e Historial
        if any(p in texto_limpio for p in ["constancia", "estudios", "creditos", "historial", "tira", "boleta", "kardex", "materias aprobadas", "porcentaje", "promedio general", "sellada", "firmada", "comprobante de estudios", "pedir constancia", "avance academico"]):
            self.action_faq_constancias()
            return
            
        # 5. Intención: Identificación Física y Resellos
        if any(p in texto_limpio for p in ["credencial", "resello", "reposicion", "crede", "perdi mi credencial", "tarjeta unam", "plastico", "sello anual", "credencial escolar", "renovar credencial"]):
            self.action_faq_credencial()
            return
            
        # 6. Intención: Exámenes Extraordinarios
        if any(p in texto_limpio for p in ["extraordinario", "extra", "extras", "reprobe", "pasar materia", "oposicion", "pagar extra", "cuando son los extras", "inscribir extraordinario", "sinodales de extras"]):
            self.action_horarios_extras()
            return
            
        # 7. Intención: Pausas Académicas y Suspensión de Estudios
        if any(p in texto_limpio for p in ["suspension", "baja temporal", "gracia", "dejar de estudiar", "pausar", "periodo de gracia", "congelar un año", "congelar semestre", "darme de baja temporal"]):
            self.action_tram_suspension()
            return
            
        # 8. Intención: Corrección de Actas o Revalidación Externa
        if any(p in texto_limpio for p in ["rectificacion", "aclaracion calificacion", "cambio calificacion", "revalidacion", "movilidad", "f306", "revalidar materias", "clase espejo", "coil virtual", "el profe se equivoco"]):
            self.action_tram_rectificacion()
            return
            
        # 9. Intención: Cambios Internos de Carrera o Sistema SUAyED
        if any(p in texto_limpio for p in ["cambio interno", "cambio de carrera", "cambio de sistema", "cambio modalidad", "8.5", "suayed", "siae", "dgae", "modalidad abierta", "modalidad distancia", "requisitos para cambio de carrera"]):
            self.action_tram_cambio_carrera_sistema()
            return
            
        # 10. Intención: Años Posteriores e Incorporadas
        if any(p in texto_limpio for p in ["años posteriores", "acreditacion", "incorporado", "revalidación", "vengo de incorporada", "externa", "licenciatura externa", "sistema incorporado", "continuar estudios unam"]):
            self.action_tram_anos_posteriores()
            return
            
        # 12. Intención: Permutas Internas o Interplanteles
        if any(p in texto_limpio for p in ["permuta", "permutas", "cambio de plantel", "cambio de fes", "cambiarme de facultad", "permuta de alumno"]):
            self.action_tram_permutas_imss_menu()
            return
            
        # 13. Intención: Seguro Facultativo Médico (IMSS)
        if any(p in texto_limpio for p in ["imss", "seguro", "facultativo", "medico", "médico", "clinica", "alta imss", "seguridad social", "nss", "cartilla del seguro", "vigencia de derechos imss"]):
            self.action_tram_permutas_imss_menu()
            return
            
        # 14. Intención: Renuncia de Carrera o Bajas Definitivas
        if any(p in texto_limpio for p in ["baja materia", "baja materias", "baja asignatura", "bajas asignaturas", "baja semestre", "baja definitiva", "baja total", "renunciar carrera", "extemporanea", "irme de la unam"]):
            self.action_tram_bajas_menu()
            return
            
        # 15. Intención: Deportes, Instalaciones, Escuela del Deporte, Gimnasio, CLE y Cultura (Espectro Unificado)
        if any(p in texto_limpio for p in ["deporte", "deportes", "futbol", "basquet", "gimnasio", "pesas", "siefc", "instalaciones", "carlos octavio", "ajedrez", "karate", "taekwondo", "ludoteca", "diverpuma", "95 pesos", "390", "115", "donde entreno", "canchas", "pista de atletismo", "cuentas con actividades culturales", "que actividades tiene la fes", "que actividades hay", "talleres culturales", "actividades de extension", "aprender idiomas"]):
            if self.es_nuevo_ingreso:
                self.process_mensaje_directo("actividades", mensaje)
            else:
                self.action_faq_deportes_menu()
            return
            
        # 16. Intención: Intercambios Internacionales o Convocatorias DGECI
        if any(p in texto_limpio for p in ["intercambio", "movilidad", "dgeci", "crai", "coil", "clase espejo", "pittaae", "toefl", "ielts", "extranjero", "beca internacional", "44%", "irme a otro pais", "estudiar fuera de mexico", "erasmus"]):
            self.action_faq_intercambio_menu()
            return
            
        # 17. Intención: Consulta Escolar de Calificaciones / Actas
        if any(p in texto_limpio for p in ["calificacion", "calificaciones", "sabes calificacion", "ver notas", "ver calificacion", "subieron actas", "promedio", "siae notas", "donde veo mis califis", "portal de calificaciones"]):
            self.action_faq_calificaciones()
            return
            
        # 18. Intención: Consulta Completa de Horarios, Finales, Salones o Profesores
        if any(p in texto_limpio for p in ["horario", "horarios", "como checo mi horario", "finales", "extraordinarios", "combo grupo", "salon", "docente", "sinodales", "materia", "filtrar por materia", "donde ver mi horario", "que salon me toca", "quien es mi profesor"]):
            self.action_faq_horarios_menu()
            return

        # ==========================================================================
        # 3. FILTRADO CONTEXTUAL CONDICIONADO POR PERFILES DE USUARIO
        # ==========================================================================
        if self.es_nuevo_ingreso:
            if mensaje == "inscripciones_nuevo" or categoria == "inscripciones":
                self.mostrar_inscripcion_nuevo_ingreso()
            elif mensaje == "preguntas_nuevo" or categoria == "preguntas":
                self.mostrar_menu_preguntas_frecuentes_acciones()
            elif mensaje == "tramites" or categoria == "tramites":
                self.action_tramites_menu()
            elif mensaje == "horarios" or categoria == "horarios":
                self.action_faq_horarios_menu()
            elif mensaje == "contactos" or categoria == "contactos":
                self.process_mensaje_directo("contactos", mensaje)
            elif categoria == "convocatoria" or any(p in texto_limpio for p in ["cuando sale la convocatoria", "requisitos de ingreso", "examen de admision unam"]):
                self.ui.agregar_mensaje_bot("BotICO: Con base en tu estatus de Nuevo Ingreso, preparé este acceso rápido para los detalles oficiales de la Convocatoria:")
                self.ui.agregar_boton_en_chat(texto_boton="📄 Ver Requisitos de Convocatoria 2026-1", comando=self.mostrar_requisitos_pdf)
            else:
                self.process_mensaje_directo(categoria, mensaje)
        else:
            # FLUJO ASIGNADO A ALUMNO REGULAR
            if mensaje == "inscripciones" or categoria == "inscripciones":
                self.action_inscripcion_regulares()
            elif mensaje == "preguntas" or categoria == "preguntas":
                self.mostrar_menu_preguntas_frecuentes_acciones()
            elif mensaje == "tramites" or categoria == "tramites":
                self.action_tramites_menu()
            elif mensaje == "horarios" or categoria == "horarios":
                self.action_faq_horarios_menu()
            elif mensaje == "contactos" or categoria == "contactos":
                self.process_mensaje_directo("contactos", mensaje)
            else:
                self.process_mensaje_directo(categoria, mensaje)

    def evaluar_categoria(self, comando):
        """Diccionario semántico con mapeo avanzado de intenciones estudiantiles"""
        text_clean = limpiar_texto(comando)
        comandos_directos = ["inscripciones_nuevo", "co4nvocatoria", "preguntas_nuevo", "preguntas", 
                             "horarios", "contactos", "contacto", "inscripciones", "tramites", "actividades", "calendario"]
        
        if comando in comandos_directos:
            if comando in ["inscripciones_nuevo", "co4nvocatoria"]: return "convocatoria"
            if comando in ["preguntas_nuevo", "preguntas"]: return "preguntas"
            if comando in ["contacto"]: return "contactos"
            return comando
            
        palabras_clave = {
            "convocatoria": ["convocatoria", "ingreso", "admision", "examen", "pase reglamentado", "primer ingreso", "nuevo ingreso"],
            "horarios": ["horario", "horarios", "materias", "clases", "profesores", "grupo", "turno", "finales", "extraordinarios", "salon", "docente"],
            "contactos": ["telefono", "correo", "direccion", "contacto", "redes", "facebook", "ubicacion", "oficina", "ventanilla", "edificio", "extension", "responsable", "ext", "carlos octavio", "valencia"],
            "inscripciones": ["inscripcion", "inscripciones", "pago", "banco", "costo", "cuota", "referencia", "cajas", "ficha", "contraseña", "clave", "bloqueado"],
            "tramites": ["constancia", "certificado", "titulacion", "servicio social", "bajas", "altas", "baja", "alta", "permuta", "sorteo", "cita", "extra", "suspension", "rectificacion", "revalidacion", "turno", "simultanea", "imss", "seguro", "egresado", "acreditacion", "pasante", "Titulacion", "servicio"],
            "actividades": ["taller", "deporte", "cultural", "musica", "idiomas", "cle", "ingles", "futbol", "basquet", "talleres", "teatro", "gimnasio", "pesas", "siefc", "ludoteca", "diverpuma", "intercambio", "movilidad", "dgeci", "coil"]
        }
        for cat, palabras in palabras_clave.items():
            for p in palabras:
                if p in text_clean: return cat
        return "desconocido"

    def obtener_respuesta_por_categoria(self, categoria, mensaje_original):
        respuestas = {
            "convocatoria": MenuSystem.mensaje_convocatoria,
            "contactos": MenuSystem.mensaje_contactos,
            "inscripciones": MenuSystem.mensaje_inscripciones,
            "actividades": MenuSystem.mensaje_actividades,
        }
        if categoria in respuestas: return respuestas[categoria]()
        return MenuSystem.mensaje_no_entendido()

    # ========== MÓDULO UNIFICADO DE PREGUNTAS FRECUENTES (SÚPER ÍNDICE) ==========
    def mostrar_menu_preguntas_frecuentes_acciones(self):
        """Muestra el índice unificado completo de Preguntas Frecuentes y Trámites"""
        self.ui.agregar_mensaje_bot("❓ Índice Completo de Preguntas Frecuentes y Trámites de Servicios Escolares:")
        
        self.ui.agregar_boton_en_chat(texto_boton="🔑 1. Olvidé mi Contraseña / Accesos", comando=self.action_faq_olvido_contrasena)
        self.ui.agregar_boton_en_chat(texto_boton="🔄 2. Reinscripción, Sorteos y Pagos", comando=self.action_faq_reinscripcion)
        self.ui.agregar_boton_en_chat(texto_boton="📄 3. Tramitar Constancias e Historial", comando=self.action_faq_constancias)
        self.ui.agregar_boton_en_chat(texto_boton="🪪 4. Nueva Credencial y Resellos", comando=self.action_faq_credencial)
        self.ui.agregar_boton_en_chat(texto_boton="📝 5. Exámenes Extraordinarios (Extras)", comando=self.action_horarios_extras)
        self.ui.agregar_boton_en_chat(texto_boton="🛑 6. Suspensión Temporal de Estudios", comando=self.action_tram_suspension)
        self.ui.agregar_boton_en_chat(texto_boton="🔄 7. Rectificación / Revalidación de Notas", comando=self.action_tram_rectificacion)
        self.ui.agregar_boton_en_chat(texto_boton="🔀 8. Cambios de Carrera / De Sistema (SUAyED)", comando=self.action_tram_cambio_carrera_sistema)
        self.ui.agregar_boton_en_chat(texto_boton="🎓 9. Ingreso a Años Posteriores / Egresados", comando=self.action_faq_egresados_menu)
        self.ui.agregar_boton_en_chat(texto_boton="🤝 10. Permutas e Inscripción al IMSS", comando=self.action_tram_permutas_imss_menu)
        self.ui.agregar_boton_en_chat(texto_boton="📉 11. Bajas de Materias o del Semestre", comando=self.action_tram_bajas_menu)
        self.ui.agregar_boton_en_chat(texto_boton="⚽ 12. Actividades Deportivas y Recreativas", comando=self.action_faq_deportes_menu)
        self.ui.agregar_boton_en_chat(texto_boton="✈️ 13. Intercambio Académico y Movilidad UNAM", comando=self.action_faq_intercambio_menu)
        self.ui.agregar_boton_en_chat(texto_boton="📊 14. Consulta de Calificaciones e Historial (SIAE)", comando=self.action_faq_calificaciones)
        self.ui.agregar_boton_en_chat(texto_boton="🕒 15. Portal de Horarios, Finales y Extraordinarios", comando=self.action_faq_horarios_menu)
        self.ui.agregar_boton_en_chat(texto_boton="🔄 16. ¿Qué es el periodo de Altas y Bajas?", comando=self.action_faq_concepto_altas_bajas)

    # ========== CONTROLADORES DE ACCIONES INDIVIDUALES ==========
    def action_faq_olvido_contrasena(self):
        """Despliega los requisitos de reajuste presencial de contraseñas bloqueadas."""
        self.ui.agregar_mensaje_bot(MenuSystem.faq_olvido_contrasena_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Ver Ubicación de Servicios Escolares", comando=self.abrir_pagina_escolares_fes)

    def action_inscripcion_regulares(self):
        """Despliega el panel híbrido para reinscripción en línea / física de alumnos."""
        self.ui.agregar_mensaje_bot(MenuSystem.faq_inscripcion_regulares_texto())
        self.ui.agregar_boton_en_chat(texto_boton="📅 Ver Calendario Oficial 2026-II", comando=self.abrir_calendario)
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Entrar al Portal TramiFES", comando=self.abrir_link_tramifes_final)

    def action_faq_reinscripcion(self):
        """Enlaza el flujo hacia el concepto de altas y bajas."""
        self.ui.agregar_mensaje_bot(MenuSystem.faq_reinscripcion_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Entrar al Sistema TramiFES", comando=self.abrir_link_tramifes_final)
        self.ui.agregar_boton_en_chat(texto_boton="📋 Ver Guía de Sorteo Altas/Bajas", comando=self.action_faq_concepto_altas_bajas)

    def action_faq_constancias(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_constancias_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Ir al Portal Escolar CISE FES", comando=self.abrir_pagina_escolares_fes)

    def action_faq_credencial(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_credencial_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Acceder a Servicios Escolares Web", comando=self.abrir_pagina_escolares_fes)

    def action_tram_suspension(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_suspension_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Consultar en el Portal del CISE", comando=self.abrir_pagina_escolares_fes)

    def action_tram_rectificacion(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_rectificacion_texto())
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_tram_cambio_carrera_sistema(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_cambio_carrera_sistema_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Portal Oficial DGAE SIAE", comando=self.abrir_siae_web)

    def abrir_siae_web(self):
        webbrowser.open("https://www.dgae-siae.unam.mx")
        self.ventana.after(1000, self.preguntar_continuidad)

    # ========== MODIFICADO: CONTROLADORES INTERACTIVOS DE TRÁMITES Y TITULACIÓN ==========
    def action_tramites_menu(self):
        """Despliega el menú con botones interactivos para la sección de Trámites y Titulación."""
        self.ui.agregar_mensaje_bot(MenuSystem.mensaje_tramites())
        botones = MenuSystem.get_botones_tramites()
        for texto_btn, comando_id in botones:
            self.ui.agregar_boton_en_chat(texto_boton=texto_btn, comando=lambda cid=comando_id: self.procesar_mensaje(cid))

    def action_tramite_registro_titulacion(self):
        """Muestra los requisitos de registro de modalida de titulación."""
        self.ui.agregar_mensaje_bot(MenuSystem.tramite_registro_titulacion_texto())
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_tramite_protesta_diplomados(self):
        """Muestra los requisitos detallados de toma de protesta, fotos y liga del formulario."""
        self.ui.agregar_mensaje_bot(MenuSystem.tramite_protesta_diplomados_texto())
        # Inserción de botón dinámico para el enlace directo de Microsoft Forms
        self.ui.agregar_boton_en_chat(
            texto_boton="📝 Llenar Formulario de Registro (Microsoft Forms)", 
            comando=self.abrir_forms_titulacion
        )
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_forms_titulacion(self):
        """Abre de forma segura el enlace de Microsoft Forms proporcionado."""
        webbrowser.open("https://forms.office.com/pages/responsepage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAN__mF8m8FUQzZJTjdUTVdMUFA5VDQyVTZLWVRDVTRCNS4u")

    def action_tramite_web_titulacion(self):
        """Abre el sitio oficial de titulación de la FES Aragón."""
        self.ui.agregar_mensaje_bot(MenuSystem.tramite_web_titulacion_texto())
        webbrowser.open("https://aragon.unam.mx/comunidad-egresada/content/titulacion/")
        self.ventana.after(1000, self.preguntar_continuidad)

    # ========== ANTERIORES FLUJOS SECUNDARIOS DE EGRESADOS ==========
    def action_faq_egresados_menu(self):
        self.ui.agregar_mensaje_bot("🎓 Selecciona el trámite específico para Egresados o Años Posteriores:")
        self.ui.agregar_boton_en_chat(texto_boton="📜 Ingreso a Años Posteriores por Acreditación/Revalidación", comando=self.action_tram_anos_posteriores)
        self.ui.agregar_boton_en_chat(texto_boton="📄 Constancias y Credencial de Egresado", comando=self.action_faq_egresados_bloque)
        self.ui.agregar_boton_en_chat(texto_boton="📜 Expedición de Certificados y Carta Pasante", comando=self.action_faq_egresados_docs_pesados)

    def action_tram_anos_posteriores(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_anos_posteriores_texto())
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_faq_egresados_bloque(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_egresados_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Portal de Exalumnos UNAM", comando=self.abrir_exalumnos_web)

    def abrir_exalumnos_web(self):
        webbrowser.open("http://www.pve.unam.mx/credencial.html")
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_faq_egresados_docs_pesados(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_egresados_documentos_pesados_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Portal Oficial SIGEREL", comando=self.abrir_sigerel_web)

    def abrir_sigerel_web(self):
        webbrowser.open("https://sigerel.dgae.unam.mx")
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_tram_permutas_imss_menu(self):
        self.ui.agregar_mensaje_bot("🤝 Selecciona la duda específica que deseas resolver:")
        self.ui.agregar_boton_en_chat(texto_boton="📜 Ver requisitos para Permutas", comando=self.action_tram_permutas)
        self.ui.agregar_boton_en_chat(texto_boton="🏥 Ver alta de Seguro Médico IMSS", comando=self.action_tram_seguro)

    def action_tram_permutas(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_permutas_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Ir a Servicios Escolares FES", comando=self.abrir_pagina_escolares_fes)

    def action_tram_seguro(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_seguro_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Acceder a IMSS Digital", comando=self.abrir_imss_digital)

    def abrir_imss_digital(self):
        webbrowser.open("https://www.imss.gob.mx/derechohabientes/tramites")
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_tram_bajas_menu(self):
        self.ui.agregar_mensaje_bot("📉 Selecciona el tipo de baja que deseas revisar:")
        self.ui.agregar_boton_en_chat(texto_boton="❌ Solicitar Aclaraciones Generales", comando=self.abrir_pagina_escolares_fes)

    def action_faq_deportes_menu(self):
        self.ui.agregar_mensaje_bot("⚽ Coordinación Deportiva. Selecciona la opción que deseas desglosar:")
        self.ui.agregar_boton_en_chat(texto_boton="📋 Disciplinas, Ejes y Programas (Diverpuma)", comando=self.action_faq_deportes_presentacion)
        self.ui.agregar_boton_en_chat(texto_boton="💰 Requisitos, Costos (Cajas FES) e Inscripciones", comando=self.action_faq_deportes_costos)
        self.ui.agregar_boton_en_chat(texto_boton="🏛️ Infraestructura, Horarios y Contacto Oficial", comando=self.action_faq_deportes_instalaciones)

    def action_faq_deportes_presentacion(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_deportes_presentacion_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Acceder al Sistema de Inscripción SIEFC", comando=self.abrir_siefc_web)

    def action_faq_deportes_costos(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_deportes_costos_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Entrar a la plataforma SIEFC", comando=self.abrir_siefc_web)

    def action_faq_deportes_instalaciones(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_deportes_instalaciones_texto())
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_siefc_web(self):
        webbrowser.open("https://lovelace.aragon.unam.mx/siefc/")
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_faq_intercambio_menu(self):
        """Oficina de Intercambio Académico y Vinculación. Selecciona una opción."""
        self.ui.agregar_mensaje_bot("✈️ Oficina de Intercambio Académico y Vinculación. Selecciona una opción:")
        self.ui.agregar_boton_en_chat(texto_boton="📜 Movilidad para Alumnos Inscritos (DGECI/CRAI)", comando=self.action_faq_intercambio_internos)
        self.ui.agregar_boton_en_chat(texto_boton="🏛️ Alumnos Externos / Estancias / Académicos Visitantes", comando=self.action_faq_intercambio_externos)
        self.ui.agregar_boton_en_chat(texto_boton="📞 Ubicación, Horarios de Oficina y Contacto", comando=self.action_faq_intercambio_contacto)

    def action_faq_intercambio_internos(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_intercambio_alumnos_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Portal Oficial DGAE SIAE Citas", comando=self.abrir_siae_web)

    def action_faq_intercambio_externos(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_intercambio_externos_texto())
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_faq_intercambio_contacto(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_intercambio_contacto_texto())
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_faq_calificaciones(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_calificaciones_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Abrir Sistema SIAE (DGAE UNAM)", comando=self.abrir_gateway_siae_calificaciones)

    def abrir_gateway_siae_calificaciones(self):
        webbrowser.open("https://www.dgae-siae.unam.mx/www_gate.php")
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_faq_horarios_menu(self):
        """Despliega el submenú experto para la gestión de Horarios, Finales y Extraordinarios"""
        self.ui.agregar_mensaje_bot("🕒 Portal de Horarios (Unidad de Cómputo). Selecciona la consulta que deseas realizar:")
        self.ui.agregar_boton_en_chat(texto_boton="📅 1. Horarios de Clases Ordinarios (Materia, Salón, Docente)", comando=self.action_horarios_clases)
        self.ui.agregar_boton_en_chat(texto_boton="📝 2. Calendario de Exámenes Extraordinarios (1ra y 2da Vuelta)", comando=self.action_horarios_extras)
        self.ui.agregar_boton_en_chat(texto_boton="📜 3. Calendario de Exámenes Finales Ordinarios", comando=self.action_horarios_finales)

    def action_horarios_clases(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_horarios_detallado_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Entrar al Portal de Horarios de Clases", comando=self.abrir_sistema_horarios_aragon)

    def action_horarios_extras(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_horarios_extraordinarios_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Entrar a Consulta de Extraordinarios", comando=self.abrir_sistema_extras_aragon)

    def action_horarios_finales(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_horarios_finales_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Entrar a Consulta de Finales", comando=self.abrir_sistema_finales_aragon)

    def abrir_sistema_horarios_aragon(self):
        webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/")
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_sistema_extras_aragon(self):
        webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/extras.php")
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_sistema_finales_aragon(self):
        webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/finales.php")
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_faq_concepto_altas_bajas(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_concepto_altas_bajas_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Entrar Directo a TramiFES", comando=self.abrir_link_tramifes_final)

    def abrir_link_tramifes_final(self):
        webbrowser.open("https://tramifes.aragon.unam.mx/")
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_pagina_escolares_fes(self):
        webbrowser.open("https://www.aragon.unam.mx/fes-aragon/#!/cise/servicios-escolares")
        self.ventana.after(1000, self.preguntar_continuidad)

    def mostrar_inscripcion_nuevo_ingreso(self):
        self.ui.agregar_mensaje_bot(MenuSystem.mensaje_inscripciones())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Acceder al Portal PIIANITE FES", comando=self.abrir_portal_piianite_final)
        self.ui.agregar_boton_en_chat(texto_boton="📄 Descargar Carta Compromiso Oficial", comando=self.descargar_documento_compromiso_final)

    def abrir_portal_piianite_final(self):
        webbrowser.open("http://132.248.44.93:8080/PIIANI/")
        self.ventana.after(1000, self.preguntar_continuidad)

    def descargar_documento_compromiso_final(self):
        webbrowser.open("http://132.248.44.93:8080/PIIANI/doc/CARTA_COMPROMISO_GEN_2026-2.pdf")
        self.ventana.after(1000, self.preguntar_continuidad)

    def mostrar_requisitos_pdf(self):
        self.ui.agregar_mensaje_bot("BotICO: Selecciona el tipo de proceso por el cual deseas ingresar a la UNAM:")
        self.ui.agregar_boton_en_chat(texto_boton="📜 Pase Reglamentado UNAM", comando=self.abrir_pase_reglamentado)
        self.ui.agregar_boton_en_chat(texto_boton="📝 Concurso de Selección", comando=self.abrir_concurso_ingreso)

    def abrir_pase_reglamentado(self):
        webbrowser.open("https://www.dgae.unam.mx/Pase2026/index.html")
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_concurso_ingreso(self):
        webbrowser.open("https://www.dgae-siae.unam.mx")
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_calendario(self):
        webbrowser.open("https://aragon.unam.mx/fes-aragon/public_html/documents/nuestra_facultad/calendario-2026-ll.pdf")
        self.ventana.after(1000, self.preguntar_continuidad)

    # ========== GESTIÓN DE FLUJO ==========
    def preguntar_continuidad(self):
        """Despliega la verificación de continuidad de forma asíncrona."""
        self.ui.agregar_mensaje_bot("BotICO: ¿Te puedo ayudar en algo más?")
        self.ui.agregar_boton_en_chat(texto_boton="👍 Sí, tengo otra duda", comando=self.usuario_desea_continuar)
        self.ui.agregar_boton_en_chat(texto_boton="🛑 No, es todo. Salir", comando=self.usuario_desea_clean_close)

    def usuario_desea_continuar(self):
        """Retorna al flujo de autopilot reinyectando los descriptores en la UI."""
        self.ui.agregar_mensaje_bot("BotICO: ¡Perfecto! Puedes usar los botones inferiores o escribirme tu duda directamente.")
        self.autopilot_regresar_menu()

    def autopilot_regresar_menu(self):
        """Mapea condicionalmente el layout de la botonera baja según el estado."""
        if self.es_nuevo_ingreso:
            self.ui.actualizar_botones(MenuSystem.get_botones_nuevo_ingreso())
        else:
            self.ui.actualizar_botones(MenuSystem.get_botones_principales())

    def Ballback_quit(self):
        """Maneja el cierre seguro del loop de Tkinter."""
        self.ventana.quit()

    def usuario_desea_clean_close(self):
        """Despliega el banner de salida final."""
        self.ui.agregar_mensaje_bot("👋 ¡Gracias por utilizar BotICO! Tu sesión ha finalizado con éxito. ¡Goya!")
        self.ventana.after(2000, self.Ballback_quit)

    def run(self):
        """Punto de entrada síncrono para correr la ventana."""
        self.ventana.mainloop()

if __name__ == "__main__":
    app = BotICO()
    app.run()