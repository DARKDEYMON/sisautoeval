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
    #etapa3
    path('etapa3cr/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_3_view.as_view())), name='etapa3cr'),
    path('etapa3up/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_3_update_view.as_view())), name='etapa3up'),
    path('etapa3re/<int:pk>/',permission_required('usuarios.rediseño')(login_required(redirec_eval_etapa_3_view)), name='etapa3re'),
    #etapa4
    path('etapa4cr/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_4_view.as_view())), name='etapa4cr'),
    path('etapa4up/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_4_update_view.as_view())), name='etapa4up'),
    path('etapa4re/<int:pk>/',permission_required('usuarios.rediseño')(login_required(redirec_eval_etapa_4_view)), name='etapa4re'),
    #etapa5
    path('etapa5cr/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_5_view.as_view())), name='etapa5cr'),
    path('etapa5up/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_5_update_view.as_view())), name='etapa5up'),
    path('etapa5re/<int:pk>/',permission_required('usuarios.rediseño')(login_required(redirec_eval_etapa_5_view)), name='etapa5re'),
    #etapa6
    path('etapa6cr/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_6_view.as_view())), name='etapa6cr'),
    path('etapa6up/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_6_update_view.as_view())), name='etapa6up'),
    path('etapa6re/<int:pk>/',permission_required('usuarios.rediseño')(login_required(redirec_eval_etapa_6_view)), name='etapa6re'),
    #etapa7
    path('etapa7cr/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_7_view.as_view())), name='etapa7cr'),
    path('etapa7up/<int:pk>/',permission_required('usuarios.rediseño')(login_required(etapa_7_update_view.as_view())), name='etapa7up'),
    path('etapa7re/<int:pk>/',permission_required('usuarios.rediseño')(login_required(redirec_eval_etapa_7_view)), name='etapa7re'),
    
    path('participantes/<int:pk>/',permission_required('usuarios.rediseño')(login_required(participantes_view)), name='participantes')
]
