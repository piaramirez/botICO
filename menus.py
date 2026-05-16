# menus.py - Sistema de menús y botones para BotICO

class MenuSystem:
    
    @staticmethod
    def get_botones_nuevo_ingreso():
        """Botones específicos para nuevo ingreso"""
        return [
            ("📋 INSCRIPCIÓN", "inscripciones_nuevo"),
            ("❓ PREGUNTAS FRECUENTES", "preguntas_nuevo"),
            ("🕒 HORARIOS", "horarios"),
            ("📞 CONTACTO", "contactos")
        ]
    
    @staticmethod
    def get_botones_principales():
        """Botones generales para alumnos regulares"""
        return [
            ("📌 Inscripciones", "inscripciones"),
            ("🕒 Horarios", "horarios"),
            ("📄 Trámites", "tramites"),
            ("📞 Contacto", "contactos"),
            ("🎭 Actividades", "actividades")
        ]
    
    @staticmethod
    def mensaje_bienvenida_nuevo(nombre):
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
        return f"""
╔══════════════════════════════════════════════════════════════════╗
║           📚 ¡BIENVENIDO DE VUELTA, {nombre.upper()}! 📚           ║
╠══════════════════════════════════════════════════════════════════╣
║  ¿En qué puedo ayudarte hoy?                                     ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def mensaje_fechas_inscripcion():
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
║     • Carta Compromiso (llena y firmada).                        ║
║     • Comprobante de aportación voluntaria de banco o cajas:     ║
║       (Cajas plantel: $0.50 centavos / Banco: Mínimo $100.00).   ║
║     • Clave CURP impresa.                                        ║
║     • Original y copia de tu identificación oficial vigente con  ║
║       fotografía y firma por AMBOS LADOS (INE, Pasaporte,        ║
║       Licencia o Credencial de bachillerato).                    ║
║                                                                  ║
║  🪪 RECOLECCIÓN DE PAPELES:                                      ║
║     Al entregar tus documentos en ventanilla, recibirás tu       ║
║     comprobante de inscripción oficial y tu credencial UNAM      ║
║     física (si no hubiese llegado, se te avisará la fecha).       ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def mensaje_tramites():
        return """
╔══════════════════════════════════════════════════════════════════╗
║                 📄 TRÁMITES ESCOLARES - ICO                      ║
╠══════════════════════════════════════════════════════════════════╗
║  📄 CONSTANCIAS: Servicios Escolares                             ║
║  🎓 CERTIFICADO: Control Escolar                                 ║
║  📜 TITULACIÓN: Tesis o reporte profesional                      ║
║                                                                  ║
║  🤝 SERVICIO SOCIAL:                                             ║
║     https://www.fes-aragon.unam.mx/servicio-social               ║
║                                                                  ║
║  📧 escolares@fes-aragon.unam.mx                                 ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def mensaje_actividades():
        return """
╔══════════════════════════════════════════════════════════════════╗
║        🎭 TALLERES CULTURALES Y EXTENSIÓN UNIVERSITARIA          ║
╠══════════════════════════════════════════════════════════════════╣
║ 🏛️ CENTRO DE LENGUAS (CLE):                                       ║
║    Cursos oficiales de Inglés, Francés, Alemán, Italiano y       ║
║    Certificaciones de comprensión de lectura.                    ║
║                                                                  ║
║ 🎵 TALLERES CULTURALES ACTIVOS:                                  ║
║    Clases de música (guitarra, piano), teatro, danza             ║
║    contemporánea, fotografía y artes plásticas.                  ║
║                                                                  ║
║ ⚽ ACTIVIDADES DEPORTIVAS:                                       ║
║    Inscripción a las 21 disciplinas de recreación, uso de        ║
║    pista de atletismo, canchas de fútbol rápido y gimnasio.      ║
║                                                                  ║
║ 👉 Escribe 'Deportes' para ver los costos o requisitos oficiales║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def mensaje_no_entendido():
        return "❓ No entendí tu pregunta. Puedes escribir 'menú' para ver las opciones disponibles o reformular tu duda."

    # ========== COMPONENTES DE PREGUNTAS FRECUENTES (CATÁLOGO COMPLETO) ==========
    @staticmethod
    def faq_reinscripcion_texto():
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
        return """
📄 GUÍA DE TRÁMITE DE CONSTANCIAS Y TIRAS

• REPOSICIÓN DE TIRA DE MATERIAS (Comprobante de Inscripción):
  - 1er Ingreso: Solicítala en tu ventanilla de Servicios Escolares con tu identificación oficial vigente. Se expide en el momento.
  - Alumnos Regulares: Entra al portal de Servicios Escolares > Alumnos > Trámites Escolares. Elige 'Comprobantes de Reinscripción' y dale clic al icono de la impresora.

• CONSTANCIA DE ESTUDIOS (Indica turno, materias y periodo lectivo):
  - Requisitos: Identificación vigente, Comprobante de inscripción y recibo de pago (cuota voluntaria). Presenta documentos en ventanilla y recoge al 3er día hábil.

• CONSTANCIA DE CRÉDITOS (Muestra promedio general y avance de créditos):
  - Requisitos: ID oficial, Historial Académico reciente, recibo de pago y comprobante de inscripción. Lista al 3er día hábil en ventanilla.

• CONSTANCIA DE HISTORIAL ACADÉMICO (Sello y firma oficial):
  - Requisitos: Historial de internet, ID oficial y recibo de pago (negro cuota voluntaria / color $20 pesos). Lista al 3er día hábil.
        """

    @staticmethod
    def faq_credencial_texto():
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
        return """
🏛️ ESTUDIA EN LA FES ARAGÓN (ESTUDIANTES EXTERNOS / PRIMER INGRESO)

• INTERCAMBIO EN LA LICENCIATURA (ALUMNOS DE OTRAS UNIVERSIDADES):
  Estudiantes de otras instituciones de educación superior nacionales o extranjeras pueden realizar un intercambio académico en nuestra Facultad si su escuela tiene convenio vigente con la UNAM. Esto contempla la exención total del pago de inscripción y colegiaturas. Las solicitudes las gestiona de entrada la DGECI.

• ESTANCIAS DE INVESTIRACIÓN:
  Es posible realizar estancias de investigación especializada colaborando directamente con el personal académico de las distintas licenciaturas de la Facultad.

• COOPERACIÓN E INTERNACIONALIZACIÓN IN SITU:
  Toda la comunidad (incluyendo primer ingreso) puede participar en congresos internacionales, semanas académicas, Master Classes, Hackathones académicos y representaciones en concursos internacionales.
        """

    @staticmethod
    def faq_intercambio_contacto_texto():
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
        return """
📝 2. CONSULTA DE EXÁMENES EXTRAORDINARIOS

Módulo dedicado a revisar las fechas, horarios y sinodales asignados para la evaluación por oposición extraordinaria.

📋 INSTRUCCIONES DE USO:
• Selecciona el semestre a consultar en el combo correspondiente.
• Selecciona la vuelta de examen que deseas revisar (1ra. o 2da. vuelta de acuerdo a los plazos marcados en el calendario escolar).
• Elige tu carrera (Ingeniería en Computación) y dale clic a ENVIAR.
• Adicionalmente, el portal te permite realizar un filtrado dinámico directo por materia para localizar el aula exacta de aplicación de forma rápida.
        """

    @staticmethod
    def faq_horarios_finales_texto():
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
        return """
🔄 RECTIFICACIÓN DE ACTAS Y ACLARACIÓN DE CALIFICACIONES

Módulo diseñado para solicitar la corrección de una nota mal asentada en el historial oficial del SIAE.

📋 INSTRUCCIONES Y TIEMPOS LEGALES:
• Plazo Máximo: Cuentas estrictamente con 60 días naturales posteriores a la fecha de aplicación del examen para solicitar aclaraciones.
• Proceso: El alumno debe contactar al docente titular de la materia. Es el profesor quien genera la solicitud oficial de rectificación ante la Jefatura de Carrera y Servicios Escolares. Una vez firmada, verás reflejado el cambio en tu Historia Académica de internet.
        """

    # ========== MÉTODOS REINJECTADOS FALTANTES (REPARACIÓN COMPLETA) ==========
    @staticmethod
    def tram_cambio_carrera_sistema_texto():
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
        return """
🏥 SEGURO FACULTATIVO MÉDICO (IMSS UNAM)

Derecho de acceso gratuito a los servicios de salud clínica y hospitalaria por ser estudiante de la UNAM.

📋 PASOS PARA EL ALTA OFICIAL:
1️⃣ OBTENER TU NSS: Ingresa al portal web o App de IMSS Digital y genera tu Número de Seguridad Social de 11 dígitos.
2️⃣ REGISTRO EN FES: Entra al portal de Servicios Escolares de la FES Aragón, ve al apartado 'Seguro Médico' e introduce tu NSS.
3️⃣ CLÍNICA: Acude a la Unidad de Medicina Familiar (UMF) asignada con tu carátula impresa para darte de alta en ventanilla y recibir tu cartilla física.
        """