from django.db import models
from apps.academico.models import *
import datetime
from constance import config
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

from simple_history.models import HistoricalRecords

def gestion():
	now = datetime.datetime.now()
	return config.GESTION if (config.GESTION_ACTIVO) else now.year

# Create your models here.
class evaluacion_recurricular(models.Model):
	carrera = models.ForeignKey(carrera, on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, on_delete= models.CASCADE)
	gestion = models.IntegerField(
		verbose_name=u'Gestion',
		null=False,
		blank=False,
		unique=True,
		default=gestion
	)
	activo = models.BooleanField(
		null=False,
		blank=False,
		default=True
	)
	genero = models.CharField(
		verbose_name=u'Genero',
		max_length=1,
		null=False,
		blank=False,
		choices= (('m','Masculino'),('f','Femenino'))
	)
	director = models.CharField(
		verbose_name=u'Aplicar en caso de que la respuesta sea Director.',
		max_length=2,
		null=True,
		blank=True,
		choices=(('t','Titular'),('i','A ínterin'))
	)
	aprobacion = models.DateField(
		verbose_name=u'Indique en qué fecha se aprobó el actual diseño curricular que está aplicando la carrera (RAN)',
		null=False,
		blank=False
	)
	#etapa1
	retapa_1 = models.BooleanField(
		verbose_name=u'La carrera realizo la etapa de Jornada Académica?',
		blank=True,
		null=False,
	)
	netapa_1 = MultiSelectField(
		verbose_name=u'Porque no realizó esta etapa? (Jornada Académica)',
		max_choices=5,
		max_length=20,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'),('o','Otros'))
	)
	oetapa_1 = models.TextField(
		verbose_name=u'Cuales otros?',
		blank=True,
		null=True
	)
	#etapa2
	retapa_2 = models.BooleanField(
		verbose_name=u'La carrera realizo la etapa de Diagnostico Inicial?',
		blank=True,
		null=False,
	)
	netapa_2 = MultiSelectField(
		verbose_name=u'Porque no realizó esta etapa? (Diagnostico Inicial)',
		max_choices=5,
		max_length=20,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'),('o','Otros'))
	)
	oetapa_2 = models.TextField(
		verbose_name=u'Cuales otros?',
		blank=True,
		null=True
	)
	#etapa3
	retapa_3 = models.BooleanField(
		verbose_name=u'La carrera realizo la etapa de Estudio de Contexto?',
		blank=True,
		null=False,
	)
	netapa_3 = MultiSelectField(
		verbose_name=u'Porque no realizó esta etapa? (Estudio de Contexto)',
		max_choices=5,
		max_length=20,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'),('o','Otros'))
	)
	oetapa_3 = models.TextField(
		verbose_name=u'Cuales otros?',
		blank=True,
		null=True
	)
	#etapa4
	retapa_4 = models.BooleanField(
		verbose_name=u'La carrera realizo la etapa de Mesa Multisectorial?',
		blank=True,
		null=False,
	)
	netapa_4 = MultiSelectField(
		verbose_name=u'Porque no realizó esta etapa? (Mesa Multisectorial)',
		max_choices=5,
		max_length=20,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'),('o','Otros'))
	)
	oetapa_4 = models.TextField(
		verbose_name=u'Cuales otros?',
		blank=True,
		null=True
	)
	#etapa5
	retapa_5 = models.BooleanField(
		verbose_name=u'La carrera realizo la etapa de Macro Curricula?',
		blank=True,
		null=False,
	)
	netapa_5 = MultiSelectField(
		verbose_name=u'Porque no realizó esta etapa? (Macro Curricula)',
		max_choices=5,
		max_length=20,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'),('o','Otros'))
	)
	oetapa_5 = models.TextField(
		verbose_name=u'Cuales otros?',
		blank=True,
		null=True
	)
	#etapa6
	retapa_6 = models.BooleanField(
		verbose_name=u'La carrera realizo la etapa de Reunión Académica de la RAC?',
		blank=True,
		null=False,
	)
	netapa_6 = MultiSelectField(
		verbose_name=u'Porque no realizó esta etapa? (Reunión Académica de la RAC)',
		max_choices=5,
		max_length=20,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'),('o','Otros'))
	)
	oetapa_6 = models.TextField(
		verbose_name=u'Cuales otros?',
		blank=True,
		null=True
	)
	#etapa7
	retapa_7 = models.BooleanField(
		verbose_name=u'La carrera realizo la etapa de Reunión Académica Nacional RAN',
		blank=True,
		null=False,
	)
	netapa_7 = MultiSelectField(
		verbose_name=u'Porque no realizó esta etapa? (Reunión Académica Nacional RAN)',
		max_choices=5,
		max_length=20,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'),('o','Otros'))
	)
	oetapa_7 = models.TextField(
		verbose_name=u'Cuales otros?',
		blank=True,
		null=True
	)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.gestion)

class etapa_1(models.Model):
	evaluacion_recurricular = models.OneToOneField(
		evaluacion_recurricular,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	pregunta_1 = models.BooleanField(
		verbose_name=u'1.1.	El Departamento de Gestión Curricular, programó con anticipación la jornada académica, cumpliendo con las etapas requeridas.',
		blank=False,
		null=False
	)
	pregunta_2 = models.CharField(
		verbose_name=u'1.2.	Qué tipo de enfoque es el que se utilizó para el rediseño curricular. Elija una opción',
		max_length=2,
		blank=False,
		null=False,
		choices=(('c','Formación Basada en competencias'),('po','Por objetivos'),('o','Otros'))
	)
	opregunta_2 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_3 = models.BooleanField(
		verbose_name=u'1.3.	Se realizaron exposiciones (departamento de gestión Curricular) para la comprensión del proceso de rediseño curricular',
		blank=False,
		null=False
	)
	pregunta_4 = models.CharField(
		verbose_name=u'1.4.	¿La comprensión de la exposición de las etapas metodológicas del rediseño curricular fue? Elija una opción:',
		max_length=2,
		blank=False,
		null=False,
		choices=(('b','Buena'),('ra','Razonable'),('re','Regular'),('d','Deficiente'))
	)
	sugpregunta_4 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_5 = models.BooleanField(
		verbose_name=u'1.5.	Se necesitó ampliar la exposición de las etapas metodológicas del rediseño curricular',
		blank=False,
		null=False
	)
	pregunta_6 = MultiSelectField(
		verbose_name=u'1.6.	Que herramienta digital utilizó para organizar la información en esta etapa. Puede elegir varias opciones:',
		max_choices=4,
		max_length=20,
		blank=False,
		null=False,
		choices=(('b','Computadora'),('c','Celular'),('d','Data Display'),('o','Otros'))
	)
	opregunta_6 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_7 = models.CharField(
		verbose_name=u'1.7.	Que calificación daría al equipo de gestión curricular en esta etapa.',
		max_length=2,
		blank=False,
		null=False,
		choices=(('b','Bueno'),('o','Oportuno'),('r','Regular'))
	)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.evaluacion_recurricular)

class etapa_2(models.Model):
	evaluacion_recurricular = models.OneToOneField(
		evaluacion_recurricular,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	pregunta_1 = models.IntegerField(
		verbose_name=u'2.2.	El formulario FDI-1: documentos de creación, fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_1 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_2 = models.IntegerField(
		verbose_name=u'2.3.	El formulario FDI-2: plan curricular vigente, fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_2 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_3 = models.IntegerField(
		verbose_name=u'2.4.	El formulario FDI-3a de componente docentes, fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_3 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_4 = models.IntegerField(
		verbose_name=u'2.5.	El formulario FDI-3b: componentes estudiantes, fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_4 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_5 = models.IntegerField(
		verbose_name=u'2.6.	El formulario FDI-3c: componente de interacción, fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_5 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_6 = models.IntegerField(
		verbose_name=u'2.7.	El formulario FDI-3d: componente de recursos educativos fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_6 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_7 = models.IntegerField(
		verbose_name=u'2.8.	El formulario FDI-3e: administración financiera, fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_7 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_8 = models.IntegerField(
		verbose_name=u'2.9.	El formulario FDI-3f: componente de equipamiento, fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_8 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_9 = models.IntegerField(
		verbose_name=u'2.10. El formulario FDI-3g: seguimiento a graduados, fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_9 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_10 = models.IntegerField(
		verbose_name=u'2.11. El formulario FDI-4a de pertinencia estudiantil, fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_10 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_11 = models.IntegerField(
		verbose_name=u'2.12. El formulario FDI-4b: cuestionario de pertinencia docente, fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	) 
	sugpregunta_11 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_12 = MultiSelectField(
		verbose_name=u'2.13. Que dificultad tuvo al momento de hacer la recolección de información con los formularios antes mencionados. Seleccione Varias opciones',
		max_choices=4,
		max_length=20,
		blank=False,
		null=False,
		choices=(('pp','Poca predisposición de los encuestados'),('de','Demora en la entrega de las encuestas'),('pc','Poca comprensión de los formularios'),('o','Otros'))
	)
	opregunta_12 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_13 = MultiSelectField(
		verbose_name=u'1.6. Que herramienta digital utilizó para organizar la información en esta etapa. Puede elegir varias opciones:',
		max_choices=4,
		max_length=20,
		blank=False,
		null=False,
		choices=(('b','Computadora'),('c','Celular'),('d','Data Display'),('o','Otros'))
	)
	opregunta_13 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_14 = models.CharField(
		verbose_name=u'2.15. Que calificación daría al equipo de gestión curricular en esta etapa.',
		max_length=2,
		blank=False,
		null=False,
		choices=(('b','Bueno'),('o','Oportuno'),('r','Regular'))
	)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.evaluacion_recurricular)

class etapa_3(models.Model):
	evaluacion_recurricular = models.OneToOneField(
		evaluacion_recurricular,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	pregunta_1 = models.IntegerField(
		verbose_name=u'3.2.	El formulario F-EC1; mapeo de actores institucionales e informantes fue.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_1 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_2 = models.IntegerField(
		verbose_name=u'3.3.	El formulario F-EC2, cuestionarios realizados a empleadores públicos y privados sirvieron para la obtención de resultados de manera.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_2 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_3 = models.IntegerField(
		verbose_name=u'3.4.	El formulario F-EC3, cuestionarios realizados a profesionales con empleo sirvieron para la obtención de resultados de manera.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_3 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_4 = models.IntegerField(
		verbose_name=u'3.5.	El formulario F-EC4, cuestionarios realizados a profesionales sin empleo sirvieron para la obtención de resultados de manera.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_4 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_5 = models.IntegerField(
		verbose_name=u'3.6.	El formulario F-EC5, entrevistas a expertos sirvió para la obtención de resultados de manera.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_5 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_6 = models.IntegerField(
		verbose_name=u'3.7.	El formulario F-EC6, análisis documental denota los requerimientos para el desarrollo del rediseño curricular, es.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_6 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_7 = models.IntegerField(
		verbose_name=u'3.8.	El formulario F-EC7, de oferta formativa nacional sirvió de manera.',
		blank=False,
		null=False,
		choices=((4,'Muy útil'),(3,'Relativamente útil'),(2,'Moderadamente útil'),(1,'Poco útil'),(0,'Nada útil'))
	)
	sugpregunta_7 = models.TextField(
		verbose_name=u'Que sujiere?',
		blank=True,
		null=True
	)
	pregunta_8 = models.IntegerField(
		verbose_name=u'3.9.	Con la aplicación de los instrumentos y metodología detallados anteriormente, se pudo identificar de manera cualitativa y cuantitativa la demanda del mercado profesional.',
		blank=False,
		null=False,
		choices=((3,'Buena Identificacion'),(2,'Razonable identificación'),(1,'Regular identificación'),(0,'Deficiente identificación'))
	)
	pregunta_9 = models.IntegerField(
		verbose_name=u'3.10. Con la aplicación de los instrumentos y metodología detallados anteriormente se identificaron las principales áreas de desempeño profesionales, sus funciones….',
		blank=False,
		null=False,
		choices=((3,'Buena Identificacion'),(2,'Razonable identificación'),(1,'Regular identificación'),(0,'Deficiente identificación'))
	)
	pregunta_10 = models.IntegerField(
		verbose_name=u'3.11. Con la aplicación de los instrumentos fuentes primarias y secundarias se pudo estructurar sistémicamente el proyecto curricular que responde a las exigencias y necesidades de la realidad actual.',
		blank=False,
		null=False,
		choices=((3,'Buena Identificacion'),(2,'Razonable identificación'),(1,'Regular identificación'),(0,'Deficiente identificación'))
	)
	pregunta_11 = models.IntegerField(
		verbose_name=u'3.12. Con la aplicación de los instrumentos fuentes primarias y secundarias se pudo identificar las familias laborales en el rediseño curricular ',
		blank=False,
		null=False,
		choices=((3,'Buena Identificacion'),(2,'Razonable identificación'),(1,'Regular identificación'),(0,'Deficiente identificación'))
	)
	pregunta_12 = MultiSelectField(
		verbose_name=u'3.13. Que herramientas de apoyo y recolección de información se utilizó en esta etapa, para acceder a los colaboradores; selecciones varias opciones ',
		max_choices=5,
		max_length=20,
		blank=False,
		null=False,
		choices=(("i",'Internet'),("c",'Computadora'),("h",'Hojas electrónicas'),("s",'Software estadístico'),("o","Otros"))
	)
	opregunta_12 = models.TextField(
		verbose_name=u'Que otros?',
		blank=True,
		null=True
	)
	pregunta_13 = models.CharField(
		verbose_name=u'3.14. Que calificación daría al equipo de gestión curricular en esta etapa.',
		max_length=2,
		blank=False,
		null=False,
		choices=(('b','Bueno'),('o','Oportuno'),('r','Regular'))
	)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.evaluacion_recurricular)

class etapa_4(models.Model):
	evaluacion_recurricular = models.OneToOneField(
		evaluacion_recurricular,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	pregunta_1 = models.BooleanField(
		verbose_name=u'4.2.	Se cumplió toda la metodología planteada por el departamento de gestión curricular para llevar a cabo la reunión multisectorial.',
		blank=False,
		null=False
	)
	pregunta_2 = models.CharField(
		verbose_name=u'4.3.	Que grado de comprensión se tuvo en la exposición de los resultados de contexto por el responsable académico (Director o Representante de la comisión).',
		max_length=2,
		blank=False,
		null=False,
		choices=(('b','Buena'),('ra','Razonable'),('re','Regular'),('d','Deficiente'))
	)
	sugpregunta_2 = models.TextField(
		verbose_name=u'Que sugiere?',
		blank=True,
		null=True
	)
	pregunta_3 = models.BooleanField(
		verbose_name=u'4.4.	La conformación de las mesas temáticas fue asignada en función de las familias laborales y de acuerdo a la necesidad del rediseño curricular.',
		blank=False,
		null=False
	)
	pregunta_4 = MultiSelectField(
		verbose_name=u'4.5.	Las mesas temáticas estaban conformadas por:',
		max_choices=6,
		max_length=20,
		blank=False,
		null=False,
		choices=(('e','Expertos'),('i','Instituciones'),('a','Autoridades'),('d','Docentes'),('e','Estudiantes'),('o','Otros'))
	)
	opregunta_4 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_5 = models.BooleanField(
		verbose_name='4.6.	Se hizo una plenaria con los representantes de las diferentes mesas temáticas:',
		blank=False,
		null=False
	)
	pregunta_5_1 = models.CharField(
		verbose_name=u'4.6.1. El grado de la comprensión de la metodología empleada fue.',
		max_length=2,
		blank=True,
		null=True,
		choices=(('ex','Excelente'),('b','Buena'),('ra','Razonable'),('re','Regular'),('d','Deficiente'))
	)
	pregunta_6 = MultiSelectField(
		verbose_name=u'4.7.	Que dificultades se identificaron para aprobar y validar los resultados de las mesas temáticas en pleno por la sala:',
		max_choices=6,
		max_length=20,
		blank=False,
		null=False,
		choices=(('nc','No se comprendió la metodología '),('cp','Falta de compromiso de los participantes'),('ac','No se pudo llegar a un acuerdo conjunto'),('o','Otros'))
	)
	opregunta_6 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_7 = models.CharField(
		verbose_name=u'4.8.	Se realizó el fortalecimiento de cada una de las familias laborales en base a las:',
		max_length=2,
		blank=False,
		null=False,
		choices=(('ad','Áreas de desempeño'),('cg','Competencia Global'),('np','Nodos problematizadores'),('o','Otros'))
	)
	opregunta_7 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_8 = models.CharField(
		verbose_name=u'4.9.	Que calificación daría al equipo de gestión curricular en esta etapa.',
		max_length=2,
		blank=False,
		null=False,
		choices=(('b','Bueno'),('o','Oportuno'),('r','Regular'))
	)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.evaluacion_recurricular)

class etapa_5(models.Model):
	evaluacion_recurricular = models.OneToOneField(
		evaluacion_recurricular,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	pregunta_1 = models.BooleanField(
		verbose_name=u'5.2. Las familias laborales identificadas tienen correlación entre ellas y abastecen para contemplar todo lo necesario en la formación profesional.',
		blank=False,
		null=False
	)
	pregunta_2 = models.IntegerField(
		verbose_name=u'5.3.	La metodología para obtener la congruencia entre las familias laborales y el contexto sociocultural de la región y nacional fue:',
		blank=False,
		null=False,
		choices=((5,"Excelente"),(4,"Buena"),(3,"Razonable"),(2,"Regular"),(1,"Deficiente"))
	)
	pregunta_3 = models.IntegerField(
		verbose_name=u'5.4.	La metodología empleada para identificar las competencias globales del perfil profesional académico de egreso es:',
		blank=False,
		null=False,
		choices=((5,"Muy útil"),(4,"Relativamente útil"),(3,"Moderadamente útil"),(2,"Poco útil"),(1,"Nada útil"))
	)
	pregunta_4 = models.IntegerField(
		verbose_name=u'5.5.	La metodología para obtener la pertenencia de las materias en las distintas familias laborales fue.',
		blank=False,
		null=False,
		choices=((5,"Muy Adecuada"),(4,"Adecuada"),(3,"Neutral"),(2,"Poco adecuada"),(1,"Inadecuada"))
	) 
	pregunta_5 = models.BooleanField(
		verbose_name=U'5.6.	Existieron instancias participativas de retroalimentación (mejoras y modificaciones) de la Malla Curricular.',
		blank=False,
		null=False
	)
	pregunta_5_1 = models.IntegerField(
		verbose_name=u'5.6.1. Qué grado de modificación se realizó en la retroalimentación.',
		blank=True,
		null=True,
		choices=((3,"Alta"),(2,"Media"),(1,"Baja"))
	)
	pregunta_6 = models.BooleanField(
		verbose_name=U'5.7.	Se realizó algún instrumento que denote el total de créditos, la distribución crediticia por área de formación y la proporción de horas teóricas y horas prácticas que estén dentro de los rangos recomendados.',
		blank=False,
		null=False
	)
	pregunta_6_1 = models.IntegerField(
		verbose_name=u'5.7.1. Que tan importante fue el uso de este instrumento para para generar la malla curricular.',
		blank=True,
		null=True,
		choices=((5,"Muy útil"),(4,"Relativamente útil"),(3,"Moderadamente útil"),(2,"Poco útil"),(1,"Nada útil"))
	)
	pregunta_7 = models.IntegerField(
		verbose_name=u'5.8.	La valoración que se da a las horas teóricas y prácticas en función de su cantidad como de su nivel de complejidad es:',
		blank=False,
		null=False,
		choices=((5,"Muy Adecuada"),(4,"Adecuada"),(3,"Neutral"),(2,"Poco adecuada"),(1,"Inadecuada"))
	)
	pregunta_8 = models.IntegerField(
		verbose_name=u'5.9. La ubicación de las materias de acuerdo a las áreas de desempeño y familias laborales, de acuerdo a su grado de complejidad son:',
		blank=False,
		null=False,
		choices=((5,"Muy Adecuada"),(4,"Adecuada"),(3,"Neutral"),(2,"Poco adecuada"),(1,"Inadecuada"))
	)
	pregunta_9 = models.CharField(
		verbose_name=u'5.10. Toda La documentación generada en el rediseño curricular esta etapa la tiene guardada en formato:',
		max_length=2,
		blank=False,
		null=False,
		choices=(("di","Digital en internet"),("dc","Digital en una computadora"),("h","Hojas foliadas"),("nt","No tiene"),("o","Otros"))
	)
	opregunta_9 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_7 = models.CharField(
		verbose_name=u'5.11. Que calificación daría al equipo de gestión curricular en esta etapa.',
		max_length=2,
		blank=False,
		null=False,
		choices=(('b','Bueno'),('o','Oportuno'),('r','Regular'))
	)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.evaluacion_recurricular)

class etapa_6(models.Model):
	evaluacion_recurricular = models.OneToOneField(
		evaluacion_recurricular,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	pregunta_1 = models.IntegerField(
		verbose_name=u'6.2.	La respuesta fue SI. aplicar las siguientes preguntas La aplicación de normativas vigentes establecidas en la Reunión Académica de Carrera fue:',
		blank=False,
		null=False,
		choices=((5,"Muy Adecuada"),(4,"Adecuada"),(3,"Neutral"),(2,"Poco adecuada"),(1,"Inadecuada"))
	)
	pregunta_2 = models.BooleanField(
		verbose_name=u'6.3.	Para la validación de los informes anteriores se realizó en una RAC (pre sectorial).',
		blank=False,
		null=False
	)
	pregunta_3 = models.CharField(
		verbose_name=u'6.4.	En la RAC (pre sectorial) que tipo de comisiones se conformaron.',
		max_length=2,
		blank=False,
		null=False,
		choices=(('in','Institucional'),('a','Académica'),('iv','Investigación'),('ex','Extensión e interacción social'),('P','Postgrado'),('o','Otros'))
	)
	opregunta_3 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_4 = models.IntegerField(
		verbose_name=u'6.5.	El grado de aporte en la RAC (pre sectorial) del sector docente',
		blank=False,
		null=False,
		choices=((3,"Alta"),(2,"Media"),(1,"Baja"))
	)
	pregunta_5 = models.IntegerField(
		verbose_name=u'6.6.	El grado de aporte en la RAC (pre sectorial) del sector estudiantil',
		blank=False,
		null=False,
		choices=((3,"Alta"),(2,"Media"),(1,"Baja"))
	)
	pregunta_6 = models.CharField(
		verbose_name=u'6.7.	Cuáles son las bases en las que se fundamentaron para llevar a cabo la RAC (pre sectoriales)',
		max_length=2,
		blank=False,
		null=False,
		choices=(('n','Normas'),('po','Procesos'),('pi','Principios'),('fo','Fines y objetivos de la Universidad'),('o','Otros'))
	)
	opregunta_6 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_7 = models.CharField(
		verbose_name=u'6.8.	Toda La documentación generada en la RAC (pre sectorial) del se tiene guardada en formato:',
		max_length=2,
		blank=False,
		null=False,
		choices=(("di","Digital en internet"),("dc","Digital en una computadora"),("h","Hojas foliadas"),("nt","No tiene"))
	)
	pregunta_8 = MultiSelectField(
		verbose_name=u'6.9.	Que herramienta digital utilizó para organizar la información en esta etapa.',
		max_choices=4,
		max_length=20,
		blank=False,
		null=False,
		choices=(('b','Computadora'),('c','Celular'),('d','Data Display'),('o','Otros'))
	)
	opregunta_8 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	pregunta_7 = models.CharField(
		verbose_name=u'6.10. Que calificación daría al equipo de gestión curricular en esta etapa.',
		max_length=2,
		blank=False,
		null=False,
		choices=(('b','Bueno'),('o','Oportuno'),('r','Regular'))
	)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.evaluacion_recurricular)

class etapa_7(models.Model):
	evaluacion_recurricular = models.OneToOneField(
		evaluacion_recurricular,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	pregunta_1 = models.BooleanField(
		verbose_name='7.2.	Se cumplió con todos los requisitos para presentar a la Reunión Académica Nacional.',
		blank=False,
		null=False
	)
	pregunta_2 = models.CharField(
		verbose_name=u'7.3.	Las recomendaciones que hizo la Reunión Académica Nacional en su informe fueron.',
		max_length=2,
		blank=False,
		null=False,
		choices=(('a','Aplicados'),('fr','Pospuestos por falta de recursos'),('ne','No tomados en cuenta'),('pc','En proceso de corrección'),('o','Otros'))
	)
	opregunta_2 = models.TextField(
		verbose_name=u'Que Otros?',
		blank=True,
		null=True
	)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.evaluacion_recurricular)

class participantes(models.Model):
	evaluacion_recurricular = models.ForeignKey(
		evaluacion_recurricular,
		on_delete=models.CASCADE,
	)
	nombre = models.CharField(
		max_length=50,
		blank=False,
		null=False,
	)
	apellidos = models.CharField(
		max_length=50,
		blank=False,
		null=False,
	)
	ci = models.PositiveIntegerField(
		blank=False,
		null=False
	)
	estamento = models.CharField(
		max_length=1,
		blank=False,
		null=False,
		choices=(('e','Estudiante'),('d','Docente'))
	)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.ci)