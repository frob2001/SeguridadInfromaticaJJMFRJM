from config import fdb

data = {
    "1_1": {
        "Clasificacion": "Industrial",
        "Amenaza": "Daños por agua",
        "Vulnerabilidad": "Falta de protección contra daños por agua",  
        "Calificación": 4,
        "DC": True,
        "SW": False,
        "HW": True,
        "R": True,
        "P": True,
        "IF": True,
        "DT": False,
        "DM": False
    },
    "1_2": {
        "Clasificacion": "Industrial",
        "Amenaza": "Daños por fuego",
        "Vulnerabilidad": "Falta de protección contra daños por fuego", 
        "Calificación": 4,
        "DC": True,
        "SW": False,
        "HW": True,
        "R": True,
        "P": True,
        "IF": True,
        "DT": False,
        "DM": False
    },
    "1_3": {
        "Clasificacion": "Industrial",
        "Amenaza": "Desastres industriales",
        "Vulnerabilidad": "Falta de protección contra desastres industriales", 
        "Calificación": 4,
        "DC": True,
        "SW": False,
        "HW": True,
        "R": True,
        "P": True,
        "IF": True,
        "DT": False,
        "DM": False
    },
    "1_4": {
        "Clasificacion": "Industrial",
        "Amenaza": "Degradación de activos",
        "Vulnerabilidad": "Activos desprotegidos contra la degradación",
        "Calificación": 2,
        "DC": False,
        "SW": True,
        "HW": True,
        "R": True,
        "P": False,
        "IF": False,
        "DT": False,
        "DM": False
    },
    "2_1": {
        "Clasificacion": "Errores y fallos no intencionados",
        "Amenaza": "Errores del administrador",
        "Vulnerabilidad": "Falta de conocimiento o capacitación adecuada del administrador",
        "Calificación": 3,
        "DC": False,
        "SW": True,
        "HW": True,
        "R": True,
        "P": False,
        "IF": True,
        "DT": False,
        "DM": True
    },
    "2_2": {
        "Clasificacion": "Errores y fallos no intencionados",
        "Amenaza": "Errores de los usuarios",
        "Vulnerabilidad": "Falta de conocimiento o capacitación adecuada de los usuarios",
        "Calificación": 2,
        "DC": False,
        "SW": True,
        "HW": True,
        "R": False,
        "P": False,
        "IF": True,
        "DT": False,
        "DM": True
    },
    "2_3": {
        "Clasificacion": "Errores y fallos no intencionados",
        "Amenaza": "Difusión de software dañino",
        "Vulnerabilidad": "Falta de medidas de seguridad y conciencia de los usuarios",
        "Calificación": 5,
        "DC": False,
        "SW": True,
        "HW": False,
        "R": False,
        "P": False,
        "IF": False,
        "DT": False,
        "DM": False
    },
    "2_4": {
        "Clasificacion": "Errores y fallos no intencionados",
        "Amenaza": "Destrucción de información",
        "Vulnerabilidad": "Falta de medidas de protección y respaldo de datos adecuadas",
        "Calificación": 5,
        "DC": False,
        "SW": True,
        "HW": False,
        "R": True,
        "P": False,
        "IF": False,
        "DT": True,
        "DM": False
    },
    "3_1": {
        "Clasificacion": "Ataques intencionados",
        "Amenaza": "Hurto de medios o documentos",
        "Vulnerabilidad": "Falta de medidas de seguridad física y lógica",
        "Calificación": 4,
        "DC": True,
        "SW": True,
        "HW": True,
        "R": False,
        "P": True,
        "IF": True,
        "DT": True,
        "DM": True
    },
    "3_2": {
        "Clasificacion": "Ataques intencionados",
        "Amenaza": "Uso no autorizado",
        "Vulnerabilidad": "Falta de controles de acceso adecuados",
        "Calificación": 4,
        "DC": True,
        "SW": True,
        "HW": True,
        "R": False,
        "P": True,
        "IF": True,
        "DT": True,
        "DM": True
    },
    "3_3": {
        "Clasificacion": "Ataques intencionados",
        "Amenaza": "Corrupción de datos",
        "Vulnerabilidad": "Falta de medidas de integridad de datos adecuadas",
        "Calificación": 4,
        "DC": False,
        "SW": False,
        "HW": False,
        "R": False,
        "P": False,
        "IF": False,
        "DT": True,
        "DM": False
    },
    "3_4": {
        "Clasificacion": "Ataques intencionados",
        "Amenaza": "Mal uso de software",
        "Vulnerabilidad": "Falta de controles y políticas de uso adecuadas",
        "Calificación": 2,
        "DC": False,
        "SW": False,
        "HW": False,
        "R": False,
        "P": False,
        "IF": False,
        "DT": True,
        "DM": False
    },
    "3_5": {
        "Clasificacion": "Ataques intencionados",
        "Amenaza": "Espionaje remoto",
        "Vulnerabilidad": "Falta de medidas de seguridad adecuadas en los sistemas y redes",
        "Calificación": 4,
        "DC": False,
        "SW": True,
        "HW": True,
        "R": False,
        "P": False,
        "IF": True,
        "DT": False,
        "DM": False
    },
    "3_6": {
        "Clasificacion": "Ataques intencionados",
        "Amenaza": "Ataques de ciberseguridad",
        "Vulnerabilidad": "Falta de protección y preparación contra ataques de ciberseguridad",
        "Calificación": 5,
        "DC": False,
        "SW": True,
        "HW": False,
        "R": False,
        "P": True,
        "IF": True,
        "DT": True,
        "DM": True
    },
    "3_7": {
        "Clasificacion": "Ataques intencionados",
        "Amenaza": "Ataques al personal",
        "Vulnerabilidad": "Falta de conciencia y capacitación en seguridad cibernética",
        "Calificación": 4,
        "DC": False,
        "SW": False,
        "HW": False,
        "R": True,
        "P": False,
        "IF": False,
        "DT": False,
        "DM": False
    }
}

for codigo, valores in data.items():
    fdb.child("Amenazas").child(codigo).set(valores)


data = {
    "1_1": {
        "0": "Instalar sistemas de detección y alarma de fugas de agua para una detección temprana y rápida respuesta.",
        "1": "Implementar sistemas de protección contra inundaciones, como barreras físicas o sistemas de drenaje adecuados.",
        "2": "Realizar inspecciones y mantenimiento regular de las tuberías y sistemas de plomería para identificar y solucionar problemas antes de que causen daños significativos."
    },
    "1_2": {
        "0": "Instalar y mantener sistemas de detección de incendios y alarmas para una respuesta rápida.",
        "1": "Implementar sistemas de extinción de incendios apropiados, como extintores, rociadores automáticos o sistemas de supresión de incendios.",
        "2": "Establecer políticas y procedimientos claros de seguridad contra incendios, que incluyan capacitación regular para el personal y prácticas seguras de manipulación y almacenamiento de materiales inflamables."
    },
    "1_3": {
        "0": "Realizar evaluaciones de riesgos y estudios de impacto para identificar y comprender los posibles desastres industriales relevantes.",
        "1": "Desarrollar y mantener planes de contingencia y continuidad del negocio que aborden los escenarios de desastres identificados.",
        "2": "Establecer medidas de protección y seguridad adecuadas, como el uso de equipo de protección personal y el cumplimiento de regulaciones y estándares de seguridad industrial."
    },
    "1_4": {
        "0": "Implementar un programa de mantenimiento preventivo regular para garantizar el buen estado y funcionamiento de los activos.",
        "1": "Establecer procedimientos y prácticas de uso y manipulación adecuados para minimizar el desgaste y la degradación de los activos.",
        "2": "Realizar monitoreo continuo de los activos, utilizando tecnologías como sensores y sistemas de gestión de activos, para detectar signos tempranos de degradación y tomar medidas correctivas oportunas."
    },
    "2_1": {
        "0": "Implementar un sistema de revisión y aprobación de cambios, donde los cambios en la configuración y la administración de los sistemas sean revisados y aprobados por personal autorizado.",
        "1": "Establecer una política de privilegios y accesos basada en el principio de menor privilegio, limitando los derechos y privilegios administrativos solo a los roles y personas necesarias.",
        "2": "Proporcionar capacitación y concienciación regular sobre las mejores prácticas de administración de sistemas y seguridad informática para el personal administrativo."
    },
    "2_2": {
        "0": "Realizar programas de concienciación y capacitación en seguridad informática para educar a los usuarios sobre las mejores prácticas y los riesgos asociados con los errores de los usuarios.",
        "1": "Implementar políticas y controles de acceso adecuados que limiten los derechos y privilegios de los usuarios a lo necesario para realizar sus tareas.",
        "2": "Establecer sistemas de monitoreo y detección de comportamientos inusuales o riesgosos por parte de los usuarios, como actividad sospechosa o intentos de acceso no autorizado."
    },
    "2_3": {
        "0": "Implementar sistemas de seguridad de correo electrónico y filtrado de contenido para bloquear y detectar correos electrónicos y archivos adjuntos maliciosos.",
        "1": "Mantener software y aplicaciones actualizadas con los últimos parches de seguridad para mitigar vulnerabilidades conocidas.",
        "2": "Utilizar soluciones de seguridad en endpoints, como software antivirus y antimalware, para detectar y bloquear software dañino en los dispositivos."
    },
    "2_4": {
        "0": "Implementar medidas de respaldo y recuperación de datos, como realizar copias de seguridad regulares y almacenarlas de manera segura en ubicaciones externas.",
        "1": "Establecer políticas y procedimientos de gestión de registros que especifiquen los requisitos de retención y disposición segura de la información.",
        "2": "Aplicar controles de acceso y autenticación robustos para proteger la información contra accesos no autorizados y asegurar la integridad y confidencialidad de los datos."
    },
    "3_1": {
        "0": "Establecer controles físicos, como el uso de cerraduras, acceso restringido y monitoreo de áreas de almacenamiento de medios o documentos sensibles.",
        "1": "Implementar sistemas de seguimiento y registro de activos, como el uso de etiquetas de identificación por radiofrecuencia (RFID), para realizar un seguimiento y monitoreo efectivos de los medios y documentos.",
        "2": "Proporcionar capacitación al personal sobre la importancia de la seguridad física de los medios y documentos, y promover la conciencia de la responsabilidad individual en la protección de los activos."
    },
    "3_2": {
        "0": "Implementar políticas de acceso y control de usuarios que especifiquen los derechos y privilegios de acceso a sistemas y datos, y asegurarse de que se apliquen de manera efectiva.",
        "1": "Utilizar autenticación multifactorial para verificar la identidad de los usuarios y proteger contra accesos no autorizados.",
        "2": "Establecer sistemas de monitoreo y detección de actividad sospechosa o intentos de acceso no autorizado en la red y los sistemas."
    },
    "3_3": {
        "0": "Implementar soluciones de respaldo y recuperación de datos para restaurar versiones limpias y confiables en caso de corrupción de datos.",
        "1": "Utilizar soluciones de detección y prevención de intrusos para monitorear y detectar intentos de manipulación o corrupción de datos.",
        "2": "Establecer políticas y procedimientos de gestión de cambios y actualizaciones de software que minimicen el riesgo de corrupción de datos durante los procesos de actualización y migración."
    },
    "3_4": {
        "0": "Establecer políticas y procedimientos claros sobre el uso aceptable del software y las restricciones de licencia.",
        "1": "Realizar una revisión y monitoreo periódicos del software instalado para identificar y eliminar cualquier software no autorizado o no deseado.",
        "2": "Proporcionar capacitación y concienciación al personal sobre las prácticas seguras de uso del software y los riesgos asociados con su mal uso."
    },
    "3_5": {
        "0": "Implementar soluciones de seguridad en la red, como firewalls, sistemas de detección y prevención de intrusiones (IDS/IPS) y sistemas de monitoreo de red, para detectar y bloquear actividades de espionaje remoto.",
        "1": "Establecer políticas y prácticas de seguridad para la protección de la información sensible y la comunicación segura, como el uso de encriptación de datos y redes privadas virtuales (VPN).",
        "2": "Realizar auditorías de seguridad y evaluaciones de riesgos periódicas para identificar posibles vulnerabilidades y brechas de seguridad que podrían ser explotadas por actividades de espionaje remoto."
    },
    "3_6": {
        "0": "Implementar soluciones de seguridad en capas, que incluyan firewalls, sistemas de detección y prevención de intrusiones, antivirus y antimalware, y sistemas de autenticación fuerte.",
        "1": "Realizar análisis y pruebas de vulnerabilidad periódicos para identificar y remediar las vulnerabilidades conocidas antes de que sean explotadas por ataques.",
        "2": "Establecer un programa de concienciación y capacitación en seguridad cibernética para el personal, promoviendo una cultura de seguridad y buenas prácticas de seguridad informática."
    },
    "3_7": {
        "0": "Implementar políticas y procedimientos de seguridad que incluyan una gestión efectiva de identidad y acceso, y un control de privilegios basado en el principio de menor privilegio.",
        "1": "Proporcionar capacitación y concienciación regular sobre la ingeniería social y las tácticas de phishing para ayudar a los empleados a reconocer y evitar ataques dirigidos al personal.",
        "2": "Establecer sistemas de monitoreo y detección de actividades sospechosas en los sistemas y redes, y contar con una respuesta efectiva a incidentes de seguridad para mitigar los ataques al personal."
    }
}


for codigo, valores in data.items():
    fdb.child("Medidas").child(codigo).set(valores)