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
            # 1. Mensaje de bienvenida institucional para primer ingreso
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_bienvenida_nuevo(self.nombre_usuario))
            
            # 2. Fechas oficiales del semestre académico 2026-2
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
            # ALUMNO REGULAR: Bienvenida tradicional y barra inferior de botones generales
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_bienvenida_regular(self.nombre_usuario))
            self.ui.actualizar_botones(MenuSystem.get_botones_principales())
    
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
            self.ui.agregar_boton_en_chat(
                texto_boton="📅 Ver Calendario Oficial 2026-II",
                comando=self.abrir_calendario
            )
            return

        # ========== FILTRADO POR ESTADO EXPERTO (NUEVO VS REGULAR) ==========
        if self.es_nuevo_ingreso:
            # Si escribe inscripción o pulsa el botón de inscripciones de nuevo ingreso
            if mensaje == "inscripciones_nuevo" or categoria == "inscripciones":
                self.mostrar_inscripcion_nuevo_ingreso()
            
            # Si escribe convocatoria o activa la palabra de admisión
            elif categoria == "convocatoria":
                self.ui.agregar_mensaje_bot("BotICO: Con base en tu estatus de Nuevo Ingreso, preparé este acceso rápido para los detalles oficiales de la Convocatoria:")
                self.ui.agregar_boton_en_chat(
                    texto_boton="📄 Ver Requisitos de Convocatoria 2026-1",
                    comando=self.mostrar_requisitos_pdf
                )
            # Redirección inteligente si preguntan por altas o bajas directamente por texto
            elif categoria == "tramites" and any(p in texto_limpio for p in ["alta", "baja", "sorteo"]):
                self.mostrar_detalles_altas_bajas()
            else:
                respuesta = self.obtener_respuesta_por_categoria(categoria, mensaje)
                self.ui.agregar_mensaje_bot(respuesta)
        else:
            # ALUMNO REGULAR: Cualquier consulta (incluyendo altas/bajas) va a sus respuestas ASCII tradicionales
            respuesta = self.obtener_respuesta_por_categoria(categoria, mensaje)
            self.ui.agregar_mensaje_bot(respuesta)

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
            "inscripciones": ["inscripcion", "inscripciones", "inscribirme", "fechas", "documentos", "costo", "pago", "cuota"],
            # Ruteo semántico para altas y bajas mapeado a trámites tradicionales de ventanilla
            "tramites": ["constancia", "certificado", "titulacion", "servicio social", "bajas", "altas", "baja", "alta", "permuta", "sorteo"],
            "actividades": ["taller", "deporte", "cultural", "musica", "teatro", "actividad", "talleres"],
            "calendario": ["calendario", "agenda", "fechas oficiales", "cuando entramos", "inicio de clases"]
        }
        
        for categoria, palabras in palabras_clave.items():
            for palabra in palabras:
                if palabra in texto:
                    return categoria
        return "desconocido"

    def obtener_respuesta_por_categoria(self, categoria, mensaje_original):
        """Mapea las respuestas fijas de menus.py"""
        respuestas = {
            "convocatoria": MenuSystem.mensaje_convocatoria,
            "preguntas": MenuSystem.mensaje_preguntas_nuevo_ingreso,
            "horarios": MenuSystem.mensaje_horarios,
            "contactos": MenuSystem.mensaje_contactos,
            "inscripciones": MenuSystem.mensaje_inscripciones,
            "tramites": MenuSystem.mensaje_tramites,
            "actividades": MenuSystem.mensaje_actividades,
        }
        if categoria in respuestas:
            return respuestas[categoria]()
        return MenuSystem.mensaje_no_entendido()

    # ========== TRÁMITES DE CONVOCATORIA (NUEVO INGRESO) ==========
    def mostrar_requisitos_pdf(self):
        self.ui.agregar_mensaje_bot(
            "BotICO: Selecciona el tipo de proceso por el cual deseas ingresar a la UNAM "
            "para dirigirte al sitio oficial correspondiente:"
        )
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
        """Despliega la información formal de Servicios Escolares"""
        informacion_inscripcion = (
            "🏛️ FACULTAD DE ESTUDIOS SUPERIORES ARAGÓN\n"
            "📢 SECRETARÍA ACADÉMICA\n"
            "🏫 DEPARTAMENTO DE SERVICIOS ESCOLARES\n\n"
            "¡Enhorabuena!\n"
            "A partir de ahora te integras a la comunidad universitaria y nos "
            "congratulamos de saber que formas parte de esta Facultad.\n\n"
            "📋 Deberás tener preparados los siguientes documentos para iniciar tu inscripción:\n"
            "• Carta de asignación firmada (marcada como PLANTEL)\n"
            "• Carta Compromiso (descarga, llena y firma)\n"
            "• Comprobante de aportación voluntaria\n\n"
            "⚠️ ES INDISPENSABLE QUE EL DÍA DE LA INSCRIPCIÓN LOS DOCUMENTOS SE ENCUENTREN EN ORDEN.\n\n"
            "La entrega de documentación incompleta y/o apócrifa, cancelará el trámite "
            "y se procederá conforme a lo establecido en la legislación universitaria.\n\n"
            "📧 Dudas o aclaraciones:\n"
            "Atención de lunes a viernes 9:00 a 20:00 hrs. al correo: serviciosescolares@aragon.unam.mx"
        )
        self.ui.agregar_mensaje_bot(informacion_inscripcion)
        
        # Opción 1: Portal de inscripción PIIANI
        self.ui.agregar_boton_en_chat(texto_boton="🌐 Acceder al Sistema PIIANI FES Aragón", comando=self.abrir_sistema_piiani)
        
        # Opción 2: Descarga de Carta Compromiso PDF
        self.ui.agregar_boton_en_chat(texto_boton="📄 Descargar Carta Compromiso 2026-2", comando=self.descargar_carta_compromiso)

        # Opción 3: Portal de la Coordinación CISE Servicios Escolares
        self.ui.agregar_boton_en_chat(texto_boton="🏫 Página Servicios Escolares FES", comando=self.abrir_pagina_escolares_fes)

        # Opción 4: Cambia el comando directo para que primero despliegue el desglose detallado
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

    # ========== NUEVA SECCIÓN DETALLADA: PASO A PASO DE ALTAS Y BAJAS ==========
    def mostrar_detalles_altas_bajas(self):
        """Desglosa la guía paso a paso basada en el diagrama oficial de la FES"""
        guia_pasos = (
            "🔄 PROCESO DETALLADO DE ALTAS Y BAJAS (TramiFES)\n\n"
            "Sigue cuidadosamente estos pasos para realizar tus modificaciones de horario de forma correcta:\n\n"
            "1️⃣ CONSULTAR TU CITA:\n"
            "   Ingresa al portal de TramiFES para verificar el día y la hora exacta que se te "
            "asignó mediante el sorteo automatizado.\n\n"
            "2️⃣ ACCEDER EN TU HORARIO:\n"
            "   Deberás ingresar al sistema estrictamente dentro del periodo de tiempo que "
            "marca tu cita. Fuera de ese horario el acceso estará deshabilitado.\n\n"
            "3️⃣ REALIZAR TUS MOVIMIENTOS:\n"
            "   Dentro de la plataforma podrás dar de baja asignaturas o solicitar el alta en "
            "los grupos y materias que tengan cupos o lugares disponibles.\n\n"
            "4️⃣ GUARDAR COMPROBANTE:\n"
            "   Al finalizar tus cambios, es obligatorio que guardes e imprimas tu comprobante "
            "oficial de movimientos. Este documento es tu único respaldo legal ante la facultad."
        )
        self.ui.agregar_mensaje_bot(guia_pasos)
        
        # Le pintamos el botón directo para ir al portal ya que leyó las instrucciones
        self.ui.agregar_boton_en_chat(
            texto_boton="🌐 Ir a la plataforma TramiFES ahora",
            comando=self.abrir_link_tramifes_final
        )

    def abrir_link_tramifes_final(self):
        """Abre la URL y ejecuta la pasarela de control de flujo"""
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