from django import forms
from django.forms import ModelForm
from .models import *
from material import *

class eval_recurricular_form(ModelForm):
	layout = Layout(
		'genero',
		'situacion',
		'director',
		'f_aprobacion',
		Fieldset('Jornada Académica',
			'jor_etapa',
			'jor_programacion',
			'jor_enfoque',
			'jor_expositor',
			'jor_comprencion',
			'jor_amcomprencion',
			'jor_amprosedimiento',
			'jor_material',
			'jor_hedigital',
			'jor_hedigital_otros',
			
		)
	)
	class Meta:
		model = eval_recurricular
		exclude = ['gestion']