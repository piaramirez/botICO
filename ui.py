"""
================================================================
INTERFAZ GRÁFICA DE USUARIO - PROYECTO chatbotICO
================================================================
Fecha: 18 de mayo de 2026
Escuela: Universidad Nacional Autónoma de México (UNAM) 
         Facultad de Estudios Superiores Aragón
Grupo: 2907
Materia: Inteligencia Artificial
Docente: MARTIN ROMERO UGALDE
Estudiante: Ramírez Alcántara Pedro Antonio
            Victor Flores Felix Omar

MÓDULO DE INTERFAZ GRÁFICA DE USUARIO (UI)

DESCRIPCIÓN:
============
Este módulo maneja toda la interfaz gráfica del chatbot BotICO.
Implementa un diseño moderno de chat con burbujas de conversación,
botones interactivos y área de entrada de texto.

FUNCIONALIDADES:
================
- Ventana principal con header institucional
- Área de chat con scroll automático
- Burbujas diferenciadas (bot vs usuario)
- Botones de menú dinámicos
- Botones interactivos dentro del chat
- Campo de entrada de texto con envío por Enter
- Formato de hora en cada mensaje
- Colores institucionales UNAM
================================================================
*NOTA IMPORTANTE:* 
El proyecto utiliza un sistema de matching por palabras clave 
implementado manualmente (NLP básico) que no requiere librerías 
externas adicionales como thefuzz o python-Levenshtein como 
se había considerado inicialmente.
"""

import tkinter as tk
from datetime import datetime
from config import COLORS, NOMBRE_APP, INSTITUCION
from menus import MenuSystem


class UI:
    """
    Clase que maneja toda la interfaz gráfica del chatbot.
    
    Esta clase es responsable de:
    - Crear y configurar la ventana principal
    - Mostrar mensajes en formato de burbujas de chat
    - Manejar botones interactivos (menús y acciones)
    - Procesar entrada de texto del usuario
    - Mantener el scroll automático al último mensaje
    
    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación
        on_enviar_mensaje (callable): Función callback para procesar mensajes
        es_nuevo_ingreso (bool): True si es nuevo alumno, False si es regular
        nombre_usuario (str): Nombre del usuario actual
        mensajes_frame (tk.Frame): Contenedor de los mensajes del chat
        botones_frame (tk.Frame): Contenedor de los botones del menú
        entrada (tk.Entry): Campo de entrada de texto
    """
    
    def __init__(self, ventana, on_enviar_mensaje, es_nuevo_ingreso):
        """
        Inicializa la interfaz de usuario.
        
        Args:
            ventana (tk.Tk): Ventana principal de la aplicación
            on_enviar_mensaje (callable): Función que procesa los mensajes del usuario.
                                         Recibe el texto como argumento.
            es_nuevo_ingreso (bool): Indica si el usuario es de nuevo ingreso,
                                    afecta el contenido de los botones.
        """
        self.ventana = ventana
        self.on_enviar_mensaje = on_enviar_mensaje
        self.es_nuevo_ingreso = es_nuevo_ingreso
        self.nombre_usuario = ""          # Se establecerá después del registro
        self.mensajes_frame = None        # Contenedor de mensajes
        self.botones_frame = None         # Contenedor de botones de menú
        self.entrada = None               # Campo de texto
        
        # Crear toda la interfaz gráfica
        self._crear_interfaz()
    
    def set_nombre_usuario(self, nombre):
        """
        Establece el nombre del usuario para mostrar en los mensajes.
        
        Args:
            nombre (str): Nombre del usuario registrado
        """
        self.nombre_usuario = nombre
    
    def _crear_interfaz(self):
        """
        Crea y configura todos los componentes visuales de la interfaz.
        
        Estructura de la ventana:
        - Fila 0: Header (título, subtítulo, estado)
        - Fila 1: Área de chat (con scroll)
        - Fila 2: Botones del menú principal
        - Fila 3: Área de entrada de texto
        
        Utiliza grid layout con pesos para comportamiento responsivo.
        """
        # Configuración base de la ventana
        self.ventana.configure(bg=COLORS["fondo"])
        
        # Configurar el grid para que el chat se expanda
        self.ventana.grid_rowconfigure(1, weight=1)  # Fila del chat se expande
        self.ventana.grid_columnconfigure(0, weight=1)  # Columna única se expande
        
        # ========== HEADER (BARRA SUPERIOR) ==========
        # Contiene título de la app, institución e indicador de estado
        header = tk.Frame(self.ventana, bg=COLORS["header"], height=100)
        header.grid(row=0, column=0, sticky="ew")  # sticky="ew" = expande horizontal
        header.grid_propagate(False)  # Mantiene altura fija de 100px
        
        # Título principal de la aplicación
        titulo = tk.Label(
            header, 
            text=f"📚 {NOMBRE_APP}", 
            font=("Segoe UI", 22, "bold"), 
            bg=COLORS["header"], 
            fg=COLORS["titulo"]
        )
        titulo.pack(pady=(15, 0))
        
        # Subtítulo con nombre de la institución
        subtitulo = tk.Label(
            header, 
            text=INSTITUCION, 
            font=("Segoe UI", 10), 
            bg=COLORS["header"], 
            fg=COLORS["texto_bot"]
        )
        subtitulo.pack()
        
        # Indicador de estado (en línea)
        estado_frame = tk.Frame(header, bg=COLORS["header"])
        estado_frame.pack(pady=(5, 0))
        estado = tk.Label(
            estado_frame, 
            text="🟢 En línea | Atención 24/7", 
            font=("Segoe UI", 9), 
            fg=COLORS["estado"], 
            bg=COLORS["header"]
        )
        estado.pack()
        
        # ========== ÁREA DE CHAT CON SCROLL ==========
        # Frame contenedor del chat
        chat_frame = tk.Frame(self.ventana, bg=COLORS["fondo"])
        chat_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        chat_frame.grid_rowconfigure(0, weight=1)
        chat_frame.grid_columnconfigure(0, weight=1)
        
        # Canvas para scroll (permite desplazamiento vertical)
        canvas = tk.Canvas(chat_frame, bg=COLORS["fondo"], highlightthickness=0)
        canvas.grid(row=0, column=0, sticky="nsew")
        
        # Scrollbar vertical
        scrollbar = tk.Scrollbar(chat_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Frame interno donde se colocan los mensajes
        self.mensajes_frame = tk.Frame(canvas, bg=COLORS["fondo"])
        canvas.create_window((0, 0), window=self.mensajes_frame, anchor="nw")
        
        # Función para actualizar la región desplazable cuando cambia el tamaño
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        # Función para ajustar el ancho del canvas cuando se redimensiona
        def on_canvas_configure(event):
            canvas.itemconfig(1, width=event.width)
        
        # Vincular eventos para scroll responsivo
        self.mensajes_frame.bind("<Configure>", on_frame_configure)
        canvas.bind("<Configure>", on_canvas_configure)
        
        # ========== BOTONES DEL MENÚ PRINCIPAL ==========
        # Frame que contiene los botones de acceso rápido
        self.botones_frame = tk.Frame(self.ventana, bg=COLORS["fondo"])
        self.botones_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
        
        # ========== ÁREA DE ENTRADA DE TEXTO ==========
        # Frame para entrada de usuario (con altura fija)
        input_frame = tk.Frame(self.ventana, bg=COLORS["header"], height=80)
        input_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=(0, 10))
        input_frame.grid_propagate(False)  # Mantiene altura fija
        input_frame.grid_columnconfigure(0, weight=1)  # Campo de texto se expande
        
        # Campo de entrada de texto
        self.entrada = tk.Entry(
            input_frame, 
            font=("Segoe UI", 12), 
            bg=COLORS["fondo"], 
            fg=COLORS["texto_bot"], 
            insertbackground=COLORS["texto_bot"],  # Color del cursor
            relief=tk.FLAT  # Sin borde 3D
        )
        self.entrada.grid(row=0, column=0, sticky="ew", padx=(10, 5), pady=15, ipady=10)
        self.entrada.bind("<Return>", self._enviar_texto)  # Enter para enviar
        
        # Botón de enviar
        btn_enviar = tk.Button(
            input_frame, 
            text="📤 Enviar", 
            command=self._enviar_texto,
            bg=COLORS["boton_fondo"], 
            fg=COLORS["boton_texto"],
            font=("Segoe UI", 10, "bold"), 
            relief=tk.FLAT, 
            padx=15, 
            pady=5
        )
        btn_enviar.grid(row=0, column=1, padx=(0, 5), pady=15)
    
    def _enviar_texto(self, event=None):
        """
        Procesa y envía el texto ingresado por el usuario.
        
        Obtiene el texto del campo de entrada, lo limpia de espacios
        en blanco y lo envía al callback on_enviar_mensaje.
        
        Args:
            event (tk.Event, optional): Evento de teclado (para bind con Enter)
        """
        texto = self.entrada.get().strip()
        if not texto:  # Ignorar mensajes vacíos
            return
        
        # Limpiar campo de entrada
        self.entrada.delete(0, tk.END)
        
        # Enviar al callback principal del bot
        self.on_enviar_mensaje(texto)
    
    def agregar_mensaje_bot(self, mensaje):
        """
        Agrega un mensaje del bot al área de chat.
        
        Los mensajes del bot aparecen:
        - Alineados a la izquierda
        - Con fondo azul (COLORS["bot_bubble"])
        - Con ícono 🤖 y nombre "BotICO"
        
        Args:
            mensaje (str): Texto del mensaje a mostrar
        """
        self._agregar_mensaje("bot", mensaje)
    
    def agregar_mensaje_usuario(self, mensaje):
        """
        Agrega un mensaje del usuario al área de chat.
        
        Los mensajes del usuario aparecen:
        - Alineados a la derecha
        - Con fondo dorado (COLORS["user_bubble"])
        - Con ícono 👤 y nombre del usuario
        
        Args:
            mensaje (str): Texto del mensaje a mostrar
        """
        self._agregar_mensaje("usuario", mensaje)
    
    def _agregar_mensaje(self, emisor, mensaje):
        """
        Método interno para agregar un mensaje al chat.
        
        Crea la estructura visual de un mensaje:
        - Contenedor principal (frame)
        - Burbuja (bubble) que contiene el mensaje
        - Header con nombre del emisor y hora
        - Cuerpo del mensaje
        
        Args:
            emisor (str): "bot" o "usuario" (determina estilo y alineación)
            mensaje (str): Contenido del mensaje
        """
        # Frame contenedor del mensaje (ocupa todo el ancho)
        frame = tk.Frame(self.mensajes_frame, bg=COLORS["fondo"])
        frame.pack(fill=tk.X, pady=8, padx=5)
        
        # Configurar estilo según el emisor
        if emisor == "bot":
            bg = COLORS["bot_bubble"]      # Azul para el bot
            fg = COLORS["texto_bot"]       # Texto blanco
            nombre = "🤖 BotICO"           # Nombre del bot
            lado = tk.LEFT                 # Alinear a la izquierda
            padding_extra = (0, 100)       # Margen derecho (deja espacio)
        else:
            bg = COLORS["user_bubble"]     # Dorado para el usuario
            fg = COLORS["texto_user"]      # Texto oscuro
            nombre = f"👤 {self.nombre_usuario}"  # Nombre del usuario
            lado = tk.RIGHT                # Alinear a la derecha
            padding_extra = (100, 0)       # Margen izquierdo (deja espacio)
        
        # Burbuja del mensaje
        bubble = tk.Frame(frame, bg=bg, relief=tk.FLAT)
        bubble.pack(side=lado, fill=tk.X, expand=True, padx=padding_extra)
        
        # Header de la burbuja (nombre y hora)
        header = tk.Frame(bubble, bg=bg)
        header.pack(fill=tk.X, padx=12, pady=(8, 0))
        
        # Nombre del emisor
        tk.Label(
            header, 
            text=nombre, 
            font=("Segoe UI", 9, "bold"), 
            fg=fg, 
            bg=bg
        ).pack(side=tk.LEFT)
        
        # Hora actual (formato HH:MM)
        tk.Label(
            header, 
            text=datetime.now().strftime("%H:%M"), 
            font=("Segoe UI", 8), 
            fg=fg, 
            bg=bg
        ).pack(side=tk.RIGHT)
        
        # Cuerpo del mensaje
        msg = tk.Label(
            bubble, 
            text=mensaje, 
            font=("Segoe UI", 10), 
            fg=fg, 
            bg=bg,
            wraplength=600,      # Ajuste de línea a 600px
            justify=tk.LEFT      # Alineación izquierda
        )
        msg.pack(fill=tk.X, padx=12, pady=(5, 10))
        
        # Auto-scroll al final del chat
        self._forzar_scroll()
    
    def agregar_boton_en_chat(self, texto_boton, comando):
        """
        Agrega un botón interactivo dentro del flujo del chat.
        
        Estos botones aparecen como parte de la conversación, simulando
        una respuesta del bot con una acción disponible.
        
        Estructura visual similar a un mensaje del bot, pero con un
        botón clickeable en lugar de texto plano.
        
        Args:
            texto_boton (str): Texto que se muestra en el botón
            comando (callable): Función a ejecutar cuando se presiona el botón
        """
        # Frame contenedor (similar a un mensaje del bot)
        frame = tk.Frame(self.mensajes_frame, bg=COLORS["fondo"])
        frame.pack(fill=tk.X, pady=5, padx=5)
        
        # Burbuja con estilo de bot
        bubble = tk.Frame(frame, bg=COLORS["bot_bubble"], relief=tk.FLAT)
        bubble.pack(side=tk.LEFT, padx=(0, 100))
        
        # Header indicando acción disponible
        header = tk.Frame(bubble, bg=COLORS["bot_bubble"])
        header.pack(fill=tk.X, padx=12, pady=(6, 0))
        tk.Label(
            header, 
            text="⚡ Acción disponible", 
            font=("Segoe UI", 8, "bold"), 
            fg=COLORS["titulo"], 
            bg=COLORS["bot_bubble"]
        ).pack(side=tk.LEFT)
        
        # Botón interactivo
        btn_interactivo = tk.Button(
            bubble, 
            text=texto_boton, 
            command=comando,
            bg=COLORS["boton_fondo"], 
            fg=COLORS["boton_texto"],
            font=("Segoe UI", 10, "bold"), 
            relief=tk.FLAT, 
            cursor="hand2",      # Cambia el cursor a mano al pasar sobre el botón
            padx=20, 
            pady=8
        )
        btn_interactivo.pack(fill=tk.X, padx=12, pady=(5, 10))
        
        # Auto-scroll al final
        self._forzar_scroll()
    
    def _forzar_scroll(self):
        """
        Mueve automáticamente la vista del chat al último mensaje.
        
        Actualiza los widgets y desplaza el canvas hacia abajo
        para que el mensaje más reciente sea visible.
        """
        self.mensajes_frame.update_idletasks()
        for widget in self.mensajes_frame.winfo_children():
            widget.update_idletasks()
        
        # Obtener el canvas padre y desplazar al final
        canvas = self.mensajes_frame.master
        canvas.yview_moveto(1.0)  # 1.0 = al final (100% abajo)
    
    def actualizar_botones(self, botones):
        """
        Actualiza los botones del menú principal.
        
        Limpia todos los botones existentes y crea nuevos según
        la lista proporcionada.
        
        Args:
            botones (list[tuple[str, str]]): Lista de pares (texto, comando)
                                            donde comando es el identificador
                                            que se enviará al callback.
        """
        # Destruir todos los botones existentes
        for widget in self.botones_frame.winfo_children():
            widget.destroy()
        
        # Crear nuevos botones
        for texto, comando in botones:
            btn = tk.Button(
                self.botones_frame, 
                text=texto, 
                command=lambda c=comando: self.on_enviar_mensaje(c),  # Capturar valor actual
                bg=COLORS["boton_fondo"], 
                fg=COLORS["boton_texto"],
                font=("Segoe UI", 10, "bold"), 
                relief=tk.FLAT, 
                padx=15, 
                pady=8
            )
            btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)