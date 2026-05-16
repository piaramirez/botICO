# auth.py - Registro de usuario (nombre + tipo de alumno)
import tkinter as tk
from config import COLORS

class AuthManager:
    """Maneja el registro de usuarios"""
    
    def __init__(self, ventana, on_registro_completo):
        self.ventana = ventana
        self.on_registro_completo = on_registro_completo
        self.nombre_usuario = ""
        self.es_nuevo = None
    
    def solicitar_registro(self):
        """Ventana modal para solicitar nombre y tipo de alumno"""
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Bienvenido a BotICO")
        ventana_registro.geometry("500x450")
        ventana_registro.configure(bg=COLORS["fondo"])
        ventana_registro.transient(self.ventana)
        ventana_registro.grab_set()
        ventana_registro.resizable(False, False)
        
        # Centrar ventana
        ventana_registro.update_idletasks()
        x = (ventana_registro.winfo_screenwidth() // 2) - (500 // 2)
        y = (ventana_registro.winfo_screenheight() // 2) - (450 // 2)
        ventana_registro.geometry(f"+{x}+{y}")
        
        # Título
        tk.Label(ventana_registro, text="📚 FES Aragón - ICO", 
                font=("Segoe UI", 14, "bold"), bg=COLORS["fondo"], fg=COLORS["titulo"]).pack(pady=15)
        tk.Label(ventana_registro, text="BotICO", 
                font=("Segoe UI", 24, "bold"), bg=COLORS["fondo"], fg=COLORS["texto_bot"]).pack()
        
        tk.Label(ventana_registro, text="\n🔐 Para comenzar, necesito saber tu nombre:", 
                font=("Segoe UI", 11), bg=COLORS["fondo"], fg=COLORS["texto_bot"]).pack(pady=15)
        
        # Campo de nombre
        entry_nombre = tk.Entry(ventana_registro, font=("Segoe UI", 14), bg=COLORS["header"], 
                                fg=COLORS["texto_bot"], relief=tk.FLAT, justify=tk.CENTER)
        entry_nombre.pack(pady=10, padx=40, fill=tk.X)
        entry_nombre.focus()
        
        # Label de error
        error_label = tk.Label(ventana_registro, text="", font=("Segoe UI", 9), 
                               fg="#f72585", bg=COLORS["fondo"])
        error_label.pack()
        
        # Tipo de alumno
        tipo_frame = tk.Frame(ventana_registro, bg=COLORS["fondo"])
        tipo_frame.pack(pady=15)
        
        tk.Label(tipo_frame, text="¿Cuál es tu situación actual?", 
                font=("Segoe UI", 11), bg=COLORS["fondo"], fg=COLORS["texto_bot"]).pack(pady=5)
        
        tipo_var = tk.StringVar(value="")
        
        rb_nuevo = tk.Radiobutton(tipo_frame, text="🆕 NUEVO INGRESO (voy a entrar por primera vez)",
                                  variable=tipo_var, value="nuevo",
                                  bg=COLORS["fondo"], fg=COLORS["texto_bot"],
                                  selectcolor=COLORS["header"], font=("Segoe UI", 10))
        rb_nuevo.pack(anchor=tk.W, padx=20, pady=5)
        
        rb_regular = tk.Radiobutton(tipo_frame, text="✅ ALUMNO REGULAR (estoy inscrito actualmente)",
                                    variable=tipo_var, value="regular",
                                    bg=COLORS["fondo"], fg=COLORS["texto_bot"],
                                    selectcolor=COLORS["header"], font=("Segoe UI", 10))
        rb_regular.pack(anchor=tk.W, padx=20, pady=5)
        
        def guardar():
            nombre = entry_nombre.get().strip()
            tipo = tipo_var.get()
            
            if not nombre or len(nombre) < 2:
                error_label.config(text="⚠️ Ingresa un nombre válido (mínimo 2 caracteres)")
                return
            
            if not tipo:
                error_label.config(text="⚠️ Selecciona si eres NUEVO INGRESO o ALUMNO REGULAR")
                return
            
            self.nombre_usuario = nombre
            self.es_nuevo = (tipo == "nuevo")
            ventana_registro.destroy()
            self.on_registro_completo(self.nombre_usuario, self.es_nuevo)
        
        btn = tk.Button(ventana_registro, text="🎓 COMENZAR", command=guardar,
                       bg=COLORS["boton_fondo"], fg=COLORS["boton_texto"],
                       font=("Segoe UI", 12, "bold"), relief=tk.FLAT, padx=30, pady=10)
        btn.pack(pady=15)
        entry_nombre.bind("<Return>", lambda e: guardar())