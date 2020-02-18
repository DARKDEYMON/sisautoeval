from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from constance import config

class crear_user_form(UserCreationForm):
	class Meta:
		model=User
		fields=[
			'username',
			'first_name',
			'last_name',
			'email'
		]
	def __init__(self, *args, **kwargs):
		super(crear_user_form, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True

class search_form(forms.Form):
	search = forms.CharField(required=False, label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))

class add_permissions_form(forms.Form):
	def __init__(self, *args, **kwargs):
		#esto permite aderir datos al constructor dinamicamente deste arg y kwargs
		model_permissions = kwargs.pop('model_permissions', None)
		showd_permissions = kwargs.pop('showd_permissions', False)
		super(add_permissions_form, self).__init__(*args, **kwargs)
		content_type=ContentType.objects.get_for_model(model_permissions)
		permission = Permission.objects.filter(content_type=content_type).order_by('id')
		for idx, p in enumerate(permission):
			if(showd_permissions):
				self.fields[p.codename] = forms.BooleanField(label='Dar permiso para el modulo '+ p.codename, required=False)
			else:
				if(idx>3):
					self.fields[p.codename] = forms.BooleanField(label='Dar permiso para el modulo '+ p.codename, required=False)

class asignar_evaluacion_form(ModelForm):
	def __init__(self,*args,**kwargs):
		super (asignar_evaluacion_form,self ).__init__(*args,**kwargs)
		self.fields['carrera'].widget.attrs = {'class':'js-example-basic-single browser-default'}
	class Meta:
		model = asignacion_evaluacion
		exclude = ['usuario']

class configuracion_general_form(forms.Form):
	gestion = forms.IntegerField(required=True,min_value=1999,max_value=3000,initial=lambda:config.GESTION,label='Gestión de activación manual para la evaluación')
	activada_gestion_manual = forms.BooleanField(initial=lambda:config.GESTION_ACTIVO,required=False,label='Activar/desactivar Gestión/periodo manual para la evaluación')
	activar_eval_redi = forms.BooleanField(initial=lambda:config.ACTIVO_REDIEVAL,required=False,label='Activar evaluacion al rediseño curricular')

	def save(self):
		ges = self.cleaned_data['gestion']
		config.GESTION = ges

		activo = self.cleaned_data['activada_gestion_manual']
		config.GESTION_ACTIVO = activo

		rediact = self.cleaned_data['activar_eval_redi']
		config.ACTIVO_REDIEVAL = rediact

		return