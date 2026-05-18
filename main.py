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
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_fechas_inscripcion())
            self.ui.agregar_boton_en_chat("📄 Ver Requisitos Convocatoria", self.mostrar_requisitos_pdf)
            self.ui.actualizar_botones(MenuSystem.get_botones_nuevo_ingreso())
        else:
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_bienvenida_regular(self.nombre_usuario))
            self.ui.actualizar_botones(MenuSystem.get_botones_principales())
    
    def procesar_mensaje(self, mensaje):
        # ========== TRÁMITES (SUBMENÚ) ==========
        if mensaje == "tramites":
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_submenu_tramites())
            for texto, cmd in MenuSystem.get_botones_submenu_tramites():
                self.ui.agregar_boton_en_chat(texto, lambda c=cmd: self.procesar_mensaje(c))
            return
        
        # ========== SUBMENÚ TITULACIÓN ==========
        if mensaje == "submenu_titulacion":
            self.ui.agregar_mensaje_bot("📜 Procesos de Titulación:")
            for texto, cmd in MenuSystem.get_botones_titulacion():
                self.ui.agregar_boton_en_chat(texto, lambda c=cmd: self.procesar_mensaje(c))
            return
        
        # ========== CONSTANCIAS ==========
        if mensaje == "tramite_constancias":
            self.ui.agregar_mensaje_bot(MenuSystem.tramite_constancias_texto())
            self.ui.agregar_boton_en_chat("🌐 TramiFES", self.abrir_tramifes)
            self.preguntar_continuidad()
            return
        
        # ========== SERVICIO SOCIAL ==========
        if mensaje == "servicio_social":
            self.action_servicio_social()
            return
        
        # ========== TITULACIÓN (ACCIONES) ==========
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
        
        # ========== ACTIVIDADES ==========
        if mensaje == "actividades":
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_actividades())
            for texto, cmd in MenuSystem.get_botones_actividades():
                self.ui.agregar_boton_en_chat(texto, lambda c=cmd: self.procesar_mensaje(c))
            return
        
        # ========== DEPORTES ==========
        if mensaje == "actividades_deportes":
            self.ui.agregar_mensaje_bot("⚽ Deportes FES Aragón:")
            for texto, cmd in MenuSystem.get_botones_deportes():
                self.ui.agregar_boton_en_chat(texto, lambda c=cmd: self.procesar_mensaje(c))
            return
        
        # Diccionario de deportes
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
        
        if mensaje in deportes:
            self.ui.agregar_mensaje_bot(deportes[mensaje]())
            if mensaje == "deporte_costos":
                self.ui.agregar_boton_en_chat("💻 SIEFC", self.abrir_siefc)
            elif mensaje == "deporte_contacto":
                self.ui.agregar_boton_en_chat("💻 SIEFC", self.abrir_siefc)
            self.preguntar_continuidad()
            return
        
        if mensaje == "actividades_culturales":
            self.ui.agregar_mensaje_bot("🎨 Talleres culturales: Consulta en Extensión Universitaria.")
            self.preguntar_continuidad()
            return
        if mensaje == "actividades_intercambio":
            self.ui.agregar_mensaje_bot(MenuSystem.faq_intercambio_alumnos_texto())
            self.preguntar_continuidad()
            return
        if mensaje == "actividades_idiomas":
            self.ui.agregar_mensaje_bot("🌐 Centro de Lenguas CLE\n📧 cle.aragon@unam.mx")
            self.ui.agregar_boton_en_chat("🌐 CLE UNAM", lambda: webbrowser.open("https://cle.unam.mx"))
            self.preguntar_continuidad()
            return
        
        # ========== INSCRIPCIONES ==========
        if mensaje == "inscripciones_nuevo":
            self.mostrar_inscripcion_nuevo()
            return
        if mensaje == "inscripciones":
            self.action_inscripcion_regulares()
            return
        
        # ========== HORARIOS ==========
        if mensaje == "horarios":
            self.ui.agregar_mensaje_bot("🕒 Portal de Horarios:")
            self.ui.agregar_boton_en_chat("📅 Horarios", lambda: webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/"))
            self.ui.agregar_boton_en_chat("📝 Extraordinarios", lambda: webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/extras.php"))
            self.ui.agregar_boton_en_chat("📜 Finales", lambda: webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/finales.php"))
            return
        
        # ========== CONTACTOS ==========
        if mensaje == "contactos":
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_contactos())
            return
        
        # ========== PREGUNTAS FRECUENTES ==========
        if mensaje == "preguntas_nuevo" or mensaje == "preguntas":
            self.mostrar_faqs_completo()
            return
        
        # ========== TEXTO LIBRE DEL USUARIO ==========
        self.ui.agregar_mensaje_usuario(mensaje)
        texto = limpiar_texto(mensaje)
        
        # Comandos rápidos
        if texto in ["salir", "adios", "exit", "bye"]:
            self.ui.agregar_mensaje_bot("👋 ¡Hasta pronto!")
            self.ventana.after(1500, self.ventana.quit)
            return
        
        if texto in ["menu", "menú", "ayuda"]:
            self.ui.agregar_mensaje_bot("Usa los botones o escribe tu duda.")
            return
        
        # ========== ALTAS Y BAJAS (DIRECTO) ==========
        if any(p in texto for p in ["altas y bajas", "altas", "bajas", "periodo de altas", "ajustar horario", "no alcance cupo"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_concepto_altas_bajas_texto())
            self.ui.agregar_boton_en_chat("🌐 TramiFES", self.abrir_tramifes)
            self.preguntar_continuidad()
            return
        
        # ========== DEPORTES (DIRECTO) ==========
        if any(p in texto for p in ["deportes", "deporte", "gimnasio", "futbol", "basquet", "taekwondo", "karate", "voleibol", "atletismo", "beisbol", "ajedrez"]):
            self.procesar_mensaje("actividades_deportes")
            return
        
        # ========== SERVICIO SOCIAL (DIRECTO) ==========
        if any(p in texto for p in ["servicio social", "liberacion servicio", "sass"]):
            self.action_servicio_social()
            return
        
        # ========== CONSTANCIAS (DIRECTO) ==========
        if any(p in texto for p in ["constancia", "tira", "historial", "kardex", "boleta"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_constancias_texto())
            self.ui.agregar_boton_en_chat("🌐 TramiFES", self.abrir_tramifes)
            return
        
        # ========== CALENDARIO ==========
        if any(p in texto for p in ["calendario", "fechas", "asueto", "puente", "vacaciones"]):
            self.ui.agregar_mensaje_bot("📅 Calendario oficial FES Aragón:")
            self.ui.agregar_boton_en_chat("📅 Ver Calendario", self.abrir_calendario)
            return
        
        # ========== REINSCRIPCIÓN ==========
        if any(p in texto for p in ["reinscripcion", "pago", "cuota", "scotiabank", "santander", "bbva", "tramifes"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_reinscripcion_texto())
            self.ui.agregar_boton_en_chat("🌐 TramiFES", self.abrir_tramifes)
            return
        
        # ========== CREDENCIAL ==========
        if any(p in texto for p in ["credencial", "resello", "reposicion"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_credencial_texto())
            return
        
        # ========== EXTRAORDINARIOS ==========
        if any(p in texto for p in ["extraordinario", "extra", "reprobe", "oposicion"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_horarios_extraordinarios_texto())
            self.ui.agregar_boton_en_chat("🌐 Ver Extras", lambda: webbrowser.open("https://www.aragon.unam.mx/horarios/horarios/horarios/extras.php"))
            return
        
        # ========== SUSPENSIÓN ==========
        if any(p in texto for p in ["suspension", "baja temporal", "gracia", "congelar"]):
            self.ui.agregar_mensaje_bot(MenuSystem.tram_suspension_texto())
            return
        
        # ========== RECTIFICACIÓN ==========
        if any(p in texto for p in ["rectificacion", "aclaracion", "revalidacion"]):
            self.ui.agregar_mensaje_bot(MenuSystem.tram_rectificacion_texto())
            return
        
        # ========== CAMBIO DE CARRERA ==========
        if any(p in texto for p in ["cambio carrera", "cambio sistema", "suayed"]):
            self.ui.agregar_mensaje_bot(MenuSystem.tram_cambio_carrera_sistema_texto())
            return
        
        # ========== PERMUTAS Y SEGURO ==========
        if any(p in texto for p in ["permuta", "imss", "seguro", "medico"]):
            self.ui.agregar_mensaje_bot(MenuSystem.tram_permutas_texto() + "\n\n" + MenuSystem.tram_seguro_texto())
            return
        
        # ========== CALIFICACIONES ==========
        if any(p in texto for p in ["calificacion", "calificaciones", "siae", "notas", "promedio"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_calificaciones_texto())
            self.ui.agregar_boton_en_chat("🌐 SIAE", self.abrir_siae)
            return
        
        # ========== INTERCAMBIO ==========
        if any(p in texto for p in ["intercambio", "movilidad", "dgeci", "extranjero"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_intercambio_alumnos_texto())
            return
        
        # ========== CONTRASEÑA ==========
        if any(p in texto for p in ["olvide contrasena", "no puedo entrar", "bloqueado", "recuperar"]):
            self.ui.agregar_mensaje_bot(MenuSystem.faq_olvido_contrasena_texto())
            return
        
        # ========== TITULACIÓN (TEXTO LIBRE) ==========
        if any(p in texto for p in ["titulacion", "titulación", "egreso", "normatividad", "seguimiento dgae"]):
            self.procesar_mensaje("tramites")
            return
        
        # Si no entendió nada
        self.ui.agregar_mensaje_bot(MenuSystem.mensaje_no_entendido())
    
    # ========== MENÚ DE PREGUNTAS FRECUENTES COMPLETO ==========
    def mostrar_faqs_completo(self):
        self.ui.agregar_mensaje_bot("❓ ÍNDICE COMPLETO DE PREGUNTAS FRECUENTES ❓")
        
        self.ui.agregar_boton_en_chat("🔑 1. Olvidé mi Contraseña", lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_olvido_contrasena_texto()))
        self.ui.agregar_boton_en_chat("🔄 2. Reinscripción y Pagos", lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_reinscripcion_texto()))
        self.ui.agregar_boton_en_chat("📄 3. Constancias e Historial", lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_constancias_texto()))
        self.ui.agregar_boton_en_chat("🪪 4. Credencial y Resellos", lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_credencial_texto()))
        self.ui.agregar_boton_en_chat("📝 5. Exámenes Extraordinarios", lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_horarios_extraordinarios_texto()))
        self.ui.agregar_boton_en_chat("🛑 6. Suspensión de Estudios", lambda: self.ui.agregar_mensaje_bot(MenuSystem.tram_suspension_texto()))
        self.ui.agregar_boton_en_chat("🔄 7. Rectificación de Notas", lambda: self.ui.agregar_mensaje_bot(MenuSystem.tram_rectificacion_texto()))
        self.ui.agregar_boton_en_chat("🔀 8. Cambio de Carrera/Sistema", lambda: self.ui.agregar_mensaje_bot(MenuSystem.tram_cambio_carrera_sistema_texto()))
        self.ui.agregar_boton_en_chat("🎓 9. Egresados y Certificados", lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_egresados_texto()))
        self.ui.agregar_boton_en_chat("🤝 10. Permutas y Seguro IMSS", lambda: self.ui.agregar_mensaje_bot(MenuSystem.tram_permutas_texto() + "\n\n" + MenuSystem.tram_seguro_texto()))
        self.ui.agregar_boton_en_chat("⚽ 11. Actividades Deportivas", lambda: self.procesar_mensaje("actividades_deportes"))
        self.ui.agregar_boton_en_chat("✈️ 12. Intercambio Académico", lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_intercambio_alumnos_texto()))
        self.ui.agregar_boton_en_chat("📊 13. Consulta de Calificaciones", lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_calificaciones_texto()))
        self.ui.agregar_boton_en_chat("🕒 14. Portal de Horarios", lambda: self.ui.agregar_mensaje_bot("🕒 Usa el botón de Horarios en el menú principal"))
        self.ui.agregar_boton_en_chat("🔄 15. Altas y Bajas", lambda: self.ui.agregar_mensaje_bot(MenuSystem.faq_concepto_altas_bajas_texto()))
    
    # ========== ACCIONES ==========
    def action_servicio_social(self):
        self.ui.agregar_mensaje_bot(MenuSystem.tramite_servicio_social_texto())
        self.ui.agregar_boton_en_chat("💻 Sistema SASS", lambda: webbrowser.open("https://cedco2.aragon.unam.mx/servsocial/"))
        self.ui.agregar_boton_en_chat("📧 Correo SS", lambda: webbrowser.open("mailto:serviciosocial@aragon.unam.mx"))
        self.preguntar_continuidad()
    
    def action_inscripcion_regulares(self):
        self.ui.agregar_mensaje_bot(MenuSystem.faq_inscripcion_regulares_texto())
        self.ui.agregar_boton_en_chat("🌐 TramiFES", self.abrir_tramifes)
        self.ui.agregar_boton_en_chat("📅 Calendario", self.abrir_calendario)
    
    def mostrar_inscripcion_nuevo(self):
        self.ui.agregar_mensaje_bot(MenuSystem.mensaje_inscripciones())
        self.ui.agregar_boton_en_chat("🌐 PIIANITE", lambda: webbrowser.open("http://132.248.44.93:8080/PIIANI/"))
        self.ui.agregar_boton_en_chat("📄 Carta Compromiso", lambda: webbrowser.open("http://132.248.44.93:8080/PIIANI/doc/CARTA_COMPROMISO_GEN_2026-2.pdf"))
    
    def mostrar_requisitos_pdf(self):
        self.ui.agregar_mensaje_bot("Selecciona tu ingreso:")
        self.ui.agregar_boton_en_chat("📜 Pase Reglamentado", lambda: webbrowser.open("https://www.dgae.unam.mx/Pase2026/index.html"))
        self.ui.agregar_boton_en_chat("📝 Concurso", lambda: webbrowser.open("https://www.dgae-siae.unam.mx"))
    
    # ========== UTILERÍAS ==========
    def abrir_tramifes(self):
        webbrowser.open("https://tramifes.aragon.unam.mx/")
        self.preguntar_continuidad()
    
    def abrir_siefc(self):
        webbrowser.open("https://lovelace.aragon.unam.mx/siefc/")
        self.preguntar_continuidad()
    
    def abrir_siae(self):
        webbrowser.open("https://www.dgae-siae.unam.mx")
        self.preguntar_continuidad()
    
    def abrir_forms(self):
        webbrowser.open("https://forms.office.com/pages/responsepage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAN__mF8m8FUQzZJTjdUTVdMUFA5VDQyVTZLWVRDVTRCNS4u")
    
    def abrir_calendario(self):
        webbrowser.open("https://aragon.unam.mx/fes-aragon/public_html/documents/nuestra_facultad/calendario-2026-ll.pdf")
        self.preguntar_continuidad()
    
    def preguntar_continuidad(self):
        self.ui.agregar_mensaje_bot("¿Te puedo ayudar en algo más?")
        self.ui.agregar_boton_en_chat("👍 Sí", self.continuar)
        self.ui.agregar_boton_en_chat("🛑 No, salir", self.salir)
    
    def continuar(self):
        if self.es_nuevo_ingreso:
            self.ui.actualizar_botones(MenuSystem.get_botones_nuevo_ingreso())
        else:
            self.ui.actualizar_botones(MenuSystem.get_botones_principales())
    
    def salir(self):
        self.ui.agregar_mensaje_bot("👋 ¡Gracias por usar BotICO! ¡Goya!")
        self.ventana.after(1500, self.ventana.quit)
    
    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = BotICO()
    app.run()