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
    def mensaje_horarios():
        return """
╔══════════════════════════════════════════════════════════════════╗
║                      🕒 HORARIOS - FES ARAGÓN                    ║
╠══════════════════════════════════════════════════════════════════╣
║  📅 CONSULTA DE HORARIOS:                                        ║
║     https://www.fes-aragon.unam.mx/horarios                      ║
║                                                                  ║
║  🔄 CAMBIO DE HORARIO:                                           ║
║     • Servicios Escolares                                        ║
║     • Formato con tutor                                          ║
║     • Primeras 2 semanas del semestre                            ║
║                                                                  ║
║  📚 EXÁMENES EXTRAORDINARIOS:                                    ║
║     • Convocatoria: Julio y enero                                ║
║     • Costo: $250 MXN por materia                                ║
║                                                                  ║
║  📧 escolares@fes-aragon.unam.mx                                 ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def mensaje_contactos():
        return """
╔══════════════════════════════════════════════════════════════════╗
║                   📞 CONTACTOS - FES ARAGÓN                      ║
╠══════════════════════════════════════════════════════════════════╣
║  📞 TELÉFONOS:                                                   ║
║     • Conmutador: 55 5623 0000                                   ║
║     • Servicios Escolares: 55 5623 1234                          ║
║                                                                  ║
║  📧 CORREOS:                                                     ║
║     • escolares@fes-aragon.unam.mx                               ║
║     • ico@fes-aragon.unam.mx                                     ║
║                                                                  ║
║  🌐 REDES SOCIALES:                                              ║
║     • Facebook: /FESAragonOficial                                ║
║     • Instagram: @fesaragon                                      ║
║                                                                  ║
║  📍 UBICACIÓN:                                                   ║
║     Av. Rancho Seco S/N, Nezahualcóyotl, EDOMEX                  ║
║                                                                  ║
║  🔗 https://www.fes-aragon.unam.mx/directorio                    ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def mensaje_inscripciones():
        return """
╔══════════════════════════════════════════════════════════════════╗
║                    📋 INSCRIPCIONES - ICO BLOCK                  ║
╠══════════════════════════════════════════════════════════════════╣
║  💰 COSTO: $0.50 centavos (mínimo $100 MXN)                      ║
║                                                                  ║
║  📄 DOCUMENTOS:                                                  ║
║     • Acta de nacimiento, CURP y Certificado de bachillerato      ║
║     • Comprobante de domicilio y certificado médico              ║
║                                                                  ║
║  🔗 https://www.fes-aragon.unam.mx/inscripciones                 ║
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
║              🎭 ACTIVIDADES COMPLEMENTARIAS - ICO                ║
╠══════════════════════════════════════════════════════════════════╣
║  🎵 TALLERES DISPONIBLES: Música, teatro, danza, artes plásticas ║
║  ⚽ DEPORTES: 21 disciplinas de recreación e instalaciones       ║
║  🗣️ IDIOMAS (CLE): Cursos de Inglés, Francés, Alemán, Italiano    ║
║  🤖 ROBÓTICA Y PROGRAMACIÓN: Arduino, Python, Desarrollo web     ║
║                                                                  ║
║  👉 Escribe 'Deportes' para ver el desglose de la Coordinación.  ║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def mensaje_no_entendido():
        return "❓ No entendí tu pregunta. Puedes escribir 'menú' para ver las opciones disponibles o reformular tu duda."

    # ========== COMPONENTES DE PREGUNTAS FRECUENTES (CATÁLOGO COMPLETO) ==========
    @staticmethod
    def faq_reinscripcion_texto():
        return """
🔄 PROCESO DE REINSCRIPCIÓN SEMESTRAL

Antes de iniciar el semestre, debes inscribir tus materias ordinarias en TRAMIFES.

💳 1. PAGO DE CUOTA ANUAL (Cajas del plantel o Banco):
   • SCOTIABANK  | Convenio: 0010215800-03751
   • SANTANDER   | Convenio: 65501522119 | CLABE: 014180655015221193
   • BBVA        | Cuenta: 0011035708  | CLABE: 012914002013009620
   * Nota: Es obligatorio poner tu NÚMERO DE CUENTA como referencia del depósito.

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
    def tram_extraordinarios_texto():
        return """
📝 REGISTRO DE EXÁMENES EXTRAORDINARIOS

Este proceso se realiza 2 veces por semestre en las fechas establecidas en el Calendario Escolar, con el fin de presentar la oposición para aprobar materias que no se hayan logrado en periodo ordinario.

📋 REQUISITOS Y PASOS:
• Registrar las asignaturas vía Internet en la plataforma oficial.
• El sistema se habilita a partir de las 10:00:00 hrs del primer día y cierra hasta las 23:59 hrs del último día marcado en la convocatoria.
• Recuerda realizar el pago correspondiente por materia en las cajas o banco autorizado.
        """

    @staticmethod
    def tram_suspension_texto():
        return """
🛑 SUSPENSIÓN TEMPORAL DE ESTUDIOS

La convocatoria para tramitar la suspensión temporal de estudios se publica al inicio de cada semestre.

📋 REQUISITOS Y PASOS:
• Los alumnos podrán solicitar este periodo de gracia por un semestre o un año lectivo máximo.
• El trámite se realiza directamente en las ventanillas del Departamento de Servicios Escolares dentro de las fechas establecidas en la convocatoria de inicio de ciclo.
        """

    @staticmethod
    def tram_rectificacion_texto():
        return """
🔄 RECTIFICACIÓN Y REVALIDACIÓN DE CALIFICACIONES

• RECTIFICACIÓN DE CALIFICACIONES:
  - Para solicitar el cambio de calificación en una materia en el sistema escolar es necesario estar dentro de los 60 días posteriores a la realización del examen.
  - El alumno debe contactar al profesor para que este realice la aclaración en el sistema. Posteriormente, verifica el cambio en tu Historia Académica.

• REVALIDACIÓN DE MATERIAS:
  - En caso de movilidad académica, presenta en tu Jefatura de Carrera el comprobante original de la calificación aprobatoria a revalidar.
  - Para materias optativas se entrega el Formato F306 (en Servicios Escolares). Verifica la actualización en tu Historia Académica en un lapso de 15 días.
        """

    @staticmethod
    def tram_cambio_carrera_sistema_texto():
        return """
🔀 CAMBIOS DE CARRERA, INTERNO Y DE SISTEMA

• CAMBIO INTERNO DE CARRERA:
  - Exclusivo para Relaciones Internacionales, Comunicación, Sociología e Ingenierías.
  - Requisitos: Ser alumno regular y estar dentro de los primeros 2 años de la carrera. Los de Ingenierías solo pueden optar por otra ingeniería. Solicitud en www.dgae-siae.unam.mx en fechas asignadas.

• CAMBIO DE SISTEMA (PRESENCIAL A SUAyED):
  - Disponible para Derecho, Economía y Relaciones Internacionales. Convocatoria una vez al año por la DGAE.
  - Requisitos (Art. 8): Cupo disponible, promedio mínimo de 8.5, haber aprobado de forma regular todas las materias de los 2 primeros semestres. La solicitud solo se puede presentar UNA vez y es definitiva. Trámite en www.dgae-siae.unam.mx.
        """

    @staticmethod
    def tram_anos_posteriores_texto():
        return """
🎓 INGRESO A AÑOS POSTERIORES (ACREDITACIÓN Y REVALIDACIÓN)

• POR ACREDITACIÓN (SISTEMA INCORPORADO):
  - Aspirantes con estudios de licenciatura en una institución del Sistema Incorporado de la UNAM que desean continuar su formación en alguna Facultad de la UNAM deben consultar el Manual del Alumno y el trámite "Ingreso en Años Posteriores al Primero por Acreditación".

• POR REVALIDACIÓN (OTRAS INSTITUCIONES LICENCIATURA):
  - Aspirantes de escuelas externas a la UNAM que desean continuar aquí sus estudios deben revisar detalladamente la convocatoria de la Dirección General de Incorporación y Revalidación (DGIRE).
        """

    @staticmethod
    def faq_egresados_texto():
        return """
🎓 TRÁMITES FORMALES PARA EGRESADOS

• CONSTANCIA DE CRÉDITOS: Informa el avance de créditos, materias aprobadas y promedio. Requisitos: Historial Académico reciente e impreso (máx 1 mes) y recibo de pago de cuota voluntaria.
• CONSTANCIA DE HISTORIAL ACADÉMICO: Copia sellada por Secretaría Académica. Requisitos: Historial reciente, ID oficial y recibo de pago (cuota voluntaria en negro).
• CREDENCIAL DE EGRESADO: Para quienes terminaron la carrera o están titulados. Con grandes beneficios institucionales.
        """

    @staticmethod
    def faq_egresados_documentos_pesados_texto():
        return """
📜 EXPEDICIÓN DE CERTIFICADOS Y CARTA PASANTE

• CERTIFICADO DE ESTUDIOS (Oficial FES Aragón, describe materias, notas y periodos):
  - Costo: 1er certificado aportación voluntaria. A partir del 2do cuesta $100 pesos (descarga referencia bancaria en SIGEREL: https://sigerel.dgae.unam.mx). Tiempo de entrega: 25 

días hábiles. Requisitos: Historial con datos de contacto y fotos tamaño óvalo credencial oficiales.

• CARTA PASANTE (Sirve para ejercer la carrera de forma oficial por 1 año):
  - Se puede tramitar dentro de los 11 meses posteriores al acreditar el 100% de créditos. Requisitos: Promedio mín 7.00, recibo cuota voluntaria, Historial SIAE y Carta Responsiva firmado por un responsable titulado (con copia de cédula). Recógela en ventanilla, recaba firma de DGAE en C.U. y continúa en la SEP.
        """

    @staticmethod
    def tram_permutas_texto():
        return """
🤝 TRÁMITE DE PERMUTAS Y SEGURO FACULTATIVO

• PERMUTAS (CAMBIO DE PLANTEL O CARRERA): Ambos alumnos deben ser regulares, estar inscritos en el semestre vigente y registrar la solicitud en los tiempos de la convocatoria de la DGAE al término del ciclo escolar.
• SEGURO FACULTATIVO (IMSS): Derecho al servicio médico gratuito. Obtén tu Número de Seguridad Social (NSS) en el portal de IMSS Digital e ingrésalo en el sistema de Servicios Escolares de la FES Aragón en el apartado 'Seguro Médico'.
        """

    @staticmethod
    def tram_baja_materias_texto():
        return """
📉 BAJA DE ASIGNATURAS Y BAJA DEL SEMESTRE

• BAJA DE ASIGNATURAS: La Ordinaria se procesa en línea a través del sistema TramiFES las primeras semanas del ciclo. La Extemporánea requiere causas de fuerza mayor comprobables y carta dirigida a la Jefatura de Carrera.
• BAJA DEL SEMESTRE / DEFINITIVA: La Temporal Reglamentaria se solicita en ventanilla al inicio del bloque. La Definitiva es la renuncia total a tu lugar e implica la devolución de papeles originales previa entrega de firmas de no adeudo.
        """

    # ========== COMPONENTES: EXTENSIÓN UNIVERSITARIA (DEPORTES ACTUALIZADO) ==========
    @staticmethod
    def faq_deportes_presentacion_texto():
        return """
⚽ COORDINACIÓN DE ACTIVIDADES DEPORTIVAS Y RECREATIVAS

El objetivo es ofrecer y promover una cultura deportiva y de buenos hábitos competitivos/formativos en tres ejes fundamentales:
1️⃣ Cultura física, activación y recreación.
2️⃣ Deporte competitivo.
3️⃣ Escuela del Deporte (infantil y juvenil).

📍 LUGARES DE ENTRENAMIENTO OFICIALES POR DISCIPLINA:
• Ajedrez: Lobby del teatro José Vasconcelos
• Atletismo: Pista de atletismo
• Bádminton, Basquetbol, Tenis de mesa, Voleibol sala: Gimnasio de parquet
• Beisbol: Campo de beisbol
• Futbol 7: Cancha de futbol 7
• Futbol asociación: Campo de futbol
• Futbol rápido: Cancha de futbol rápido
• Gimnasia, Porras y animación: Gimnasio multidisciplinario, salón 1
• Gimnasio de pesas, Karate do: Gimnasio de pesas y salones
• Lima Lama, Luchas asociadas: Gimnasio multidisciplinario, salón 2
• Montañismo: Áreas deportivas generales
• Rugby, Tocho bandera: Campo anexo
• Taekwondo: Gimnasio multidisciplinario

🎮 PROGRAMAS ESPECIALES DISPONIBLES:
• Diverpuma: Concepto lúdico-recreativo para integración de grupos (Agendar cita en Coordinación).
• Deporteca y Ludoteca: Préstamo de material deportivo/lúdico de lunes a viernes de 8:00 a 19:00 h en la Coordinación.
• Espacio Puma: Activación física predeportiva para relajación y compañerismo.
        """

    @staticmethod
    def faq_deportes_costos_texto():
        return """
💰 REQUISITOS, COSTOS E INSCRIPCIÓN DEPORTIVA

Para la práctica de cualquier disciplina o el uso del gimnasio de pesas es obligatorio inscribirse en línea. Las convocatorias semestrales se publican en el Facebook oficial de 'Extensión Universitaria FES Aragón'.

📋 REQUISITOS INDISPENSABLES:
1. Credencial UNAM o INE vigente.
2. Tira de materias o comprobante de inscripción del semestre actual.
3. Certificado médico original (No mayor a 3 meses de antigüedad).
4. Comprobante de seguro médico activo (IMSS, ISSSTE, etc.).
5. Comprobante de pago original de cajas.

💳 COSTOS DE APORTACIÓN SEMESTRAL:
• Comunidad Universitaria Vigente: $115.00 MXN.
• Exalumnos: $600.00 MXN.
* Nota: Los pagos se realizan físicamente en las cajas de la FES Aragón ubicadas en el edificio de la Unidad de Extensión Universitaria (Entrada de Bosques de Aragón). Horarios: Lun-Vie 10:00 a 13:00 h y 16:00 a 19:00 h.

👶 ESCUELA DEL DEPORTE (MENORES DE 6 A 17 AÑOS / COMUNIDAD EXTERNA):
• Disciplinas: Ajedrez (en línea), Básquetbol, Béisbol, Fútbol, Gimnasia, Taekwondo, Tochito y Voleibol. 
• Inscripciones: Martes y jueves de 10:00 a 13:00 h y 16:00 a 20:00 h. WhatsApp: 55 5474 4687 | Correo: deportivas.escueladeldeporte@aragon.unam.mx
        """

    @staticmethod
    def faq_deportes_instalaciones_texto():
        return """
🏛️ INFRAESTRUCTURA Y CONTACTO DE COORDINACIÓN DEPORTIVA

La FES Aragón cuenta con las siguientes instalaciones de primer nivel:
• 1 Gimnasio multidisciplinario (Salón 1, Salón 2 y área de pesas).
• 1 Gimnasio de duela (parquet) junto con vestidores, regaderas y sanitarios.
• 1 Gimnasio y barras de calistenia al aire libre.
• 6 Canchas multidisciplinarias externas (Básquet, Voleibol, Fútbol).
• 1 Cancha de voleibol de playa, 2 de fútbol rápido, 1 de fútbol 7.
• 1 Pista de atletismo, 1 Campo de béisbol, 1 Campo de fútbol asociación y 1 Campo anexo.

📞 DATOS DE CONTACTO Y ATENCIÓN:
• Responsable: Carlos Octavio Cruz Valencia
• Horarios: Lunes a viernes de 8:00 a 20:00 h | Sábados de 9:00 a 14:00 h.
• Teléfono: 55 5623 0222 (Extensión 31035)
• Correo Oficial: deportivas.contacto@aragon.unam.mx
• Actividades Externas Adultos: Entrenamiento funcional, pesas, taekwondo y karate do. Costo: $390.00 MXN mensuales (validar cupo previo por correo).
        """