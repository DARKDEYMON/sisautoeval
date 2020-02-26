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
	path('evalredigen/',permission_required('usuarios.academico')(login_required(lista_evaluacionesredigen_view.as_view())), name='evalredigen'),
	path('eractdesac/<int:pk>/',permission_required('usuarios.academico')(login_required(activdesactiv_view.as_view())), name='eractdesac'),
	path('listfacul/',permission_required('usuarios.academico')(login_required(lista_facultada_view.as_view())), name='listfacul'),
	path('faculcre/',permission_required('usuarios.academico')(login_required(facultad_create_view.as_view())), name='faculcre'),
	path('faculup/<int:pk>/',permission_required('usuarios.academico')(login_required(facultad_update_view.as_view())), name='faculup'),
	path('carrelist/',permission_required('usuarios.academico')(login_required(lista_carrera_view.as_view())), name='carrelist'),
	path('carreup/<int:pk>/',permission_required('usuarios.academico')(login_required(carrera_update_view.as_view())), name='carreup'),
]
