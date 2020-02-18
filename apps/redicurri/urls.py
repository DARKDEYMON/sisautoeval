"""sisautoeval URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import *

urlpatterns = [
	path('evalredicur/<int:pk>/',permission_required('usuarios.rediseño')(login_required(eval_evaluacion_recurricular_view.as_view())), name='evalredicur'),
    path('evalredicurup/<int:pk>/',permission_required('usuarios.rediseño')(login_required(eval_evaluacion_recurricular_update_view.as_view())), name='evalredicurup'),
    path('evalredicu/<int:pk>/',permission_required('usuarios.rediseño')(login_required(redirec_eval_evaluacion_recurricular)), name='evalredicu'),
	path('listevalredi/',permission_required('usuarios.rediseño')(login_required(lista_evaluacionesredi_view.as_view())), name='listevalredi'),
	path('carrerasredi/',permission_required('usuarios.rediseño')(login_required(lista_carreras_view.as_view())), name='carrerasredi'),
    #segunda parte
    path('evalredicur2/<int:pk>/',permission_required('usuarios.rediseño')(login_required(eval_evaluacion_recurricular2_view.as_view())), name='evalredicur2'),
    #etapa1
    path('etapa1cr/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_1_view.as_view())), name='etapa1cr'),
    path('etapa1up/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_1_update_view.as_view())), name='etapa1up'),
    path('etapa1re/<int:pk>/',permission_required('usuarios.rediseño')(login_required(redirec_eval_etapa_1_view)), name='etapa1re'),
    #etapa2
    path('etapa2cr/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_2_view.as_view())), name='etapa2cr'),
    path('etapa2up/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_2_update_view.as_view())), name='etapa2up'),
    path('etapa2re/<int:pk>/',permission_required('usuarios.rediseño')(login_required(redirec_eval_etapa_2_view)), name='etapa2re'),
 
]
