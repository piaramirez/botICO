# main.py - Punto de entrada principal
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
            # 1. Mensaje de bienvenida
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_bienvenida_nuevo(self.nombre_usuario))
            
            # 2. Modificamos para separar el texto plano y meter el botón interactivo desde el inicio
            texto_inicial = (
                "╔══════════════════════════════════════════════════════════════════╗\n"
                "║                    📅 FECHAS DE INSCRIPCIÓN - ICO                ║\n"
                "╠══════════════════════════════════════════════════════════════════╣\n"
                "║  🗓️ SEMESTRE 2025-2:                                            ║\n"
                "║     • Registro en línea: 10 - 25 de enero                        ║\n"
                "║     • Pago de cuotas: 10 - 28 de enero                           ║\n"
                "║     • Inicio de clases: Primera semana de febrero                ║\n"
                "╚══════════════════════════════════════════════════════════════════╝"
            )
            self.ui.agregar_mensaje_bot(texto_inicial)
            
            # 3. Insertamos el botón interactivo directamente en el flujo inicial
            self.ui.agregar_mensaje_bot("BotICO: Como eres de Nuevo Ingreso, aquí tienes el acceso a tu proceso:")
            self.ui.agregar_boton_en_chat(
                texto_boton="📄 Ver Requisitos de Convocatoria 2026-1",
                comando=self.mostrar_requisitos_pdf
            )
            
            # 4. Indicación final y botones inferiores
            self.ui.agregar_mensaje_bot("📌 Elige una opción o escribe tu duda:")
            self.ui.actualizar_botones(MenuSystem.get_botones_nuevo_ingreso())
        else:
            # ALUMNO REGULAR: botones generales
            self.ui.agregar_mensaje_bot(MenuSystem.mensaje_bienvenida_regular(self.nombre_usuario))
            self.ui.actualizar_botones(MenuSystem.get_botones_principales())
    
    def procesar_mensaje(self, mensaje):
        """Procesa mensajes del usuario (texto o comando de botón)"""
        self.ui.agregar_mensaje_usuario(mensaje)
        
        texto_limpio = limpiar_texto(mensaje)
        if texto_limpio in ["salir", "adios", "exit", "chao"]:
            self.ui.agregar_mensaje_bot("👋 ¡Gracias por usar BotICO! Hasta pronto.")
            self.ventana.after(1500, self.ventana.quit)
            return
        
        if texto_limpio in ["menu", "menú", "ayuda", "opciones"]:
            if self.es_nuevo_ingreso:
                self.ui.agregar_mensaje_bot("📋 Opciones: Convocatoria, Horarios, Contactos, Preguntas Frecuentes")
            else:
                self.ui.agregar_mensaje_bot("📋 Opciones: Inscripciones, Horarios, Trámites, Contactos, Actividades")
            return
        
        categoria = self.evaluar_categoria(mensaje)
        
        # Interceptación para meter el botón interactivo si cumple la regla
        if self.es_nuevo_ingreso and categoria in ["convocatoria", "inscripciones"]:
            self.ui.agregar_mensaje_bot("BotICO: Con base en tu estatus de Nuevo Ingreso, preparé este acceso rápido para los detalles oficiales de la Convocatoria:")
            self.ui.agregar_boton_en_chat(
                texto_boton="📄 Ver Requisitos de Convocatoria 2026-1",
                comando=self.mostrar_requisitos_pdf
            )
        else:
            respuesta = self.obtener_respuesta_por_categoria(categoria, mensaje)
            self.ui.agregar_mensaje_bot(respuesta)

    def evaluar_categoria(self, comando):
        """Determina la categoría basándose en comandos o palabras clave"""
        comandos_directos = ["inscripciones_nuevo", "co4nvocatoria", "preguntas_nuevo", "preguntas", 
                             "horarios", "contactos", "contacto", "inscripciones", "tramites", "actividades"]
        
        if comando in comandos_directos:
            if comando in ["inscripciones_nuevo", "co4nvocatoria"]: return "convocatoria"
            if comando in ["preguntas_nuevo", "preguntas"]: return "preguntas"
            if comando in ["contacto"]: return "contactos"
            return comando
            
        texto = limpiar_texto(comando)
        palabras_clave = {
            "convocatoria": ["convocatoria", "ingreso", "admisión", "examen"],
            "horarios": ["horario", "cambio", "extraordinario", "materias", "turno"],
            "contactos": ["teléfono", "correo", "dirección", "contacto", "atencion"],
            "inscripciones": ["inscripción", "inscribirme", "fechas", "documentos", "costo", "pago"],
            "tramites": ["constancia", "certificado", "titulación", "servicio social", "bajas"],
            "actividades": ["taller", "deporte", "cultural", "música", "teatro", "actividad"]
        }
        
        for categoria, palabras in palabras_clave.items():
            for palabra in palabras:
                if palabra in texto:
                    return categoria
        return "desconocido"

    def obtener_respuesta_por_categoria(self, categoria, mensaje_original):
        """Mapea las respuestas tradicionales en formato de texto ASCII"""
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

    def mostrar_requisitos_pdf(self):
        """Función callback activada al presionar el botón incrustado en el chat"""
        requisitos_texto = (
            "\n📋 --- REQUISITOS ESENCIALES CONVOCATORIA 2026-1 ---\n"
            "• Acta de nacimiento original.\n"
            "• Clave Única de Registro de Población (CURP).\n"
            "• Certificado de bachillerato con promedio superior a 7.0.\n"
            "• Cuatro fotografías tamaño infantil a blanco y negro.\n"
            "• Certificado médico expedido por la institución.\n\n"
            "🌐 ¡Redirigiendo de manera segura a la página oficial de la DGAE para consultar las bases completas!"
        )
        self.ui.agregar_mensaje_bot(requisitos_texto)
        webbrowser.open("https://www.dgae.unam.mx/convocatoria")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = BotICO()
    app.run()