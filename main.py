# main.py - Punto de entrada principal del chatbot escolar
import tkinter as tk
import webbrowser
from auth import AuthManager
from ui import UI
from menus import MenuSystem
from config import COLORS, NOMBRE_APP
from utils import limpiar_texto

class BotICO:
    def __init__(self):
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
        self.ventana.update_idletasks()
        x = (self.ventana.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (650 // 2)
        self.ventana.geometry(f"+{x}+{y}")
    
    def mostrar_registro(self):
        def after_registro(nombre, es_nuevo):
            self.nombre_usuario = nombre
            self.es_nuevo_ingreso = es_nuevo
            self.construir_interfaz()
        
        AuthManager(self.ventana, after_registro).solicitar_registro()
    
    def construir_interfaz(self):
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
        respuesta = self.obtener_respuesta_por_categoria(categoria, mensaje)
        self.ui.agregar_mensaje_bot(respuesta)

    def procesar_mensaje(self, mensaje):
        """Procesa mensajes del usuario (texto libre o comandos de los botones de la interfaz)"""
        self.ui.agregar_mensaje_usuario(mensaje)
        
        texto_limpio = limpiar_texto(mensaje)
        if texto_limpio in ["salir", "adios", "exit", "chao"]:
            self.ui.agregar_mensaje_bot("👋 ¡Gracias por usar BotICO! Hasta pronto.")
            self.ventana.after(1500, self.ventana.quit)
            return
        
        if texto_limpio in ["menu", "menú", "ayuda", "opciones"]:
            if self.es_nuevo_ingreso:
                self.ui.agregar_mensaje_bot("📋 Opciones: Convocatoria, Horarios, Contactos, Preguntas Frecuentes, Calendario")
            else:
                self.ui.agregar_mensaje_bot("📋 Opciones: Inscripciones, Horarios, Trámites, Contactos, Actividades, Calendario")
            return
        
        categoria = self.evaluar_categoria(mensaje)
        
        # ========== INTERCEPTACIÓN GLOBAL: CALENDARIO ESCOLAR ==========
        if categoria == "calendario":
            self.ui.agregar_mensaje_bot("BotICO: Aquí tienes el acceso directo al calendario oficial de la FES Aragón:")
            self.ui.agregar_boton_en_chat(texto_boton="📅 Ver Calendario Oficial 2026-II", comando=self.abrir_calendario)
            return

        # ========== INTERCEPTACIÓN GLOBAL COMPLETA POR TEXTO LIBRE ==========
        if any(p in texto_limpio for p in ["cuando me inscribo", "fecha de inscripcion", "cuando me toca", "pago cuota", "ordinario", "reinscripcion", "reinscribirme", "scotiabank", "santander", "bbva", "ficha", "deposito", "adeudo", "biblioteca", "fundacion"]):
            self.action_faq_reinscripcion()
            return
        if any(p in texto_limpio for p in ["altas y bajas", "sorteo", "cambiar materia", "trami", "tramifes", "mi cita", "que dia me toca", "mover materia", "permutar grupo"]):
            self.mostrar_detalles_altas_bajas()
            return
        if any(p in texto_limpio for p in ["constancia", "estudios", "creditos", "historial", "tira", "boleta", "kardex", "materias aprobadas", "porcentaje", "promedio general", "sellada", "firmada"]):
            self.action_faq_constancias()
            return
        if any(p in texto_limpio for p in ["credencial", "resello", "reposicion", "crede", "perdi mi credencial", "tarjeta unam", "plastico", "sello anual"]):
            self.action_faq_credencial()
            return
        if any(p in texto_limpio for p in ["extraordinario", "extra", "extras", "reprobe", "pasar materia", "oposicion", "pagar extra"]):
            self.action_horarios_extras()
            return
        if any(p in texto_limpio for p in ["suspension", "baja temporal", "gracia", "dejar de estudiar", "pausar", "periodo de gracia", "congelar un año"]):
            self.action_tram_suspension()
            return
        if any(p in texto_limpio for p in ["rectificacion", "aclaracion calificacion", "cambio calificacion", "revalidacion", "movilidad", "intercambio", "f306", "revalidar", "clase espejo", "coil"]):
            self.action_tram_rectificacion()
            return
        if any(p in texto_limpio for p in ["cambio interno", "cambio de carrera", "cambio de sistema", "cambio modalidad", "8.5", "suayed", "siae", "dgae", "modalidad abierta", "modalidad distancia"]):
            self.action_tram_cambio_carrera_sistema()
            return
        if any(p in texto_limpio for p in ["años posteriores", "acreditacion", "incorporado", "revalidación", "vengo de incorporada", "externa", "licenciatura externa"]):
            self.action_tram_anos_posteriores()
            return
        if any(p in texto_limpio for p in ["egresado", "egresados", "certificado de estudios", "carta pasante", "titulacion", "titularme", "pasante", "dgp", "sep", "sigerel", "exalumnos"]):
            self.action_faq_egresados_menu()
            return
        if any(p in texto_limpio for p in ["permuta", "permutas", "cambio de plantel", "cambio de fec"]):
            self.action_tram_permutas_imss_menu()
            return
        if any(p in texto_limpio for p in ["imss", "seguro", "facultativo", "medico", "médico", "clinica", "alta imss", "seguridad social", "nss"]):
            self.action_tram_permutas_imss_menu()
            return
        if any(p in texto_limpio for p in ["baja materia", "baja materias", "baja asignatura", "bajas asignaturas", "baja semestre", "baja definitiva", "baja total", "renunciar carrera", "extemporanea"]):
            self.action_tram_bajas_menu()
            return
        if any(p in texto_limpio for p in ["deporte", "deportes", "futbol", "basquet", "gimnasio", "pesas", "siefc", "instalaciones", "carlos octavio", "ajedrez", "karate", "taekwondo", "ludoteca", "diverpuma", "95 pesos", "390", "115"]):
            self.action_faq_deportes_menu()
            return
        if any(p in texto_limpio for p in ["intercambio", "movilidad", "dgeci", "crai", "coil", "clase espejo", "pittaae", "toefl", "ielts", "extranjero", "beca internacional", "44%"]):
            self.action_faq_intercambio_menu()
            return
        if any(p in texto_limpio for p in ["calificacion", "calificaciones", "sabes calificacion", "ver notas", "ver calificacion", "subieron actas", "promedio", "siae notas"]):
            self.action_faq_calificaciones()
            return
        if any(p in texto_limpio for p in ["horario", "horarios", "como checo mi horario", "finales", "combo grupo", "vuelta", "salon", "docente", "sinodales", "materia", "filtrar por materia"]):
            self.action_faq_horarios_menu()
            return

        # ========== FILTRADO POR ESTADO EXPERTO (NUEVO VS REGULAR) ==========
        if self.es_nuevo_ingreso:
            if mensaje == "inscripciones_nuevo" or categoria == "inscripciones":
                self.mostrar_inscripcion_nuevo_ingreso()
            elif mensaje == "preguntas_nuevo" or categoria == "preguntas" or mensaje == "tramites" or categoria == "tramites":
                self.mostrar_menu_preguntas_frecuentes_acciones()
            elif mensaje == "horarios" or categoria == "horarios":
                self.action_faq_horarios_menu()
            elif categoria == "convocatoria":
                self.ui.agregar_mensaje_bot("BotICO: Con base en tu estatus de Nuevo Ingreso, preparé este acceso rápido para los detalles oficiales de la Convocatoria:")
                self.ui.agregar_boton_en_chat(texto_boton="📄 Ver Requisitos de Convocatoria 2026-1", comando=self.mostrar_requisitos_pdf)
            else:
                self.process_mensaje_directo(categoria, mensaje)
        else:
            # ALUMNO REGULAR
            if mensaje == "preguntas" or categoria == "preguntas" or mensaje == "tramites" or categoria == "tramites":
                self.mostrar_menu_preguntas_frecuentes_acciones()
            elif mensaje == "horarios" or categoria == "horarios":
                self.action_faq_horarios_menu()
            else:
                self.process_mensaje_directo(categoria, mensaje)

    def evaluar_categoria(self, comando):
        """Diccionario semántico con mapeo avanzado de intenciones estudiantiles"""
        texto = limpiar_texto(comando)
        comandos_directos = ["inscripciones_nuevo", "co4nvocatoria", "preguntas_nuevo", "preguntas", 
                             "horarios", "contactos", "contacto", "inscripciones", "tramites", "actividades", "calendario"]
        
        if comando in comandos_directos:
            if comando in ["inscripciones_nuevo", "co4nvocatoria"]: return "convocatoria"
            if comando in ["preguntas_nuevo", "preguntas"]: return "preguntas"
            if comando in ["contacto"]: return "contactos"
            return comando
            
        palabras_clave = {
            "convocatoria": ["convocatoria", "ingreso", "admision", "examen", "pase reglamentado", "primer ingreso", "nuevo ingreso"],
            "horarios": ["horario", "horarios", "materias", "clases", "profesores", "grupo", "turno", "finales", "extraordinarios", "vuelta", "salon", "docente"],
            "contactos": ["telefono", "correo", "direccion", "contacto", "redes", "facebook", "ubicacion", "oficina", "ventanilla", "edificio"],
            "inscripciones": ["inscripcion", "inscripciones", "pago", "banco", "costo", "cuota", "referencia", "cajas", "ficha"],
            "tramites": ["constancia", "certificado", "titulacion", "servicio social", "bajas", "altas", "baja", "alta", "permuta", "sorteo", "cita", "extra", "suspension", "rectificacion", "revalidacion", "turno", "simultanea", "imss", "seguro", "egresado", "acreditacion", "pasante"],
            "actividades": ["taller", "deporte", "cultural", "musica", "idiomas", "cle", "ingles", "futbol", "basquet", "talleres", "teatro", "gimnasio", "pesas", "siefc", "ludoteca", "diverpuma", "intercambio", "movilidad", "dgeci", "coil", "erasmus", "toefl", "extranjero"]
        }
        for cat, palabras in palabras_clave.items():
            for p in palabras:
                if p in texto: return cat
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

    # ========== MÓDULO UNIFICADO DE PREGUNTAS FRECUENTES (SÚPER ÍNDICE DE ACCIONES) ==========
    def mostrar_menu_preguntas_frecuentes_acciones(self):
        """Muestra el índice unificado completo de Preguntas Frecuentes y Trámites"""
        self.ui.agregar_mensaje_bot("❓ Índice Completo de Preguntas Frecuentes y Trámites de Servicios Escolares:")
        
        self.ui.agregar_boton_en_chat(texto_boton="🔄 1. Reinscripción, Sorteos y Pagos", comando=self.action_faq_reinscripcion)
        self.ui.agregar_boton_en_chat(texto_boton="📄 2. Tramitar Constancias e Historial", comando=self.action_faq_constancias)
        self.ui.agregar_boton_en_chat(texto_boton="🪪 3. Nueva Credencial y Resellos", comando=self.action_faq_credencial)
        self.ui.agregar_boton_en_chat(texto_boton="📝 4. Exámenes Extraordinarios (Extras)", comando=self.action_horarios_extras)
        self.ui.agregar_boton_en_chat(texto_boton="🛑 5. Suspensión Temporal de Estudios", comando=self.action_tram_suspension)
        self.ui.agregar_boton_en_chat(texto_boton="🔄 6. Rectificación / Revalidación de Notas", comando=self.action_tram_rectificacion)
        self.ui.agregar_boton_en_chat(texto_boton="🔀 7. Cambios de Carrera / De Sistema (SUAyED)", comando=self.action_tram_cambio_carrera_sistema)
        self.ui.agregar_boton_en_chat(texto_boton="🎓 8. Ingreso a Años Posteriores / Egresados", comando=self.action_faq_egresados_menu)
        self.ui.agregar_boton_en_chat(texto_boton="🤝 9. Permutas e Inscripción al IMSS", comando=self.action_tram_permutas_imss_menu)
        self.ui.agregar_boton_en_chat(texto_boton="📉 10. Bajas de Materias o del Semestre", comando=self.action_tram_bajas_menu)
        self.ui.agregar_boton_en_chat(texto_boton="⚽ 11. Actividades Deportivas y Recreativas", comando=self.action_faq_deportes_menu)
        self.ui.agregar_boton_en_chat(texto_boton="✈️ 12. Intercambio Académico y Movilidad UNAM", comando=self.action_faq_intercambio_menu)
        self.ui.agregar_boton_en_chat(texto_boton="📊 13. Consulta de Calificaciones e Historial (SIAE)", comando=self.action_faq_calificaciones)
        self.ui.agregar_boton_en_chat(texto_boton="🕒 14. Portal de Horarios, Finales y Extraordinarios", comando=self.action_faq_horarios_menu)

    # ========== CONTROLADORES DE ACCIONES INDIVIDUALES ==========
    def action_faq_reinscripcion(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_reinscripcion_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Entrar al Sistema TramiFES", comando=self.abrir_link_tramifes_final)
        self.ui.agregar_boton_en_chat(texto_boton="📋 Ver Guía de Sorteo Altas/Bajas", comando=self.mostrar_detalles_altas_bajas)

    def action_faq_constancias(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_constancias_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Ir al Portal Escolar CISE FES", comando=self.abrir_pagina_escolares_fes)

    def action_faq_credencial(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_credencial_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Acceder a Servicios Escolares Web", comando=self.abrir_pagina_escolares_fes)

    def action_faq_certificados(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_certificados_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🤝 Consultar Servicio Social FES", comando=self.abrir_servicio_social)

    def abrir_servicio_social(self):
        webbrowser.open("https://www.fes-aragon.unam.mx/servicio-social")
        self.ventana.after(1000, self.preguntar_continuidad)

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
        self.ui.agregar_boton_en_chat(texto_boton="📋 Baja parcial de asignaturas", comando=self.action_tram_baja_materias)
        self.ui.agregar_boton_en_chat(texto_boton="❌ Baja total del Semestre / Definitiva", comando=self.action_tram_baja_semestre)

    def action_tram_baja_materias(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_baja_materias_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Entrar a TramiFES", comando=self.abrir_link_tramifes_final)

    def action_tram_baja_semestre(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_baja_semestre_texto())
        self.ui.agregar_boton_en_chat(texto_boton="📖 Ver Directorio de Ventanillas", comando=self.abrir_pagina_escolares_fes)

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

    # ========== MÓDULO INTERACTIVO DE CONTROL DE HORARIOS Y EXÁMENES ==========
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

    # ========== ENLACES GLOBALES E INSCRIPCIÓN ==========
    def mostrar_inscripcion_nuevo_ingreso(self):
        informacion_inscripcion = (
            "🏛️ FACULTAD DE ESTUDIOS SUPERIORES ARAGÓN\n"
            "📢 SECRETARÍA ACADÉMICA\n"
            "🏫 DEPARTAMENTO DE SERVICIOS ESCOLARES\n\n"
            "¡Enhorabuena! Te integras a la comunidad de Ingeniería en Computación.\n\n"
            "📋 Requisitos indispensables para tu inscripción:\n"
            "• Carta de asignación firmada (marcada como PLANTEL)\n"
            "• Carta Compromiso (descarga, llena y firma)\n"
            "• Comprobante de aportación voluntaria\n\n"
            "📧 Dudas: serviciosescolares@aragon.unam.mx"
        )
        self.ui.agregar_mensaje_bot(informacion_inscripcion)
        
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Acceder al Sistema PIIANI FES Aragón", comando=self.open_piiani)
        self.ui.agregar_boton_en_chat(texto_boton="📄 Descargar Carta Compromiso 2026-2", comando=self.descargar_carta_compromiso)
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Página Servicios Escolares FES", comando=self.abrir_pagina_escolares_fes)
        self.ui.agregar_boton_en_chat(texto_boton="🔄 Sistema de Altas y Bajas TramiFES", comando=self.mostrar_detalles_altas_bajas)

    def open_piiani(self):
        webbrowser.open("http://132.248.44.93:8080/PIIANI/")
        self.ventana.after(1000, self.preguntar_continuidad)

    def descargar_carta_compromiso(self):
        webbrowser.open("http://132.248.44.93:8080/PIIANI/doc/CARTA_COMPROMISO_GEN_2026-2.pdf")
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_pagina_escolares_fes(self):
        webbrowser.open("https://www.aragon.unam.mx/fes-aragon/#!/cise/servicios-escolares")
        self.ventana.after(1000, self.preguntar_continuidad)

    def mostrar_detalles_altas_bajas(self):
        guia_pasos = (
            "🔄 PROCESO DETALLADO DE ALTAS Y BAJAS (TramiFES)\n\n"
            "1️⃣ CONSULTAR TU CITA:\n"
            "   Ingresa a TramiFES para verificar el día y la hora de tu sorteo.\n\n"
            "2️⃣ ACCEDER EN TU HORARIO:\n"
            "   Debes ingresar estrictamente dentro del periodo marcado.\n\n"
            "3️⃣ REALIZAR TUS MOVIMIENTOS:\n"
            "   Baja asignaturas o solicita alta en los grupos con cupos disponibles.\n\n"
            "4️⃣ GUARDAR COMPROBANTE:\n"
            "   Es obligatorio imprimir tu comprobante como tu único respaldo legal."
        )
        self.ui.agregar_mensaje_bot(guia_pasos)
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Ir a la plataforma TramiFES ahora", comando=self.abrir_link_tramifes_final)

    def abrir_link_tramifes_final(self):
        webbrowser.open("https://tramifes.aragon.unam.mx/")
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_calendario(self):
        webbrowser.open("https://aragon.unam.mx/fes-aragon/public_html/documents/nuestra_facultad/calendario-2026-ll.pdf")
        self.ventana.after(1000, self.preguntar_continuidad)

    def mostrar_requisitos_pdf(self):
        self.ui.agregar_mensaje_bot("BotICO: Selecciona el tipo de proceso por el cual deseas ingresar a la UNAM:")
        self.ui.agregar_boton_en_chat(texto_boton="📜 Pase Reglamentado UNAM", comando=self.abrir_pase_reglamentado)
        self.ui.agregar_boton_en_chat(texto_boton="📝 Concurso de Selección", comando=self.abrir_concurso_ingreso)

    def abrir_pase_reglamentado(self):
        webbrowser.open("https://www.dgae.unam.mx/Pase2026/index.html")
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_concurso_ingreso(self):
        webbrowser.open("https://www.dgae.unam.mx/admision_licenciatura/")
        self.ventana.after(1000, self.preguntar_continuidad)

    # ========== GESTIÓN DE FLUJO ("¿ALGO MÁS?") ==========
    def preguntar_continuidad(self):
        self.ui.agregar_mensaje_bot("BotICO: ¿Te puedo ayudar en algo más?")
        self.ui.agregar_boton_en_chat(texto_boton="👍 Sí, tengo otra duda", comando=self.usuario_desea_continuar)
        self.ui.agregar_boton_en_chat(texto_boton="🛑 No, es todo. Salir", comando=self.usuario_desea_clean_close)

    def usuario_desea_continuar(self):
        self.ui.agregar_mensaje_bot("BotICO: ¡Perfecto! Puedes usar los botones inferiores o escribirme tu duda directamente.")
        self.autopilot_regresar_menu()

    def autopilot_regresar_menu(self):
        """Helper para re-inyectar los descriptores en el chat de forma fluida"""
        if self.es_nuevo_ingreso:
            self.ui.actualizar_botones(MenuSystem.get_botones_nuevo_ingreso())
        else:
            self.ui.actualizar_botones(MenuSystem.get_botones_principales())

    def usuario_desea_clean_close(self):
        self.ui.agregar_mensaje_bot("👋 ¡Gracias por utilizar BotICO! Tu sesión ha finalizado con éxito. ¡Goya!")
        self.ventana.after(2000, self.ventana.quit)

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = BotICO()
    app.run()