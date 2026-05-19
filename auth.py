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
================================================================
*NOTA IMPORTANTE:* 
El proyecto utiliza un sistema de matching por palabras clave 
implementado manualmente (NLP básico) que no requiere librerías 
externas adicionales como thefuzz o python-Levenshtein como 
se había considerado inicialmente.
"""

import tkinter as tk
from config import COLORS


class AuthManager:
    """
    Clase que maneja el registro y autenticación de usuarios.
    
    Esta clase crea una ventana modal para solicitar el nombre del usuario
    y su tipo (nuevo ingreso o alumno regular), validando los datos antes
    de continuar.
    
    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación
        on_registro_completo (callable): Función callback ejecutada al registrar
        nombre_usuario (str): Nombre del usuario registrado
        es_nuevo (bool): True si es nuevo ingreso, False si es regular
    """
    
    def __init__(self, ventana, on_registro_completo):
        """
        Inicializa el manejador de autenticación.
        
        Args:
            ventana (tk.Tk): Ventana principal de la aplicación
            on_registro_completo (callable): Función a llamar cuando el registro 
                                             se complete exitosamente.
                                             Recibe (nombre_usuario, es_nuevo)
        """
        self.ventana = ventana
        self.on_registro_completo = on_registro_completo
        self.nombre_usuario = ""  # Se llenará después del registro
        self.es_nuevo = None      # Se llenará después del registro
    
    def solicitar_registro(self):
        """
        Crea y muestra una ventana modal para solicitar registro del usuario.
        
        Esta ventana permite al usuario ingresar su nombre y seleccionar
        si es de nuevo ingreso o alumno regular. Valida que ambos campos
        estén correctamente llenados antes de continuar.
        
        La ventana incluye:
        - Título del sistema (FES Aragón - ICO / BotICO)
        - Campo de entrada para el nombre
        - Radio buttons para tipo de alumno (Nuevo Ingreso / Regular)
        - Botón para comenzar
        - Mensajes de error en caso de validación fallida
        
        La ventana es modal (bloquea la ventana principal), no redimensionable
        y se centra automáticamente en la pantalla.
        """
        # Crear ventana modal
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Bienvenido a BotICO")
        ventana_registro.geometry("500x450")
        ventana_registro.configure(bg=COLORS["fondo"])
        ventana_registro.transient(self.ventana)  # Modal respecto a la ventana padre
        ventana_registro.grab_set()               # Bloquear interacción con ventana padre
        ventana_registro.resizable(False, False)  # No redimensionable
        
        # ========== CENTRAR VENTANA EN PANTALLA ==========
        ventana_registro.update_idletasks()  # Actualizar geometría
        x = (ventana_registro.winfo_screenwidth() // 2) - (500 // 2)
        y = (ventana_registro.winfo_screenheight() // 2) - (450 // 2)
        ventana_registro.geometry(f"+{x}+{y}")
        
        # ========== ENCABEZADO / TÍTULOS ==========
        # Título de la escuela
        tk.Label(
            ventana_registro, 
            text="📚 FES Aragón - ICO", 
            font=("Segoe UI", 14, "bold"), 
            bg=COLORS["fondo"], 
            fg=COLORS["titulo"]
        ).pack(pady=15)
        
        # Título del bot
        tk.Label(
            ventana_registro, 
            text="BotICO", 
            font=("Segoe UI", 24, "bold"), 
            bg=COLORS["fondo"], 
            fg=COLORS["texto_bot"]
        ).pack()
        
        # Mensaje de bienvenida / instrucción
        tk.Label(
            ventana_registro, 
            text="\n🔐 Para comenzar, necesito saber tu nombre:", 
            font=("Segoe UI", 11), 
            bg=COLORS["fondo"], 
            fg=COLORS["texto_bot"]
        ).pack(pady=15)
        
        # ========== CAMPO DE NOMBRE ==========
        entry_nombre = tk.Entry(
            ventana_registro, 
            font=("Segoe UI", 14), 
            bg=COLORS["header"], 
            fg=COLORS["texto_bot"], 
            relief=tk.FLAT,          # Sin borde 3D
            justify=tk.CENTER        # Texto centrado
        )
        entry_nombre.pack(pady=10, padx=40, fill=tk.X)
        entry_nombre.focus()  # Enfocar automáticamente el campo
        
        # ========== ETIQUETA PARA MENSAJES DE ERROR ==========
        error_label = tk.Label(
            ventana_registro, 
            text="", 
            font=("Segoe UI", 9), 
            fg="#f72585",  # Color rosado para errores
            bg=COLORS["fondo"]
        )
        error_label.pack()
        
        # ========== TIPO DE ALUMNO (RADIO BUTTONS) ==========
        tipo_frame = tk.Frame(ventana_registro, bg=COLORS["fondo"])
        tipo_frame.pack(pady=15)
        
        tk.Label(
            tipo_frame, 
            text="¿Cuál es tu situación actual?", 
            font=("Segoe UI", 11), 
            bg=COLORS["fondo"], 
            fg=COLORS["texto_bot"]
        ).pack(pady=5)
        
        # Variable que almacenará la selección del usuario
        tipo_var = tk.StringVar(value="")
        
        # Radio button para NUEVO INGRESO
        rb_nuevo = tk.Radiobutton(
            tipo_frame, 
            text="🆕 NUEVO INGRESO (voy a entrar por primera vez)",
            variable=tipo_var, 
            value="nuevo",
            bg=COLORS["fondo"], 
            fg=COLORS["texto_bot"],
            selectcolor=COLORS["header"],  # Color cuando está seleccionado
            font=("Segoe UI", 10)
        )
        rb_nuevo.pack(anchor=tk.W, padx=20, pady=5)  # anchor=W alinea a la izquierda
        
        # Radio button para ALUMNO REGULAR
        rb_regular = tk.Radiobutton(
            tipo_frame, 
            text="✅ ALUMNO REGULAR (estoy inscrito actualmente)",
            variable=tipo_var, 
            value="regular",
            bg=COLORS["fondo"], 
            fg=COLORS["texto_bot"],
            selectcolor=COLORS["header"],
            font=("Segoe UI", 10)
        )
        rb_regular.pack(anchor=tk.W, padx=20, pady=5)
        
        # ========== FUNCIÓN INTERNA PARA GUARDAR Y VALIDAR ==========
        def guardar():
            """
            Valida los datos ingresados y completa el registro.
            
            Validaciones:
            1. El nombre no puede estar vacío y debe tener al menos 2 caracteres
            2. Debe seleccionarse un tipo de alumno (nuevo o regular)
            
            Si la validación es exitosa:
            - Almacena el nombre y tipo en los atributos de la instancia
            - Destruye la ventana de registro
            - Ejecuta el callback on_registro_completo con los datos
            
            Si la validación falla:
            - Muestra un mensaje de error específico en error_label
            """
            nombre = entry_nombre.get().strip()  # Obtener nombre y limpiar espacios
            tipo = tipo_var.get()                # Obtener tipo seleccionado
            
            # Validación: nombre válido (no vacío y mínimo 2 caracteres)
            if not nombre or len(nombre) < 2:
                error_label.config(text="⚠️ Ingresa un nombre válido (mínimo 2 caracteres)")
                return
            
            # Validación: tipo seleccionado
            if not tipo:
                error_label.config(text="⚠️ Selecciona si eres NUEVO INGRESO o ALUMNO REGULAR")
                return
            
            # Guardar datos del usuario
            self.nombre_usuario = nombre
            self.es_nuevo = (tipo == "nuevo")  # True si "nuevo", False si "regular"
            
            # Cerrar ventana de registro
            ventana_registro.destroy()
            
            # Llamar al callback con los datos del usuario
            self.on_registro_completo(self.nombre_usuario, self.es_nuevo)
        
        # ========== BOTÓN DE COMENZAR ==========
        btn = tk.Button(
            ventana_registro, 
            text="🎓 COMENZAR", 
            command=guardar,
            bg=COLORS["boton_fondo"], 
            fg=COLORS["boton_texto"],
            font=("Segoe UI", 12, "bold"), 
            relief=tk.FLAT,  # Botón plano
            padx=30, 
            pady=10
        )
        btn.pack(pady=15)
        
        # ========== EVENTO TECLADO ==========
        # Permite presionar "Enter" en el campo de nombre para ejecutar guardar()
        entry_nombre.bind("<Return>", lambda e: guardar())