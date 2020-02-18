from django.db import models
from constance import config
from django.apps import apps
from apps.redicurri.extras import *

# Create your models here.

class facultad(models.Model):
	nombre = models.CharField(
		max_length=100,
		null=False,
		blank=False
	)
	fecha_fundacion = models.DateField(
		null=False,
		blank=False
	)
	def __str__(self):
		return self.nombre

class carrera(models.Model):
	facultad = models.ForeignKey(facultad, on_delete=models.CASCADE)
	nombre = models.CharField(
		max_length=100,
		null=False,
		blank=False
	)
	fecha_fundacion = models.DateField(
		null=False,
		blank=False
	)
	def aval_pendiente(self):
		if config.ACTIVO_REDIEVAL:
			try:
				evaluacion_recurricular = apps.get_model('redicurri', 'evaluacion_recurricular')
				res = evaluacion_recurricular.objects.get(gestion=gestion())
				if res.activo:
					return True, "La evaluación esta incompleta"
				else:
					return False, "La evaluación concluyo"
			except Exception as e:
				return True, "Tiene Una evaluación pendiente"
		else:
			return False, "Las evaluaciones no están activas aun"
	def __str__(self):
		return self.nombre