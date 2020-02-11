from django.db import models

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
	def __str__(self):
		return self.nombre