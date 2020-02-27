from django.db import models
from apps.academico.models import *
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from simple_history import register

register(User)
# Create your models here.
class permisos(models.Model):
	class Meta:
		permissions = (
			("usuarios", "Permiso al modulo de usuarios"),
			("academico", "Permiso al modulo academico"),
			("rediseño","Permiso al Modulo de Rediseño C.")
		)

class asignacion_evaluacion(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	carrera = models.ForeignKey(carrera, on_delete=models.CASCADE)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.carrera)
	class Meta:
		unique_together = (('usuario', 'carrera'),)