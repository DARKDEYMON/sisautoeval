from django.db import models
from apps.academico.models import *
import datetime

def gestion():
	now = datetime.datetime.now()
	return now.year

# Create your models here.
class eval_recurricular(models.Model):
	gestion = models.IntegerField(
		verbose_name=u'Gestion',
		null=False,
		blank=False,
		default=gestion
	)
	genero = models.CharField(
		verbose_name=u'Genero',
		max_length=1,
		null=False,
		blank=False,
		choices= (('m','Masculino'),('f','Femenino'))
	)
	situacion = models.CharField(
		verbose_name=u'Cuál es la situación laboral en la que se encuentra en la universidad?. Elija una opción',
		max_length=2,
		null=False,
		blank=False,
		choices= (('di','Director'),('do','Docente'),('es','Estudiante'))
	)
	director = models.CharField(
		verbose_name=u'Aplicar en caso de que la respuesta sea Director.',
		max_length=2,
		null=True,
		blank=True,
		choices=(('t','Titular'),('ai','A ínterin'))
	)
	f_aprobacion = models.DateField(
		verbose_name=u'Indique en qué fecha se aprobó el actual diseño curricular que está aplicando la carrera (RAN)',
		null=False,
		blank=False
	)
	#jornada academica
	jor_etapa = models.BooleanField(
		verbose_name=u'La carrera realizó esta etapa?.',
		blank=False,
		null=False,
	)
	jor_programacion = models.BooleanField(
		verbose_name=u'1.1. El Departamento de Gestión Curricular, programó con anticipación la jornada académica, cumpliendo con las etapas requeridas',
		blank=True,
		null=False
	)
	jor_enfoque = models.CharField(
		verbose_name=u'1.2. Qué tipo de enfoque es el que se utilizó para el rediseño curricular. Elija una opción:',
		max_length=3,
		blank=True,
		null=True,
		choices=(('fbc','Formación Basada en competencias'),('ob','Por Objetivos'),('o','Otros (Ecléctico)'))
	)
	jor_expositor = models.BooleanField(
		verbose_name=u'1.3.	Se realizaron exposiciones para la comprensión del proceso de rediseño curricular?.',
		blank=True,
		null=False
	)
	jor_comprencion = models.CharField(
		verbose_name=u'1.4.	¿La comprensión de la exposición de las etapas metodológicas del rediseño curricular fue? Elija una opción:',
		max_length=2,
		blank=True,
		null=False,
		choices=(('bu','Buena'),('ra','Razonable'),('re','Regular'),('de','Deficiente'))
	)
	jor_amcomprencion = models.CharField(
		verbose_name=u'1.4.1. Qué grado de comprensión se tuvo del enfoque para el rediseño curricular. Elija una opción',
		max_length=2,
		blank=True,
		null=True,
		choices=(('ex','Excelente'),('bu','Buena'),('ra','Razonable'),('re','Regular'),('de','Deficiente'))
	)
	jor_amprosedimiento = models.CharField(
		verbose_name=u'1.4.2. Usted cree que el procedimiento empleado en el trabajo es. Elija una opción:',
		max_length=2,
		blank=True,
		null=True,
		choices=(('ex','Excelente'),('bu','Buena'),('ra','Razonable'),('re','Regular'),('de','Deficiente'))
	)
	jor_material = models.BooleanField(
		verbose_name=u'1.5.	Fue entregado por el Departamento de Gestión curricular, el material de apoyo o consulta?.',
		blank=True,
		null=False,
	)
	jor_hedigital = models.CharField(
		verbose_name=u'1.6.	Que herramienta digital utilizó para organizar la información en esta etapa?. Puede elegir varias opciones:',
		max_length=2,
		blank=True,
		null=True,
		choices=(('co','Computadora'),('ce','Celular'),('da','Data Display'),('o','Otros'))
	)
	jor_hedigital_otros = models.TextField(
		verbose_name=u'Que Otros? mencione',
		blank=True,
		null=True
	)
	def __str__(self):
		return str(self.gestion)

class evaluacion_recurricular(models.Model):
	carrera = models.ForeignKey(carrera, on_delete=models.CASCADE)
	gestion = models.IntegerField(
		verbose_name=u'Gestion',
		null=False,
		blank=False,
		default=gestion
	)
	genero = models.CharField(
		verbose_name=u'Genero',
		max_length=1,
		null=False,
		blank=False,
		choices= (('m','Masculino'),('f','Femenino'))
	)
	situacion = models.CharField(
		verbose_name=u'Cuál es la situación laboral en la que se encuentra en la universidad?. Elija una opción',
		max_length=2,
		null=False,
		blank=False,
		choices= (('di','Director'),('do','Docente'),('es','Estudiante'))
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
	netapa_1 = models.CharField(
		verbose_name=u'Porque no realizó esta etapa?',
		max_length=2,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'))
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
	netapa_2 = models.CharField(
		verbose_name=u'Porque no realizó esta etapa?',
		max_length=2,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'))
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
	netapa_3 = models.CharField(
		verbose_name=u'Porque no realizó esta etapa?',
		max_length=2,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'))
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
	netapa_4 = models.CharField(
		verbose_name=u'Porque no realizó esta etapa?',
		max_length=2,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'))
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
	netapa_5 = models.CharField(
		verbose_name=u'Porque no realizó esta etapa?',
		max_length=2,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'))
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
	netapa_6 = models.CharField(
		verbose_name=u'Porque no realizó esta etapa?',
		max_length=2,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'))
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
	netapa_7 = models.CharField(
		verbose_name=u'Porque no realizó esta etapa?',
		max_length=2,
		blank=True,
		null=True,
		choices=(('fc','Falta de compromiso de los estamentos'),('nc','No se pudo conformar la comisión'),('fr','Falta de recursos '),('fa','Falta de asesoramiento técnico'))
	)
	oetapa_7 = models.TextField(
		verbose_name=u'Cuales otros?',
		blank=True,
		null=True
	)
	def __str__(self):
		return str(self.gestion)