# ui.py - Interfaz gráfica
import tkinter as tk
from datetime import datetime
from config import COLORS, NOMBRE_APP, INSTITUCION
from menus import MenuSystem

class UI:
    """Maneja la interfaz gráfica del chatbot"""
    
    def __init__(self, ventana, on_enviar_mensaje, es_nuevo_ingreso):
        self.ventana = ventana
        self.on_enviar_mensaje = on_enviar_mensaje
        self.es_nuevo_ingreso = es_nuevo_ingreso
        self.nombre_usuario = ""
        self.mensajes_frame = None
        self.botones_frame = None
        self.entrada = None
        self._crear_interfaz()
    
    def set_nombre_usuario(self, nombre):
        self.nombre_usuario = nombre
    
    def _crear_interfaz(self):
        """Crea la interfaz gráfica"""
        self.ventana.configure(bg=COLORS["fondo"])
        
        # Configurar grid
        self.ventana.grid_rowconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(0, weight=1)
        
        # ========== HEADER ==========
        header = tk.Frame(self.ventana, bg=COLORS["header"], height=100)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)
        
        titulo = tk.Label(header, text=f"📚 {NOMBRE_APP}", 
                         font=("Segoe UI", 22, "bold"), 
                         bg=COLORS["header"], fg=COLORS["titulo"])
        titulo.pack(pady=(15, 0))
        
        subtitulo = tk.Label(header, text=INSTITUCION, 
                            font=("Segoe UI", 10), 
                            bg=COLORS["header"], fg=COLORS["texto_bot"])
        subtitulo.pack()
        
        estado_frame = tk.Frame(header, bg=COLORS["header"])
        estado_frame.pack(pady=(5, 0))
        estado = tk.Label(estado_frame, text="🟢 En línea | Atención 24/7", 
                         font=("Segoe UI", 9), fg=COLORS["estado"], bg=COLORS["header"])
        estado.pack()
        
        # ========== ÁREA DE CHAT ==========
        chat_frame = tk.Frame(self.ventana, bg=COLORS["fondo"])
        chat_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        chat_frame.grid_rowconfigure(0, weight=1)
        chat_frame.grid_columnconfigure(0, weight=1)
        
        canvas = tk.Canvas(chat_frame, bg=COLORS["fondo"], highlightthickness=0)
        canvas.grid(row=0, column=0, sticky="nsew")
        
        scrollbar = tk.Scrollbar(chat_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        self.mensajes_frame = tk.Frame(canvas, bg=COLORS["fondo"])
        canvas.create_window((0, 0), window=self.mensajes_frame, anchor="nw")
        
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        def on_canvas_configure(event):
            canvas.itemconfig(1, width=event.width)
        
        self.mensajes_frame.bind("<Configure>", on_frame_configure)
        canvas.bind("<Configure>", on_canvas_configure)
        
        # ========== BOTONES DEL MENÚ ==========
        self.botones_frame = tk.Frame(self.ventana, bg=COLORS["fondo"])
        self.botones_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
        
        # ========== ÁREA DE ENTRADA ==========
        input_frame = tk.Frame(self.ventana, bg=COLORS["header"], height=80)
        input_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=(0, 10))
        input_frame.grid_propagate(False)
        input_frame.grid_columnconfigure(0, weight=1)
        
        self.entrada = tk.Entry(input_frame, font=("Segoe UI", 12), bg=COLORS["fondo"], 
                               fg=COLORS["texto_bot"], insertbackground=COLORS["texto_bot"],
                               relief=tk.FLAT)
        self.entrada.grid(row=0, column=0, sticky="ew", padx=(10, 5), pady=15, ipady=10)
        self.entrada.bind("<Return>", self._enviar_texto)
        
        btn_enviar = tk.Button(input_frame, text="📤 Enviar", command=self._enviar_texto,
                              bg=COLORS["boton_fondo"], fg=COLORS["boton_texto"],
                              font=("Segoe UI", 10, "bold"), relief=tk.FLAT, padx=15, pady=5)
        btn_enviar.grid(row=0, column=1, padx=(0, 5), pady=15)
    
    def _enviar_texto(self, event=None):
        """Envía texto escrito por el usuario"""
        texto = self.entrada.get().strip()
        if not texto:
            return
        self.entrada.delete(0, tk.END)
        self.on_enviar_mensaje(texto)
    
    def agregar_mensaje_bot(self, mensaje):
        """Agrega un mensaje del bot al chat"""
        self._agregar_mensaje("bot", mensaje)
    
    def agregar_mensaje_usuario(self, mensaje):
        """Agrega un mensaje del usuario al chat"""
        self._agregar_mensaje("usuario", mensaje)
    
    def _agregar_mensaje(self, emisor, mensaje):
        """Agrega un mensaje al chat"""
        frame = tk.Frame(self.mensajes_frame, bg=COLORS["fondo"])
        frame.pack(fill=tk.X, pady=8, padx=5)
        
        if emisor == "bot":
            bg = COLORS["bot_bubble"]
            fg = COLORS["texto_bot"]
            nombre = "🤖 BotICO"
            lado = tk.LEFT
            padding_extra = (0, 100)
        else:
            bg = COLORS["user_bubble"]
            fg = COLORS["texto_user"]
            nombre = f"👤 {self.nombre_usuario}"
            lado = tk.RIGHT
            padding_extra = (100, 0)
        
        bubble = tk.Frame(frame, bg=bg, relief=tk.FLAT)
        bubble.pack(side=lado, fill=tk.X, expand=True, padx=padding_extra)
        
        header = tk.Frame(bubble, bg=bg)
        header.pack(fill=tk.X, padx=12, pady=(8, 0))
        tk.Label(header, text=nombre, font=("Segoe UI", 9, "bold"), fg=fg, bg=bg).pack(side=tk.LEFT)
        tk.Label(header, text=datetime.now().strftime("%H:%M"), 
                font=("Segoe UI", 8), fg=fg, bg=bg).pack(side=tk.RIGHT)
        
        msg = tk.Label(bubble, text=mensaje, font=("Segoe UI", 10), fg=fg, bg=bg,
                      wraplength=600, justify=tk.LEFT)
        msg.pack(fill=tk.X, padx=12, pady=(5, 10))
        
        self._forzar_scroll()
        
    def agregar_boton_en_chat(self, texto_boton, comando):
        """Agrega un botón interactivo dentro del flujo del chat simulando una respuesta"""
        frame = tk.Frame(self.mensajes_frame, bg=COLORS["fondo"])
        frame.pack(fill=tk.X, pady=5, padx=5)
        
        bubble = tk.Frame(frame, bg=COLORS["bot_bubble"], relief=tk.FLAT)
        bubble.pack(side=tk.LEFT, padx=(0, 100))
        
        header = tk.Frame(bubble, bg=COLORS["bot_bubble"])
        header.pack(fill=tk.X, padx=12, pady=(6, 0))
        tk.Label(header, text="⚡ Acción disponible", font=("Segoe UI", 8, "bold"), 
                 fg=COLORS["titulo"], bg=COLORS["bot_bubble"]).pack(side=tk.LEFT)
        
        btn_interactivo = tk.Button(
            bubble, 
            text=texto_boton, 
            command=comando,
            bg=COLORS["boton_fondo"], 
            fg=COLORS["boton_texto"],
            font=("Segoe UI", 10, "bold"), 
            relief=tk.FLAT, 
            cursor="hand2",
            padx=20, 
            pady=8
        )
        btn_interactivo.pack(fill=tk.X, padx=12, pady=(5, 10))
        
        self._forzar_scroll()

    def _forzar_scroll(self):
        """Mueve la vista al último mensaje del canvas"""
        self.mensajes_frame.update_idletasks()
        for widget in self.mensajes_frame.winfo_children():
            widget.update_idletasks()
        canvas = self.mensajes_frame.master
        canvas.yview_moveto(1.0)
    
    def actualizar_botones(self, botones):
        """Actualiza los botones del menú"""
        for widget in self.botones_frame.winfo_children():
            widget.destroy()
        
        for texto, comando in botones:
            btn = tk.Button(self.botones_frame, text=texto, 
                          command=lambda c=comando: self.on_enviar_mensaje(c),
                          bg=COLORS["boton_fondo"], fg=COLORS["boton_texto"],
                          font=("Segoe UI", 10, "bold"), relief=tk.FLAT, 
                          padx=15, pady=8)
            btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)