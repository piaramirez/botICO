# menus.py - Sistema de menús y botones

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
║  🗓️ SEMESTRE 2025-2:                                            ║
║     • Registro en línea: 10 - 25 de enero                        ║
║     • Pago de cuotas: 10 - 28 de enero                           ║
║     • Inicio de clases: Primera semana de febrero                ║
║                                                                  ║
║  🗓️ PRÓXIMA CONVOCATORIA 2026-1:                                ║
║     • Convocatoria: Septiembre - octubre                         ║
║     • Registro: noviembre - diciembre                            ║
║     • Examen de admisión: enero                                  ║
║                                                                  ║
║  👉 Usa los botones interactivos del chat para ver tu proceso.   ║
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
    def mensaje_preguntas_nuevo_ingreso():
        return """
╔══════════════════════════════════════════════════════════════════╗
║              ❓ PREGUNTAS FRECUENTES - NUEVO INGRESO             ║
╠══════════════════════════════════════════════════════════════════╣
║  💰 ¿CUÁNTO CUESTA?                                              ║
║     $0.50 centavos (pago mínimo $100 MXN)                        ║
║                                                                  ║
║  📄 ¿QUÉ DOCUMENTOS NECESITO?                                    ║
║     Acta, CURP, certificado, comprobante, 4 fotos, certificado   ║
║                                                                  ║
║  📝 ¿CÓMO ME INSCRIBO?                                           ║
║     1. Registro en línea                                         ║
║     2. Pago en caja o transferencia                              ║
║     3. Subir documentos                                          ║
║     4. Esperar validación                                        ║
║     5. Seleccionar horario                                       ║
║                                                                  ║
║  🔗 https://www.fes-aragon.unam.mx/nuevo-ingreso                 ║
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
    def mensaje_inscripciones_nuevo():
        return """
╔══════════════════════════════════════════════════════════════════╗
║                    📋 INSCRIPCIÓN - NUEVO INGRESO                ║
╠══════════════════════════════════════════════════════════════════╣
║  💰 COSTO: $0.50 centavos (mínimo $100 MXN)                      ║
║                                                                  ║
║  📄 DOCUMENTOS NECESARIOS:                                       ║
║     • Acta de nacimiento (original y copia)                      ║
║     • CURP (original y copia)                                    ║
║     • Certificado de bachillerato                                ║
║     • Comprobante de domicilio reciente                          ║
║     • 4 fotografías tamaño infantil (blanco y negro)             ║
║     • Certificado médico (formato FES Aragón)                    ║
║                                                                  ║
║  📝 PASOS PARA INSCRIBIRTE:                                      ║
║     1. Registro en línea en la DGAE                              ║
║     2. Pago de cuotas en caja o transferencia                    ║
║     3. Subir documentos escaneados                               ║
║     4. Esperar validación (3-5 días)                             ║
║     5. Seleccionar horario en línea                              ║
║     6. Descargar comprobante                                     ║
║     7. Recoger credencial en Control Escolar                     ║
║                                                                  ║
║  🔗 https://www.fes-aragon.unam.mx/inscripciones                 ║
║  📧 ingreso@fes-aragon.unam.mx                                   ║
╚══════════════════════════════════════════════════════════════════╝
    """    
    @staticmethod
    def mensaje_no_entendido():
        return "❓ No entendí tu pregunta. Puedes escribir 'menú' para ver las opciones disponibles o reformular tu duda."