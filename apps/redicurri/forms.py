from django import forms
from django.forms import ModelForm
from .models import *
from material import *

class eval_evaluacion_recurricular_form(ModelForm):
	class Meta:
		model = evaluacion_recurricular
		exclude = [
			'carrera',
			'gestion',
			'netapa_1',
			'oetapa_1',
			'netapa_2',
			'oetapa_2',
			'netapa_3',
			'oetapa_3',
			'netapa_4',
			'oetapa_4',
			'netapa_5',
			'oetapa_5',
			'netapa_6',
			'oetapa_6',
			'netapa_7',
			'oetapa_7',
			'activo'
		]

class eval_evaluacion_recurricular_rason_form(ModelForm):
	class Meta:
		model = evaluacion_recurricular
		fields = [
			'netapa_1',
			'oetapa_1',
			'netapa_2',
			'oetapa_2',
			'netapa_3',
			'oetapa_3',
			'netapa_4',
			'oetapa_4',
			'netapa_5',
			'oetapa_5',
			'netapa_6',
			'oetapa_6',
			'netapa_7',
			'oetapa_7',
		]
	def __init__(self, *args, **kwargs):
		evaluacion = kwargs.pop('evaluacion',None)
		super(eval_evaluacion_recurricular_rason_form, self).__init__(*args, **kwargs)
		for x in range(1,8):
			fun = getattr(evaluacion,'retapa_'+str(x))
			if not fun:
				self.fields['netapa_'+str(x)].required = True
				#self.fields['oetapa_'+str(x)].required = True
			else:
				self.fields.pop('netapa_'+str(x))
				self.fields.pop('oetapa_'+str(x))

class etapa_1_form(ModelForm):
	class Meta:
		model = etapa_1
		exclude = ['evaluacion_recurricular']

class etapa_2_form(ModelForm):
	class Meta:
		model = etapa_2
		exclude = ['evaluacion_recurricular']

class etapa_3_form(ModelForm):
	class Meta:
		model = etapa_3
		exclude = ['evaluacion_recurricular']

class etapa_4_form(ModelForm):
	class Meta:
		model = etapa_4
		exclude = ['evaluacion_recurricular']

class etapa_5_form(ModelForm):
	class Meta:
		model = etapa_5
		exclude = ['evaluacion_recurricular']

class etapa_6_form(ModelForm):
	class Meta:
		model = etapa_6
		exclude = ['evaluacion_recurricular']

class etapa_7_form(ModelForm):
	class Meta:
		model = etapa_7
		exclude = ['evaluacion_recurricular']

class search_form(forms.Form):
	search = forms.CharField(required=False, label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))
