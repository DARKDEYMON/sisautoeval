from django import forms
from django.forms import ModelForm
from apps.redicurri.models import *
from .models import *

class search_form(forms.Form):
	search = forms.CharField(required=False, label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))

class activdesactiv_form(ModelForm):
	class Meta:
		model = evaluacion_recurricular
		fields = ['activo']

class facultad_form(ModelForm):
	class Meta:
		model = facultad
		exclude = ['']

class carrera_form(ModelForm):
	def __init__(self,*args,**kwargs):
		super (carrera_form,self ).__init__(*args,**kwargs)
		self.fields['facultad'].widget.attrs = {'class':'js-example-basic-single browser-default'}
	class Meta:
		model = carrera
		exclude = ['']