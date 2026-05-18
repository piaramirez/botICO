# menus.py - Sistema de menús, componentes de texto y FAQs para BotICO
"""
Módulo de Configuración de Contenido y Menús Escolares (BotICO).

Este módulo centraliza todas las estructuras de botones del sistema, mensajes 
de bienvenida y el catálogo unificado de preguntas frecuentes (FAQs) utilizando
métodos estáticos para su consumo dinámico desde el core principal.
"""

class MenuSystem:
    
    @staticmethod
    def get_botones_nuevo_ingreso():
        """
        Retorna la colección de botones interactivos para el perfil de primer ingreso.
        
        Returns:
            list[tuple[str, str]]: Pares de (Texto del Botón, Identificador de Comando).
        """
        return [
            ("📋 INSCRIPCIÓN", "inscripciones_nuevo"),
            ("❓ PREGUNTAS FRECUENTES", "preguntas_nuevo"),
            ("🕒 HORARIOS", "horarios"),
            ("📞 CONTACTO", "contactos")
        ]
    
    @staticmethod
    def get_botones_principales():
        """
        Retorna la colección de botones interactivos para el perfil de alumnos regulares.
        
        Returns:
            list[tuple[str, str]]: Pares de (Texto del Botón, Identificador de Comando).
        """
        return [
            ("📌 Inscripciones", "inscripciones"),
            ("🕒 Horarios", "horarios"),
            ("📄 Trámites", "tramites"),
            ("📞 Contacto", "contactos"),
            ("🎭 Actividades", "actividades")
        ]

    @staticmethod
    def get_botones_tramites():
        """
        Retorna los botones interactivos que se despliegan al presionar 'Trámites'.
        """
        return [
            ("1. Registro de Modalidad de Titulación", "tramite_registro_titulacion"),
            ("2. Requisitos Toma de Protesta y Fotos", "tramite_protesta_diplomados"),
            ("🌐 Sitio Oficial de Titulación FES", "tramite_web_titulacion")
        ]
    
    @staticmethod
    def mensaje_bienvenida_nuevo(nombre):
        """Genera la tarjeta de bienvenida para usuarios de nuevo ingreso."""
        return f"""
╔══════════════════════════════════════════════════════════════════╗
║     🎓 ¡BIENVENIDO A LA FES ARAGÓN - ICO, {nombre.upper()}! 🎓      ║
╠══════════════════════════════════════════════════════════════════╣
║  Te damos la más cordial bienvenida a Ingeniería en Computación. ║
║  Estoy aquí para guiarte en TODO tu proceso de ingreso.          ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def mensaje_bienvenida_regular(nombre):
        """Genera la tarjeta de bienvenida para alumnos inscritos regulares."""
        return f"""
╔══════════════════════════════════════════════════════════════════╗
║           📚 ¡BIENVENIDO DE VUELTA, {nombre.upper()}! 📚           ║
╠══════════════════════════════════════════════════════════════════╣
║  ¿En qué puedo ayudarte hoy?                                     ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def mensaje_fechas_inscripcion():
        """Retorna el cronograma síncrono del periodo lectivo vigente."""
        return """
╔══════════════════════════════════════════════════════════════════╗
║                    📅 FECHAS DE INSCRIPCIÓN - ICO                ║
╠══════════════════════════════════════════════════════════════════╣
║  🗓️ SEMESTRE 2026-2:                                             ║
║     • Registro en línea: 20 - 25 de enero                        ║
║     • Inicio de clases: 3 de febrero 2026                        ║
║     • Altas y bajas: 4, 5 y 6 de febrero 2026                    ║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def mensaje_convocatoria():
        """Retorna la información legal descriptiva del concurso de selección UNAM."""
        return """
╔══════════════════════════════════════════════════════════════════╗
║                    📋 CONVOCATORIA UNAM - ICO                    ║
╠══════════════════════════════════════════════════════════════════╣
║  📅 FECHAS IMPORTANTES:                                          ║
║     • Publicación: Septiembre - octubre                          ║
║     • Registro en línea: noviembre - diciembre                   ║
║     • Examen de admisión: enero - febrero                        ║
║                                                                  ║
║  📋 REQUISITOS GENERALES:                                        ║
║     • Acta de nacimiento, CURP y Comprobante de domicilio        ║
║     • Certificado de bachillerato (Promedio mínimo 7.0)          ║
║                                                                  ║
║  👉 Selecciona tu modalidad en los botones que aparecen abajo.   ║
╚══════════════════════════════════════════════════════════════════╝
        """  

    @staticmethod
    def mensaje_contactos():
        """Retorna el directorio unificado de dependencias del plantel."""
        return """
╔══════════════════════════════════════════════════════════════════╗
║             📞 DIRECTORIO DE CONTACTOS OFICIALES                 ║
╠══════════════════════════════════════════════════════════════════╣
║ 🏛️ CONMUTADOR GENERAL FES ARAGÓN:                                 ║
║    • Teléfono: 55 5623 0000                                      ║
║                                                                  ║
║ 🏫 DEPARTAMENTO DE SERVICIOS ESCOLARES:                          ║
║    • Correo: serviciosescolares@aragon.unam.mx                   ║
║    • Correo Alterno: escolares@fes-aragon.unam.mx                ║
║                                                                  ║
║ 🎓 JEFATURA DE INGENIERÍA EN COMPUTACIÓN (ICO):                  ║
║    • Correo: ico@fes-aragon.unam.mx                              ║
║                                                                  ║
║ ⚽ COORDINACIÓN DE ACTIVIDADES DEPORTIVAS:                        ║
║    • Responsable: Carlos Octavio Cruz Valencia                   ║
║    • Teléfono: 55 5623 0222 (Extensión: 31035)                   ║
║    • Correo: deportivas.contacto@aragon.unam.mx                  ║
║    • Escuela del Deporte: deportivas.escueladeldeporte@aragon.     ║
║      unam.mx | WhatsApp: 55 5474 4687                            ║
║    • Horarios: Lun-Vie 8:00 a 20:00 h | Sáb 9:00 a 14:00 h       ║
║                                                                  ║
║ ✈️ OFICINA DE INTERCAMBIO ACADÉMICO Y VINCULACIÓN:                ║
║    • Correo: intercambioacademico@aragon.unam.mx                 ║
║    • Ubicación: CISE, Planta Baja del Edificio A1                ║
║    • Horarios: Lun-Vie 9:00 a 13:30 h y 16:00 a 20:00 h          ║
║                                                                  ║
║ 🔗 CENTRO DE LENGUAS (CLE) - IDIOMAS:                            ║
║    • Coordinación de Idiomas: cle.aragon@unam.mx                 ║
║                                                                  ║
║ 📍 UBICACIÓN PLANTEL: Av. Rancho Seco S/N, Plazas de Aragón,     ║
║    Nezahualcóyotl, Estado de México.                             ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def mensaje_inscripciones():
        """Retorna el flujo detallado con requisitos físicos para la ventanilla de Servicios Escolares."""
        return """
╔══════════════════════════════════════════════════════════════════╗
║             📋 PROCESO DE INSCRIPCIÓN PRIMER INGRESO             ║
╠══════════════════════════════════════════════════════════════════╣
║  🏢 VENTANILLA DE SERVICIOS ESCOLARES:                            ║
║     Debes presentarte físicamente en la FES Aragón siguiendo la   ║
║     agenda de fechas y horarios establecidos según tu carrera.   ║
║                                                                  ║
║  📄 DOCUMENTACIÓN OBLIGATORIA A ENTREGAR:                        ║
║     • Carta de asignación firmada (marcada como PLANTEL).        ║
║     • Carta Compromiso (disponible en la página del PIIANITE).   ║
║     • Comprobante de aportación voluntaria de banco o cajas.     ║
║     • Clave CURP impresa.                                        ║
║     • Original y copia de tu identificación oficial vigente con  ║
║       fotografía y firma por AMBOS LADOS (INE, Pasaporte,        ║
║       Licencia o Credencial de bachillerato).                    ║
║                                                                  ║
║  🪪 RECOLECCIÓN DE PAPELES:                                      ║
║     Al entregar tus documentos en ventanilla, recibirás tu       ║
║     comprobante de inscripción oficial y tu credencial UNAM.     ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def mensaje_tramites():
        """Retorna la invitación para seleccionar un trámite específico mediante botones."""
        return """
╔══════════════════════════════════════════════════════════════════╗
║                 📄 TRÁMITES ESCOLARES Y TITULACIÓN               ║
╠══════════════════════════════════════════════════════════════════╣
║  Aquí puedes consultar la información sobre tu proceso           ║
║  de titulación y egreso en la FES Aragón.                        ║
║                                                                  ║
║  👇 Por favor, selecciona una opción en los botones de abajo     ║
║     para conocer los detalles y requisitos de tu trámite.        ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def tramite_registro_titulacion_texto():
        """Retorna los pasos para el Registro de Modalidad de Titulación."""
        return """
╔══════════════════════════════════════════════════════════════════╗
║             📝 REGISTRO DE MODALIDAD DE TITULACIÓN               ║
╠══════════════════════════════════════════════════════════════════╣
║  1️⃣ Acude a tu jefatura de carrera y llena la solicitud de       ║
║     modalidad de titulación.                                     ║
║                                                                  ║
║  2️⃣ Solicita en Secretaría Académica tu registro de tesis o     ║
║     modalidad de titulación, presentando la solicitud de         ║
║     autorización previa.                                         ║
║                                                                  ║
║  3️⃣ Después de 20 días hábiles (a partir de la solicitud),       ║
║     recibirás en Secretaría Académica el oficio de aceptación    ║
║     del registro suscrito por el director del plantel.           ║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def tramite_protesta_diplomados_texto():
        """Retorna los Requisitos para la Toma de Protesta (Diplomados) y especificaciones fotográficas."""
        return """
╔══════════════════════════════════════════════════════════════════╗
║         📜 REQUISITOS TOMA DE PROTESTA Y EMISIÓN                 ║
╠══════════════════════════════════════════════════════════════════╣
║  • Pago de título (Se realiza directamente en la DGAE).          ║
║  • Solicitud de título y Oficio de autorización reciente.        ║
║  • Comprobante y pago de revisión de estudios (sellado en caja). ║
║  • Carta de no adeudo de libros (Biblioteca Central UNAM).       ║
║  • Formato para expedición de cédula profesional (SIREP).       ║
║  • Cuestionario de opinión de egresados (Contestar en DGAE).     ║
║  • Formato de trámite de titulación.                             ║
║                                                                  ║
║  📌 Nota: Anota con lápiz tu nombre completo en un papel e       ║
║     inclúyelo en una bolsa de plástico transparente (sin el      ║
║     nombre o logotipo del estudio fotográfico).                  ║
╠══════════════════════════════════════════════════════════════════╣
║                  📸 CARACTERÍSTICAS DE LAS FOTOS                 ║
╠══════════════════════════════════════════════════════════════════╣
║  👩 Mujeres: Vestimenta formal sin escote, maquillaje discreto,   ║
║     frente y orejas descubiertas, aretes pequeños, sin lentes    ║
║     obscuros o pupilentes de color.                              ║
║                                                                  ║
║  👨 Hombres: Saco y corbata, cabello corto, frente y orejas      ║
║     descubiertas, barba y bigote recortados (deben verse los     ║
║     labios), sin lentes obscuros o pupilentes de color.          ║
║                                                                  ║
║  📜 Opción Pergamino: Siete fotos tamaño título (6 x 9 cm), en   ║
║     blanco y negro, con fondo gris claro, uniforme sin manchas,  ║
║     recientes, con retoque, impresas en papel mate (no instan-   ║
║     táneas o digitales), debidamente recortadas, rostro serio,   ║
║     el tamaño de la cara medirá 3.5 cm de oreja a oreja por      ║
║     5 cm del pelo al mentón.                                     ║
║                                                                  ║
║  📄 Opción Papel Bond: Siete fotos tamaño diploma (5 x 7 cm),    ║
║     blanco y negro, cara proporcionada al tamaño de la foto;     ║
║     y cuatro tamaño infantil (30 x 25 mm), fondo blanco con      ║
║     retoque (tiene un costo de $1.00 peso y se paga en DGAE).    ║
╠══════════════════════════════════════════════════════════════════╣
║               📊 CONSULTA DE AVANCE DE EMISIÓN                   ║
╠══════════════════════════════════════════════════════════════════╣
║  Una vez acreditado el examen o tras haber tomado protesta,      ║
║  deberás consultar en la página web de la Dirección General de   ║
║  Administración Escolar (DGAE) el avance de tu emisión.          ║
║  🔑 Requisitos: Colocar número de cuenta y NIP (el mismo de la   ║
║     historia académica. Si no puedes ingresar, verifica que tu   ║
║     NIP no tenga más de 10 caracteres).                          ║
║                                                                  ║
║  🏢 Ubicación DGAE: A un costado del metro Ciudad Universitaria   ║
║     y del CENDI.                                                 ║
║  🕒 Horario de atención: 9:00 a 17:30 horas (horario corrido).  ║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def tramite_web_titulacion_texto():
        """Retorna los enlaces de titulación oficiales de la facultad y formularios externos."""
        return """
🌐 Portal de Titulación - Comunidad Egresada FES Aragón:
https://aragon.unam.mx/comunidad-egresada/content/titulacion/

📋 Enlace al Formulario de Registro Solicitado (Microsoft Forms):
https://forms.office.com/pages/responsepage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAN__mF8m8FUQzZJTjdUTVdMUFA5VDQyVTZLWVRDVTRCNS4u
        """
    
    @staticmethod
    def mensaje_no_entendido():
        """Mensaje de excepción por defecto ante fallas del motor de parseo semántico."""
        return "❓ No entendí tu pregunta. Puedes escribir 'menú' para ver las opciones disponibles o reformular tu duda."

    @staticmethod
    def faq_reinscripcion_texto():
        """FAQ de Reinscripción Ordinaria."""
        return """
🔄 PROCESO DE REINSCRIPCIÓN SEMESTRAL Y PAGOS

Antes de iniciar el semestre, debes inscribir tus materias ordinarias en TRAMIFES.

💳 1. MONTO DE APORTACIÓN Y VIAS DE PAGO:
   • Pago físico en cajas del plantel: $0.50 centavos.
   • Depósito en banco o transferencia: Mínimo $100.00 MXN.

🏦 CUENTAS BANCARIAS AUTORIZADAS:
   • SCOTIABANK  | Convenio: 0010215800-03751
   • SANTANDER   | Convenio: 65501522119 | CLABE: 014180655015221193
   • BBVA        | Cuenta: 0011035708  | CLABE: 012914002013009620
   * Nota importante: Es obligatorio poner tu NÚMERO DE CUENTA UNAM como referencia del depósito.

📚 2. VALIDACIÓN:
   Verifica no tener adeudos en biblioteca, Fundación UNAM o laboratorios.

💻 3. REGISTRO:
   Carga tu comprobante en TRAMIFES, consulta tu cita del sorteo e ingresa en tu fecha y hora señalada a la página de Inscripciones FES Aragón para armar tu horario y guardar tu comprobante.
        """

    @staticmethod
    def faq_constancias_texto():
        """FAQ de Constancias e Historiales Académicos."""
        return """
📄 GUÍA DE TRÁMITE DE CONSTANCIAS Y TIRAS

• REPOSICIÓN DE TIRA DE MATERIAS (Comprobante de Inscripción):
  - 1er Ingreso: Solicítala en tu ventanilla de Servicios Escolares con tu identificación oficial vigente. Se expide en el momento.
  - Alumnos Regulares: Entra al portal de Servicios Escolares > Alumnos > Trámites Escolares. Elige 'Comprobantes de Reinscripción' y dale clic al icono de la impresora.

• CONSTANCIA DE ESTUDIOS (Indica turno, materias y periodo lectivo):
  - Requisitos: Identificación vigente, Comprobante de inscripción y recibo de pago (cuota voluntaria). Presenta documentos en ventanilla y recoge al 3er día hábiles.

• CONSTANCIA DE CRÉDITOS (Muestra promedio general y avance de créditos):
  - Requisitos: ID oficial, Historial Académico reciente, recibo de pago y comprobante de inscripción. Lista al 3er día hábil en ventanilla.

• CONSTANCIA DE HISTORIAL ACADÉMICO (Sello y firma oficial):
  - Requisitos: Historial de internet, ID oficial y recibo de pago (negro cuota voluntaria / color $20 pesos). Lista al 3er día hábil.
        """

    @staticmethod
    def faq_credencial_texto():
        """FAQ de Identificaciones Físicas y Resellos Escolares."""
        return """
🪪 TRÁMITES DE CREDENCIAL UNAM Y RESELLO

• SOLICITUD DE NUEVA CREDENCIAL / REPOSICIÓN:
  1. Ingresa los días LUNES y MARTES vía Internet a la página de Servicios Escolares con tu cuenta y contraseña.
  2. Selecciona la opción 'Trámite de credencial' y sigue las instrucciones.
  3. Recoge la credencial al siguiente jueves o viernes en Servicios Escolares.

• RESELLO ANUAL DE CREDENCIAL:
  - Se realiza anualmente a partir del primer lunes concluyendo los movimientos de Altas, Bajas y Cambios de horario.
  - Preséntate en tu ventanilla correspondiente mostrando tu credencial física y tu comprobante de inscripción del semestre actual.
        """

    @staticmethod
    def faq_certificados_texto():
        """FAQ descriptiva de Certificados Parciales de Egreso."""
        return """
📜 CERTIFICADOS PARCIALES Y CARTA PASANTE

• CERTIFICADO PARCIAL DE ESTUDIOS (Avance de créditos para egresados):
  - Requisitos: Solicitud de constancia (en ventanilla de egresados), ID oficial, Historial SIAE impreso (máx. 1 semana de antigüedad) y 2 fotos óvalo-credencial (B/N o color con retoque, traje formal, orejas descubiertas).
  - Costo: 1er certificado cuota voluntaria. A partir del 2do cuesta $100.00 MXN en la DGAE (Metro C.U.).
  - Entrega: Dos semanas después en ventanilla de egresados.

• CARTA PASANTE (Sirve para ejercer la carrera de forma oficial por 1 año):
  - Requisitos: Tener mínimo el 70% de créditos, promedio mínimo de 7.00, no deber materias de 1° a 6° semestre, pago de cuota voluntaria y formato de Carta Responsiva firmado por un responsable titulado (con copia de su cédula).
  - Trámite: Entrega documentos en ventanilla. Al 3er día hábil recógela, recaba la firma en la DGAE de C.U. y continúa en la Dirección General de Profesiones de la SEP.
        """

    @staticmethod
    def faq_deportes_presentacion_texto():
        """FAQ de Estructura de Deportes e Infraestructura del Gimnasio Multidisciplinario."""
        return """
⚽ COORDINACIÓN DE ACTIVIDADES DEPORTIVAS Y RECREATIVAS

El objetivo es ofrecer y promover una cultura deportiva y de buenos hábitos en tres ejes fundamentales: Cultura física, deporte competitivo y la Escuela del Deporte.

📍 LUGARES DE ENTRENAMIENTO OFICIALES POR DISCIPLINA:
• Ajedrez: Lobby del teatro José Vasconcelos | Atletismo: Pista de atletismo
• Bádminton, Basquetbol, Tenis de mesa, Voleibol sala: Gimnasio de parquet
• Beisbol: Campo de beisbol | Futbol 7: Cancha de futbol 7
• Futbol asociación: Campo de futbol | Futbol rápido: Cancha de futbol rápido
• Gimnasia, Porras y animación: Gimnasio multidisciplinario, salón 1
• Gimnasio de pesas, Karate do: Gimnasio de pesas y salones
• Lima Lama, Luchas asociadas: Gimnasio multidisciplinario, salón 2
• Montañismo: Áreas deportivas generales | Rugby, Tocho bandera: Campo anexo
• Taekwondo: Gimnasio multidisciplinario

🎮 PROGRAMAS ESPECIALES DISPONIBLES:
• Diverpuma: Dinámicas lúdicas de integración grupal (Previa solicitud en Coordinación).
• Deporteca y Ludoteca: Préstamo de material lúdico y deportivo (Lun-Vie de 8:00 a 19:00 h).
• Espacio Puma: Actividades lúdicas y predeportivas de relajación y compañerismo.
        """

    @staticmethod
    def faq_deportes_costos_texto():
        """FAQ de Costos, Requisitos e Inscripciones del Gimnasio Puma."""
        return """
💰 REQUISITOS, COSTOS E INSCRIPCIÓN DEPORTIVA

Para la práctica de cualquier disciplina o uso del gimnasio de pesas es obligatorio inscribirse en línea en la plataforma de Extensión Universitaria semestralmente.

📋 REQUISITOS:
1. Credencial UNAM o INE vigente | 2. Tira de materias o comprobante de inscripción.
3. Certificado médico original (máx. 3 meses) | 4. Comprobante de seguro médico activo (IMSS, ISSSTE).
5. Comprobante de pago original de cajas de la FES Aragón.

💳 COSTOS DE APORTACIÓN SEMESTRAL (PAGOS EN CAJAS DE EXTENSIÓN UNIVERSITARIA):
• Comunidad Universitaria Vigente: $115.00 MXN.
• Exalumnos: $600.00 MXN.
* Horarios de caja: Lunes a viernes de 10:00 a 13:00 h y de 16:00 a 19:00 h.

👶 ESCUELA DEL DEPORTE (MENORES DE 6 A 17 AÑOS / COMUNIDAD EXTERNA):
• Disciplinas: Ajedrez (en línea), Básquetbol, Béisbol, Fútbol, Gimnasia, Taekwondo, Tochito y Voleibol. 
• Inscripciones: Martes y jueves de 10:00 a 13:00 h y de 16:00 a 20:00 h. WhatsApp: 55 5474 4687.
        """

    @staticmethod
    def faq_deportes_instalaciones_texto():
        """FAQ de Infraestructura Deportiva y Horarios de Carlos Octavio Cruz Valencia."""
        return """
🏛️ INFRAESTRUCTURA Y CONTACTO DE COORDINACIÓN DEPORTIVA

La FES Aragón cuenta con las siguientes instalaciones de primer nivel:
• 1 Gimnasio multidisciplinario (Salón 1, Salón 2 y área de pesas).
• 1 Gimnasio de duela (parquet) junto con vestidores, regaderas y sanitarios.
• 6 Canchas externas, 1 de voleibol playa, 2 de fútbol rápido, 1 de fútbol 7.
• 1 Pista de atletismo, 1 Campo de béisbol, 1 Campo de fútbol asociación y 1 Campo anexo.

📞 DATOS DE CONTACTO Y ATENCIÓN:
• Responsable: Carlos Octavio Cruz Valencia | Teléfono: 55 5623 0222 (Ext. 31035)
• Horarios: Lunes a viernes de 8:00 a 20:00 h | Sábados de 9:00 a 14:00 h.
• Correo Oficial: deportivas.contacto@aragon.unam.mx
• Actividades Externas Adultos: Entrenamiento funcional, pesas, taekwondo y karate do ($390.00 MXN mensuales). Validar cupo previo por correo.
        """

    @staticmethod
    def faq_intercambio_alumnos_texto():
        """FAQ para Movilidad Estudiantil e Intercambios Académicos (CRAI/DGECI)."""
        return """
✈️ PROGRAMAS DE MOVILIDAD PARA ALUMNOS INSCRITOS (FES ARAGÓN)

El Departamento de Intercambio Académico y Vinculación (CISE, Edificio A1, Planta Baja) gestiona programas semestrales y de corta duración con universidades nacionales e internacionales vía la DGECI, CRAI o redes de colaboración (Erasmus+, CONAHEC, Fundación Carolina, etc.).

📋 REQUISITOS GENERALES OBLIGATORIOS:
1️⃣ Ser estudiante regular.
2️⃣ Contar con al menos el 44 % de créditos al momento de la postulación.
3️⃣ Contar con promedio mínimo general de 8.5.
4️⃣ Idioma (No hispanohablantes): Mínimo 80 puntos en TOEFL iBT o 6.5 en IELTS para inglés, y nivel B2 para el resto de los idiomas.

📝 MODALIDADES DISPONIBLES:
• Movilidad semestral tradicional ordinaria (Nacional o Internacional).
• Estancias cortas: Iniciación a la investigación (Becas UNAM-DGECI) o el programa "PITAAE" (Apoyo a la Titulación por Actividades Académicas en el Extranjero).
• Colaboraciones virtuales oficiales: Cursos COIL y Clases Espejo (Emiten constancia digital oficial).
        """

    @staticmethod
    def faq_intercambio_externos_texto():
        """FAQ de Colaboraciones y Estancias de Académicos Visitantes Externos."""
        return """
🏛️ ESTUDIA EN LA FES ARAGÓN (ESTUDIANTES EXTERNOS / PRIMER INGRESO)

• INTERCAMBIO EN LA LICENCIATURA (ALUMNOS DE OTRAS UNIVERSIDADES):
  Estudiantes de otras instituciones de educación superior nacionales o extranjeras pueden realizar un intercambio académico en nuestra Facultad si su escuela tiene convenio vigente con la UNAM. Esto contempla la exención total del pago de inscripción y colegiaturas. Las solicitudes las gestiona de entrada la DGECI.

• ESTANCIAS DE INVESTIGACIÓN:
  Es posible realizar estancias de investigación especializada colaborando directamente con el personal académico de las distintas licenciaturas de la Facultad.

• COOPERACIÓN E INTERNACIONALIZACIÓN IN SITU:
  Toda la comunidad (incluyendo primer ingreso) puede participar en congresos internacionales, semanas académicas, Master Classes, Hackathones académicos y representaciones en concursos internacionales.
        """

    @staticmethod
    def faq_intercambio_contacto_texto():
        """FAQ de Ubicación y Horarios de Ventanilla del Intercambio Académico."""
        return """
📞 HORARIOS, UBICACIÓN Y CONTACTO DE INTERCAMBIO ACADÉMICO

• UBICACIÓN FÍSICA DE LA OFICINA:
  Visítanos en la oficina de Intercambio Académico ubicada dentro del CISE, en la planta baja del edificio A1.
• HORARIO DE ATENCIÓN EN VENTANILLA:
  Lunes a viernes de 9:00 a 13:30 horas y de 16:00 a 20:00 horas.
  * Nota: Se recomienda visitar semanalmente las redes oficiales, ya que las convocatorias no tienen fechas fijas de publicación.

📧 DATOS DE CONTACTO:
• Correo para Alumnos/Académicos Visitantes o Convenios Universitarios:
  intercambioacademico@aragon.unam.mx
  *(A través de este medio se coordinan reuniones de colaboración y gestiones de movilidad de personal docente nacional o extranjero).*
        """

    @staticmethod
    def faq_calificaciones_texto():
        """FAQ de Acceso Técnico al Gateway del SIAE para Calificaciones."""
        return """
📊 CONSULTA DE CALIFICACIONES E HISTORIAL ACADÉMICO (SIAE)

Para revisar tus notas parciales, actas finales asentadas, promedio general acumulado o tu avance de créditos oficiales en la UNAM, debes ingresar al portal de la Dirección General de Administración Escolar (DGAE).

💻 ACCESO AL SISTEMA:
• Plataforma Oficial: Sistema de Internet de la Administración Escolar (SIAE).
• Datos de Ingreso: Número de cuenta UNAM y tu contraseña personal del sistema.
• Contenido: Historial académico, desglose de calificaciones por ciclo lectivo, estatus de regularidad y comprobante de créditos.
        """

    @staticmethod
    def faq_horarios_detallado_texto():
        """FAQ de Interpretación de Grupos y Consulta Ordinaria de Horarios."""
        return """
🕒 1. CONSULTA DE HORARIOS DE CLASES ORDINARIOS

Para revisar las asignaturas activas del semestre en curso, los salones asignados y los docentes titulares de Ingeniería en Computación:

📋 INSTRUCCIONES DE BÚSQUEDA:
1️⃣ SELECCIONAR SEMESTRE: Indica en el combo si es semestre par o impar (Nota: el dígito 9 indica Sistema Universidad Abierta SUAyED).
2️⃣ INGRESAR GRUPO (Formado por 4 números):
    • El segundo dígito representa el semestre a consultar.
    • El tercer dígito representa el turno (0 en adelante para turno matutino, y 5 en adelante para el turno vespertino).
    • Los últimos dígitos representan el grupo específico de la carrera.
3️⃣ SELECCIONAR CARRERA: Elige Ingeniería en Computación en la lista desplegable y presiona ENVIAR.

👉 El reporte final te mostrará la distribución exacta por materia, hora, salón asignado y el nombre del docente a cargo.
        """

    @staticmethod
    def faq_horarios_extraordinarios_texto():
        """FAQ de Consulta de Exámenes Extraordinarios (Extras)."""
        return """
📝 2. CONSULTA DE EXÁMENES EXTRAORDINARIOS

Módulo dedicado a revisar las fechas, horarios y sinodales asignados para la evaluación por oposición extraordinaria.

📋 INSTRUCCIONES DE USO:
• Selecciona el semestre a consultar en el combo correspondiente.
• Selecciona la vuelta de examen que deseas revisar (1ra. o 2da. de acuerdo a los plazos marcados en el calendario escolar).
• Elige tu carrera (Ingeniería en Computación) y dale clic a ENVIAR.
• Adicionalmente, el portal te permite realizar un filtrado dinámico directo por materia para localizar el aula exacta de aplicación de forma rápida.
        """

    @staticmethod
    def faq_horarios_finales_texto():
        """FAQ de Consulta de Actas de Exámenes Finales Ordinarios."""
        return """
📜 3. CONSULTA DE EXÁMENES FINALES (ORDINARIOS)

Consulta el calendario de aplicaciones para las evaluaciones de fin de curso regular ordinario.

📋 INSTRUCCIONES DE USO:
• Selecciona el periodo semestral vigente en la lista desplegable (ej. 2026-2).
• Ingresa el grupo completo a consultar, el cual se encuentra formado estrictamente por 4 números.
• Selecciona la carrera de Ingeniería en Computación en el combo y presiona ENVIAR.

👉 Te mostrará las fechas límite, horarios y especificaciones oficiales para asentar las calificaciones de tus vueltas regulares en actas.
        """

    @staticmethod
    def faq_concepto_altas_bajas_texto():
        """FAQ Descriptiva del Periodo Reglamentario de Altas/Bajas en TramiFES."""
        return """
🔄 ¿QUÉ ES EL PERIODO DE ALTAS Y BAJAS EN LA FES ARAGÓN?

Es un proceso reglamentario posterior a la reinscripción ordinaria que permite a los alumnos regulares realizar ajustes finales a su carga académica del semestre.

📋 ¿PARA QUÉ SIRVE ESTE TRÁMITE?:
• DAR DE ALTA: Inscribir asignaturas ordinarias en los grupos que cuenten con cupos disponibles tras el cierre del sorteo principal. Es la oportunidad ideal para meter materias si te quedaste sin lugar con un profesor.
• DAR DE BAJA: Renunciar a la inscripción de una asignatura que ya habías cargado en TramiFES (Liberando el cupo para que otro compañero pueda ocuparlo).

⚠️ NOTA IMPORTANTE:
Este movimiento se realiza estrictamente en las fechas marcadas en el Calendario Oficial al inicio del bloque de clases a través de TramiFES. Recuerda que es obligatorio imprimir y guardar tu comprobante final como tu único respaldo legal de inscripción.
        """

    @staticmethod
    def tram_suspension_texto():
        """FAQ de Solicitud de Baja o Suspensión Temporal de Estudios."""
        return """
🛑 SOLICITUD DE SUSPENSIÓN TEMPORAL DE ESTUDIOS (PERIODO DE GRACIA)

Trámite oficial para pausar tus estudios de forma reglamentaria sin perder tu lugar en la UNAM.

📋 REQUISITOS Y ESPECIFICACIONES:
• Los alumnos regulares podrán solicitar la suspensión por un semestre o hasta un año lectivo máximo.
• El trámite se gestiona estrictamente las primeras semanas del ciclo escolar directo en las ventanillas del Departamento de Servicios Escolares.
• Al finalizar el periodo asignado, el reingreso se procesa de forma automática en el sistema.
        """

    @staticmethod
    def tram_rectificacion_texto():
        """FAQ de Corrección de Actas Escolares por Error de Profesor."""
        return """
🔄 RECTIFICACIÓN DE ACTAS Y ACLARACIÓN DE CALIFICACIONES

Módulo diseñado para solicitar la corrección de una nota mal asentada en el historial oficial del SIAE.

📋 INSTRUCCIONES Y TIEMPOS LEGALES:
• Plazo Máximo: Cuentas estrictamente con 60 días naturales posteriores a la fecha de aplicación del examen para solicitar aclaraciones.
• Proceso: El alumno debe contactar al docente titular de la materia. Es el profesor quien genera la solicitud oficial de rectificación ante la Jefatura de Carrera y Servicios Escolares. Una vez firmada, verás reflejado el cambio en tu Historia Académica de internet.
        """

    @staticmethod
    def tram_cambio_carrera_sistema_texto():
        """FAQ de Cambios Internos de Carrera y Cambio de Sistema (SUAyED)."""
        return """
🔀 CAMBIOS INTERNOS DE CARRERA Y DE SISTEMA (SUAyED)

Especificaciones para modificar tu estatus académico dentro de los planteles de la UNAM.

📋 1. CAMBIO INTERNO DE CARRERA (FES ARAGÓN):
   • Requisitos: Ser alumno regular (no deber materias), promedio mínimo y estar dentro de los primeros dos años del plan de estudios original. Solicitud en SIAE.

📋 2. CAMBIO DE SISTEMA (PRESENCIAL A SUAyED):
   • Requisitos (Artículo 8 del Reglamento): Cupo disponible en la modalidad a distancia, promedio general mínimo de 8.5, haber acreditado el 100% de materias de los primeros dos semestres. La solicitud es definitiva y se procesa en el portal DGAE.
        """

    @staticmethod
    def tram_permutas_texto():
        return """
🤝 TRÁMITE DE PERMUTAS ENTRE FACULTADES

Proceso para intercambiar tu lugar de inscripción con otro estudiante de la misma carrera en diferente plantel.

📋 REQUISITOS GENERALES:
• Ambos alumnos solicitantes deben mantener el estatus de Alumno Regular.
• Estar formalmente inscritos en el semestre lectivo vigente.
• Registrar la solicitud conjunta durante los plazos específicos marcados en la convocatoria de la DGAE al término del ciclo escolar.
        """

    @staticmethod
    def tram_seguro_texto():
        """FAQ Descriptiva de Incorporación al Seguro Facultativo (IMSS)."""
        return """
🏥 SEGURO FACULTATIVO MÉDICO (IMSS UNAM)

Derecho de acceso gratuito a los servicios de salud clínica y hospitalaria por ser estudiante de la UNAM.

📋 PASOS PARA EL ALTA OFICIAL:
1️⃣ OBTENER TU NSS: Ingresa al portal web o App de IMSS Digital y genera tu Número de Seguridad Social de 11 dígitos.
2️⃣ REGISTRO EN FES: Entra al portal de Servicios Escolares de la FES Aragón, ve al apartado 'Seguro Médico' e introduce tu NSS.
3️⃣ CLÍNICA: Acude a la Unidad de Medicina Familiar (UMF) asignada con tu carátula impresa para darte de alta en ventanilla y recibir tu cartilla física.
        """

    @staticmethod
    def tram_anos_posteriores_texto():
        """FAQ de Continuación de Estudios por Acreditación o Revalidación Externa."""
        return """
🎓 INGRESO A AÑOS POSTERIORES (ACREDITACIÓN Y REVALIDACIÓN)

Módulo informativo para alumnos externos o de sistemas incorporados que desean continuar estudios en UNAM.

📋 1. POR ACREDITACIÓN (SISTEMA INCORPORADO):
   • Aplica para alumnos que vienen de escuelas con plan de estudios incorporado a la UNAM. Debes presentar tu historial completo y validarlo en Servicios Escolares bajo el manual de reingreso por acreditación.

📋 2. POR REVALIDACIÓN (OTRAS UNIVERSIDADES):
   • Aplica si vienes de una universidad ajena a la UNAM (pública o privada). El trámite se gestiona directamente ante la DGIRE para determinar qué porcentaje de materias son equivalentes con Ingeniería en Computación.
        """

    @staticmethod
    def faq_egresados_texto():
        """FAQ de Constancia de Créditos y Promedio para Egresados."""
        return """
🎓 TRÁMITES ACADÉMICOS FORMALES PARA EGRESADOS

Información sobre constancias de cierre de ciclo y la obtención de identificaciones institucionales.

📋 1. CONSTANCIA DE CRÉDITOS Y PROMEDIO:
   • Documento oficial que certifica que cubriste el 100% de los créditos con tu promedio final asentado. Requisitos: Historial SIAE impreso y recibo de aportación voluntaria. Lista en 3 días hábiles.

📋 2. CREDENCIAL DE EXALUMNO UNAM:
   • Otorga acceso a las bibliotecas del campus, descuentos en talleres del CLE, actividades culturales y convenios externos. El trámite se solicita en línea a través del portal del Programa de Vinculación con Exalumnos.
        """

    @staticmethod
    def faq_egresados_documentos_pesados_texto():
        """FAQ de Emisión Oficial de Certificados y Carta Pasante."""
        return """
📜 EXPEDICIÓN DE CERTIFICADOS OFICIALES Y CARTA PASANTE

Módulo definitivo para la obtención de documentos de término de carrera con validez oficial nacional.

📋 1. CERTIFICADO COMPLETO DE ESTUDIOS:
   • Describe todas las materias, calificaciones, fechas y créditos oficiales firmados por el Director. Requisitos: Descargar la referencia bancaria en la plataforma SIGEREL ($100.00 MXN), entregar fotos óvalo credencial en ventanilla de egresados. Tiempo de entrega: 25 días hábiles.

📋 2. CARTA PASANTE:
   • Documento intermedio indispensable para ejercer la carrera de forma oficial por un año mientras realizas tu titulación. Requisitos: Haber acreditado el 100% de créditos, promedio mínimo de 7.00, Servicio Social liberado y entregar la Carta Responsiva firmada por un profesional titulado junto con copia de su cédula.
        """

    @staticmethod
    def faq_inscripcion_regulares_texto():
        """
        FAQ Unificada de Reinscripción para Alumnos Regulares.
        Incluye canales oficiales hibridos (Correo electrónico institucional y ventanilla física).
        """
        return """
╔══════════════════════════════════════════════════════════════════╗
║                🔄 REINSCRIPCIÓN ALUMNOS REGULARES                ║
╠══════════════════════════════════════════════════════════════════╣
║ 🖥️ Proceso en Línea:                                             ║
║    El trámite se realiza 100% digital a través de TramiFES       ║
║    según la cita de reinscripción asignada por tu promedio.      ║
║                                                                  ║
║ 💵 Pago de Cuota:                                                ║
║    Debes realizar tu aportación voluntaria regulada en las       ║
║    fechas asignadas (Plantel: $0.50 ctvos / Banco: Mínimo $100). ║
║                                                                  ║
║ 📬 ¿Dudas o Aclaraciones con tu Estatus de Carga?                ║
║    Si tienes problemas con tu historial, bloqueo bancario o      ║
║    asignación de materias ordinarias, escribe de inmediato a:   ║
║    📧 aragon.serviciosescolares@unam.mx                          ║
║                                                                  ║
║ 🏫 Atención Presencial Directa:                                  ║
║    O si lo prefieres, puedes acudir directamente a la            ║
║    Ventanilla de tu carrera en el edificio del CISE para        ║
║    recibir aclaraciones de forma física y personalizada.         ║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def faq_olvido_contrasena_texto():
        """FAQ de Recuperación de Contraseñas y Token Personal."""
        return """
🔐 ¿QUÉ HACER SI OLVIDASTE TU CONTRASEÑA DE ACCESO? (TRAMIFES / SIAE)

Si perdiste, bloqueaste o no recuerdas tu clave para ingresar a los portales de control escolar o inscripciones, el proceso de restablecimiento NO es automatizado por internet por cuestiones de seguridad.

🏫 SOLUCIÓN OFICIAL:
• Debes acudir directamente a las ventanillas del Departamento de Servicios Escolares situadas en el edificio del CISE.
• El horario de atención general es de lunes a viernes de 9:00 a 13:30 h y de 16:00 a 20:00 h.

📄 REQUISITOS OBLIGATORIOS PARA EL TRÁMITE:
1️⃣ Presentar original y copia de tu Identificación Oficial vigente (INE, Pasaporte) o tu Credencial Física de la UNAM.
2️⃣ Proporcionar tu Número de Cuenta de la UNAM completo.
   
*Nota: El trámite es estrictamente personal. En ventanilla validarán tus datos biométricos y de sistema para asignarte un token o clave temporal de acceso al instante.*
        """

# ========== AGREGAR ESTO AL FINAL DE TU CLASE MENUSYSTEM ==========

    @staticmethod
    def get_botones_tramites():
        """Retorna las opciones de botones interactivos para Trámites."""
        return [
            ("📜 1. Normatividad", "tramite_normatividad"),
            ("📝 2. Registro de Modalidad", "tramite_registro_titulacion"),
            ("📋 3. Requisitos de Fotos", "tramite_protesta_diplomados"),
            ("💻 4. Seguimiento DGAE", "tramite_seguimiento_dgae"),
            ("❓ 5. FAQs de Titulación", "tramite_faqs_titulacion")
        ]

    @staticmethod
    def tramite_normatividad_texto():
        return """
╔══════════════════════════════════════════════════════════════════╗
║                    ⚖️ NORMATIVIDAD DE TITULACIÓN                 ║
╠══════════════════════════════════════════════════════════════════╣
║  • Reglamento General de Exámenes                                ║
║  • Lineamientos Internos para la Titulación de la FES Aragón     ║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def tramite_registro_titulacion_texto():
        return """
╔══════════════════════════════════════════════════════════════════╗
║                    📝 REGISTRO DE MODALIDAD                      ║
╠══════════════════════════════════════════════════════════════════╣
║  1. Acude a tu jefatura de carrera y llena la solicitud.         ║
║  2. Solicita en Secretaría Académica tu registro de tesis o      ║
║     modalidad presentando la solicitud de autorización.          ║
║  3. Después de 20 días hábiles recibirás en Secretaría           ║
║     Académica el oficio de aceptación suscrito por el director.  ║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def tramite_protesta_diplomados_texto():
        return """
╔══════════════════════════════════════════════════════════════════╗
║               📋 REQUISITOS GENERALES Y FOTOS                    ║
╠══════════════════════════════════════════════════════════════════╣
║  🟢 REQUISITOS INICIALES:                                        ║
║     Certificado de Estudios | Carta de Servicio Social liberado  ║
║     Revisión de Estudios Documental Autorizada                   ║
║  🔵 REQUISITOS COMPLEMENTARIOS:                                  ║
║     Solicitud de título y referencia bancaria | No adeudo libros║
║     Autorización de transferencia de información                 ║
╠══════════════════════════════════════════════════════════════════╣
║                  📸 CARACTERÍSTICAS DE LAS FOTOS                 ║
╠══════════════════════════════════════════════════════════════════╣
║  👩 Mujeres: Ropa formal sin escote, maquillaje muy discreto,    ║
║     frente/orejas descubiertas, aretes chicos, sin lentes.       ║
║  👨 Hombres: Saco y corbata, pelo corto, frente/orejas           ║
║     descubiertas, barba/bigote recortados (verse labios).        ║
║  📌 Nota: Pon tu nombre a lápiz dentro de una bolsa transparente.║
║  📜 Pergamino: 7 fotos título (6x9 cm), B/N, fondo gris claro    ║
║     uniforme, papel mate con retoque, rostro serio.              ║
║  📄 Papel Bond: 7 fotos diploma (5x7 cm) B/N y 4 infantil ($1.00)║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def tramite_seguimiento_dgae_texto():
        return """
╔══════════════════════════════════════════════════════════════════╗
║               💻 SEGUIMIENTO DE TITULACIÓN UNIVERSITARIA         ║
╠══════════════════════════════════════════════════════════════════╣
║  Plataforma de la DGAE para gestionar tu proceso asociado:       ║
║  • Registro y aceptación de la solicitud                         ║
║  • Aprobación, desarrollo y conclusión del trabajo académico     ║
║  • Entrega electrónica y física de documentos                    ║
║  • Incorporación del Acta e integración de carpeta física        ║
║  • Entrega de carpeta física a la DGAE                           ║
║  🔑 Entra con tu Cuenta y NIP (máximo 10 caracteres).           ║
║  🕒 Horario DGAE C.U.: 9:00 a 17:30 h (junto a metro C.U.).     ║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def tramite_faqs_titulacion_texto():
        return """
╔══════════════════════════════════════════════════════════════════╗
║               ❓ PREGUNTAS FRECUENTES DE TITULACIÓN               ║
╠══════════════════════════════════════════════════════════════════╣
║ ❓ ¿Dónde pago el título?                                        ║
║ 🗣️ En la DGAE, a un costado del metro Ciudad Universitaria.      ║
║                                                                  ║
║ ❓ ¿Puedo elegir Pergamino y Papel Bond seguidos?                ║
║ 🗣️ No, solo puedes escoger una opción de título.                 ║
║                                                                  ║
║ ❓ Mi NIP marca error en el sistema de seguimiento:              ║
║ 🗣️ Valida que tu contraseña del SIAE no pase de 10 caracteres.   ║
╚══════════════════════════════════════════════════════════════════╝
        """