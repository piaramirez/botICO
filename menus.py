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
║                    📋 INSCRIPCIONES - ICO                        ║
╠══════════════════════════════════════════════════════════════════╣
║  💰 COSTO: $0.50 centavos (mínimo $100 MXN)                      ║
║                                                                  ║
║  📄 DOCUMENTOS:                                                  ║
║     • Acta de nacimiento                                         ║
║     • CURP                                                       ║
║     • Certificado de bachillerato                                ║
║     • Comprobante de domicilio                                   ║
║     • 4 fotografías                                              ║
║     • Certificado médico                                         ║
║                                                                  ║
║  🔗 https://www.fes-aragon.unam.mx/inscripciones                 ║
╚══════════════════════════════════════════════════════════════════╝
        """
    
    @staticmethod
    def mensaje_tramites():
        return """
╔══════════════════════════════════════════════════════════════════╗
║                 📄 TRÁMITES ESCOLARES - ICO                      ║
╠══════════════════════════════════════════════════════════════════╣
║  📄 CONSTANCIAS: Servicios Escolares                             ║
║  🎓 CERTIFICADO: Control Escolar                                 ║
║  📜 TITULACIÓN:                                                  ║
║     • Tesis                                                      ║
║     • Reporte de experiencia profesional                         ║
║     • Totalidad de créditos                                      ║
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
║  🎵 TALLERES DISPONIBLES:                                        ║
║     • Música (guitarra, piano, canto)                            ║
║     • Teatro y danza                                             ║
║     • Artes plásticas                                            ║
║                                                                  ║
║  ⚽ DEPORTES:                                                    ║
║     • Fútbol, Basquetbol, Voleibol                               ║
║     • Taekwondo, Judo                                            ║
║                                                                  ║
║  🤖 ROBÓTICA Y PROGRAMACIÓN:                                     ║
║     • Arduino, Python, Desarrollo web                            ║
║                                                                  ║
║  📧 culturales@fes-aragon.unam.mx                                ║
║  🔗 https://www.fes-aragon.unam.mx/culturales                    ║
╚══════════════════════════════════════════════════════════════════╝
        """

    @staticmethod
    def mensaje_no_entendido():
        return "❓ No entendí tu pregunta. Puedes escribir 'menú' para ver las opciones disponibles o reformular tu duda."

    # ========== COMPONENTES DE PREGUNTAS FRECUENTES (CATÁLOGO EXPANDIDO) ==========
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
    def tram_cambio_turno_texto():
        return """
🔀 CAMBIOS DE TURNO Y CARRERA SIMULTÁNEA

• CAMBIO DE TURNO (PRIMER INGRESO): Acreditar estar inscrito en el semestre actual. Consultar la convocatoria 'Cambio de turno primer ingreso' y registrar la solicitud. Si es afirmativa, presentarse al grupo asignado.
• CAMBIO DE TURNO (REINGRESO): Requisito tener derecho a inscripción en el semestre. Solicitar el cambio con base en la convocatoria de reingreso y reincorporarse al turno asignado si se aprueba.
• CARRERA SIMULTÁNEA: Los alumnos que desean cursar otra carrera paralelamente deberán consultar las bases del Manual del alumno y tramitarlo en Servicios Escolares en periodos aprobados por DGAE.
        """

    @staticmethod
    def tram_permutas_texto():
        return """
🤝 TRÁMITE DE PERMUTAS (CAMBIO DE PLANTEL O CARRERA)

Este trámite permite solicitar el intercambio de adscripción entre dos alumnos de la misma carrera o plantel, o el cambio interno.

📋 REQUISITOS Y PASOS:
• Ambos alumnos deben ser regulares y estar formalmente inscritos en el semestre lectivo vigente.
• Consultar la convocatoria de 'Permutas' que publica la DGAE al término del ciclo escolar.
• Registrar la solicitud en los tiempos establecidos y entregar los historiales académicos en la ventanilla de Servicios Escolares para su validación técnica.
        """

    @staticmethod
    def tram_seguro_texto():
        return """
🏥 SEGURO FACULTATIVO (IMSS)

Como alumno de la UNAM, tienes derecho al servicio médico gratuito del IMSS durante tu permanencia en la carrera.

📋 REQUISITOS Y PASOS:
• Obtén tu Número de Seguridad Social (NSS) en la página oficial del IMSS Digital.
• Ingresa al sistema de Servicios Escolares de la FES Aragón y registra tu NSS en el apartado de 'Seguro Médico'.
• Descarga tu comprobante de vigencia de derechos para validar que la UNAM ya te dio de alta como estudiante activo.
        """

    @staticmethod
    def tram_baja_materias_texto():
        return """
📉 BAJA DE ASIGNATURAS (ORDINARIA Y EXTEMPORÁNEA)

• BAJA ORDINARIA: Se realiza dentro de los plazos establecidos en el Calendario Escolar (primeras semanas del semestre). El trámite se procesa directamente en línea a través del sistema TramiFES.
• BAJA EXTEMPORÁNEA: Fuera del periodo ordinario, únicamente procede por causas de fuerza mayor justificables (salud, trabajo, etc.). Debes entregar carta exposición de motivos dirigida a tu Jefatura de Carrera.
        """

    @staticmethod
    def tram_baja_semestre_texto():
        return """
❌ BAJA DEL SEMESTRE (TEMPORAL REGLAMENTARIA O DEFINITIVA)

• BAJA TEMPORAL REGLAMENTARIA: Se solicita durante las primeras semanas del bloque lectivo directamente en ventanilla. No afecta tu historial si cumples los plazos del artículo 22 del Reglamento General de Inscripciones.
• BAJA DEFINITIVA: Renuncia formal a tu lugar en la carrera. Implica la devolución de tus documentos originales (Acta, Certificado de Bachillerato) previa entrega de tu credencial y firmas de no adeudo en laboratorios ni biblioteca.
        """