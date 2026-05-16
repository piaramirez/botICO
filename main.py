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

        # ========== INTERCEPTACIÓN GLOBAL: TEXTO LIBRE DE PREGUNTAS FRECUENTES ==========
        if any(p in texto_limpio for p in ["cuando me inscribo", "fecha de inscripcion", "cuando me toca"]):
            self.action_faq_reinscripcion()
            return
        if any(p in texto_limpio for p in ["altas y bajas", "sorteo", "cambiar materia", "trami", "tramifes"]):
            self.mostrar_detalles_altas_bajas()
            return
        if any(p in texto_limpio for p in ["constancia", "estudios", "creditos", "historial", "tira"]):
            self.action_faq_constancias()
            return
        if any(p in texto_limpio for p in ["credencial", "resello", "reposicion"]):
            self.action_faq_credencial()
            return
        if any(p in texto_limpio for p in ["certificado", "pasante", "carta pasante"]):
            self.action_faq_certificados()
            return
        if any(p in texto_limpio for p in ["extraordinario", "extra", "extras"]):
            self.action_tram_extraordinarios()
            return
        if any(p in texto_limpio for p in ["suspension", "baja temporal", "gracia"]):
            self.action_tram_suspension()
            return
        if any(p in texto_limpio for p in ["rectificacion", "aclaracion calificacion", "cambio calificacion", "revalidacion", "movilidad"]):
            self.action_tram_rectificacion()
            return
        if any(p in texto_limpio for p in ["cambio de turno", "turno matutino", "turno vespertino", "simultanea", "carrera simultanea"]):
            self.action_tram_cambio_turno()
            return
        if any(p in texto_limpio for p in ["permuta", "permutas", "cambio de plantel"]):
            self.action_tram_permutas()
            return
        if any(p in texto_limpio for p in ["imss", "seguro", "facultativo", "medico", "médico"]):
            self.action_tram_seguro()
            return
        if any(p in texto_limpio for p in ["baja materia", "baja materias", "baja asignatura", "bajas asignaturas"]):
            self.action_tram_baja_materias()
            return
        if any(p in texto_limpio for p in ["baja semestre", "baja definitiva", "baja total", "renunciar carrera"]):
            self.action_tram_baja_semestre()
            return

        # ========== FILTRADO POR ESTADO EXPERTO (NUEVO VS REGULAR) ==========
        if self.es_nuevo_ingreso:
            if mensaje == "inscripciones_nuevo" or categoria == "inscripciones":
                self.mostrar_inscripcion_nuevo_ingreso()
            elif mensaje == "preguntas_nuevo" or categoria == "preguntas" or mensaje == "tramites" or categoria == "tramites":
                # Consolidamos todo en la súper botonera unificada de preguntas frecuentes
                self.mostrar_menu_preguntas_frecuentes_acciones()
            elif categoria == "convocatoria":
                self.ui.agregar_mensaje_bot("BotICO: Con base en tu estatus de Nuevo Ingreso, preparé este acceso rápido para los detalles oficiales de la Convocatoria:")
                self.ui.agregar_boton_en_chat(texto_boton="📄 Ver Requisitos de Convocatoria 2026-1", comando=self.mostrar_requisitos_pdf)
            else:
                self.process_mensaje_directo(categoria, mensaje)
        else:
            # ALUMNO REGULAR
            if mensaje == "preguntas" or categoria == "preguntas" or mensaje == "tramites" or categoria == "tramites":
                self.mostrar_menu_preguntas_frecuentes_acciones()
            else:
                self.process_mensaje_directo(categoria, mensaje)

    def evaluar_categoria(self, comando):
        """Diccionario de palabras clave (IF-THEN) con soporte para variaciones lingüísticas"""
        comandos_directos = ["inscripciones_nuevo", "co4nvocatoria", "preguntas_nuevo", "preguntas", 
                             "horarios", "contactos", "contacto", "inscripciones", "tramites", "actividades", "calendario"]
        
        if comando in comandos_directos:
            if comando in ["inscripciones_nuevo", "co4nvocatoria"]: return "convocatoria"
            if comando in ["preguntas_nuevo", "preguntas"]: return "preguntas"
            if comando in ["contacto"]: return "contactos"
            return comando
            
        texto = limpiar_texto(comando)
        
        palabras_clave = {
            "convocatoria": ["convocatoria", "ingreso", "admision", "examen", "nuevo ingreso"],
            "horarios": ["horario", "horarios", "cambio", "extraordinario", "materias", "turno"],
            "contactos": ["telefono", "correo", "direccion", "contacto", "atencion", "contactos"],
            "inscripciones": ["inscripcion", "inscripciones", "inscribirme", "fechas", "documentos", "pago"],
            "tramites": ["constancia", "certificado", "titulacion", "servicio social", "bajas", "altas", "baja", "alta", "permuta", "sorteo", "cita", "extra", "suspension", "rectificacion", "revalidacion", "turno", "simultanea", "imss", "seguro", "facultativo"],
            "actividades": ["taller", "deporte", "cultural", "musica", "teatro", "actividad", "talleres"],
            "calendario": ["calendario", "agenda", "fechas oficiales", "cuando entramos", "inicio de clases"]
        }
        
        for categoria, palabras in palabras_clave.items():
            for palabra in palabras:
                if palabra in texto:
                    return categoria
        return "desconocido"

    def obtener_respuesta_por_categoria(self, categoria, mensaje_original):
        respuestas = {
            "convocatoria": MenuSystem.mensaje_convocatoria,
            "horarios": MenuSystem.mensaje_horarios,
            "contactos": MenuSystem.mensaje_contactos,
            "inscripciones": MenuSystem.mensaje_inscripciones,
            "actividades": MenuSystem.mensaje_actividades,
        }
        if category in respuestas:
            return respuestas[categoria]()
        return MenuSystem.mensaje_no_entendido()

    # ========== MÓDULO UNIFICADO DE PREGUNTAS FRECUENTES (SÚPER ÍNDICE DE ACCIONES) ==========
    def mostrar_menu_preguntas_frecuentes_acciones(self):
        """Muestra el índice unificado completo de Preguntas Frecuentes y Trámites"""
        self.ui.agregar_mensaje_bot("❓ Índice Completo de Preguntas Frecuentes y Trámites de Servicios Escolares:")
        
        self.ui.agregar_boton_en_chat(texto_boton="🔄 1. Reinscripción, Sorteos y Pagos", comando=self.action_faq_reinscripcion)
        self.ui.agregar_boton_en_chat(texto_boton="📄 2. Tramitar Constancias e Historial", comando=self.action_faq_constancias)
        self.ui.agregar_boton_en_chat(texto_boton="🪪 3. Nueva Credencial y Resellos", comando=self.action_faq_credencial)
        self.ui.agregar_boton_en_chat(texto_boton="📜 4. Certificados y Carta Pasante", comando=self.action_faq_certificados)
        self.ui.agregar_boton_en_chat(texto_boton="📝 5. Exámenes Extraordinarios (Extras)", comando=self.action_tram_extraordinarios)
        self.ui.agregar_boton_en_chat(texto_boton="🛑 6. Suspensión Temporal de Estudios", comando=self.action_tram_suspension)
        self.ui.agregar_boton_en_chat(texto_boton="🔄 7. Rectificación / Revalidación de Notas", comando=self.action_tram_rectificacion)
        self.ui.agregar_boton_en_chat(texto_boton="🔀 8. Cambios de Turno / Carrera Simultánea", comando=self.action_tram_cambio_turno)
        self.ui.agregar_boton_en_chat(texto_boton="🤝 9. Permutas e Inscripción al IMSS", comando=self.action_tram_permutas_imss_menu)
        self.ui.agregar_boton_en_chat(texto_boton="📉 10. Bajas de Materias o del Semestre", comando=self.action_tram_bajas_menu)

    # ========== DESGLOSE DE ACCIONES DE PREGUNTAS FRECUENTES ==========
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

    def action_tram_extraordinarios(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_extraordinarios_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Ver Fechas en Calendario FES", comando=self.abrir_calendario)

    def action_tram_suspension(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_suspension_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Consultar en el Portal del CISE", comando=self.abrir_pagina_escolares_fes)

    def action_tram_rectificacion(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_rectificacion_texto())
        self.ventana.after(1000, self.preguntar_continuidad)

    def action_tram_cambio_turno(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_cambio_turno_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Verificar Convocatorias Activas", comando=self.abrir_pagina_escolares_fes)

    # Submenús internos para optimizar la vista en pantalla
    def action_tram_permutas_imss_menu(self):
        self.ui.agregar_mensaje_bot("🤝 Selecciona la duda específica que deseas resolver:")
        self.ui.agregar_boton_en_chat(texto_boton="📜 Ver requisitos para Permutas", comando=self.action_tram_permutas)
        self.ui.agregar_boton_en_chat(texto_boton="🏥 Ver alta de Seguro Médico IMSS", comando=self.action_tram_seguro)

    def action_tram_permutas(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_permutas_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Ir a Servicios Escolares FES", comando=self.abrir_pagina_escolares_fes)

    def action_tram_seguro(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tram_seguro_texto())
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Registrar NSS en portal FES", comando=self.abrir_pagina_escolares_fes)

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

    # ========== TRÁMITES DE CONVOCATORIA (NUEVO INGRESO) ==========
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

    # ========== TRÁMITES DE INSCRIPCIÓN (NUEVO INGRESO) ==========
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
        
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Acceder al Sistema PIIANI FES Aragón", comando=self.abrir_sistema_piiani)
        self.ui.agregar_boton_en_chat(texto_boton="📄 Descargar Carta Compromiso 2026-2", comando=self.descargar_carta_compromiso)
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Página Servicios Escolares FES", comando=self.abrir_pagina_escolares_fes)
        self.ui.agregar_boton_en_chat(texto_boton="🔄 Sistema de Altas y Bajas TramiFES", comando=self.mostrar_detalles_altas_bajas)

    def abrir_sistema_piiani(self):
        webbrowser.open("http://132.248.44.93:8080/PIIANI/")
        self.ventana.after(1000, self.preguntar_continuidad)

    def descargar_carta_compromiso(self):
        webbrowser.open("http://132.248.44.93:8080/PIIANI/doc/CARTA_COMPROMISO_GEN_2026-2.pdf")
        self.ventana.after(1000, self.preguntar_continuidad)

    def abrir_pagina_escolares_fes(self):
        webbrowser.open("https://www.aragon.unam.mx/fes-aragon/#!/cise/servicios-escolares")
        self.ventana.after(1000, self.preguntar_continuidad)

    # ========== SECCIÓN DETALLADA: PASO A PASO DE ALTAS Y BAJAS ==========
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

    # ========== MÉTODOS DE CONTROL GLOBAL ==========
    def abrir_calendario(self):
        webbrowser.open("https://aragon.unam.mx/fes-aragon/public_html/documents/nuestra_facultad/calendario-2026-ll.pdf")
        self.ventana.after(1000, self.preguntar_continuidad)

    # ========== SECCIÓN DE GESTIÓN DE FLUJO ("¿ALGO MÁS?") ==========
    def preguntar_continuidad(self):
        self.ui.agregar_mensaje_bot("BotICO: ¿Te puedo ayudar en algo más?")
        self.ui.agregar_boton_en_chat(texto_boton="👍 Sí, tengo otra duda", comando=self.usuario_desea_continuar)
        self.ui.agregar_boton_en_chat(texto_boton="🛑 No, es todo. Salir", comando=self.usuario_desea_clean_close)

    def usuario_desea_continuar(self):
        self.ui.agregar_mensaje_bot("BotICO: ¡Perfecto! Puedes usar los botones inferiores o escribirme tu duda directamente.")

    def usuario_desea_clean_close(self):
        self.ui.agregar_mensaje_bot("👋 ¡Gracias por utilizar BotICO! Tu sesión ha finalizado con éxito. ¡Goya!")
        self.ventana.after(2000, self.ventana.quit)

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = BotICO()
    app.run()