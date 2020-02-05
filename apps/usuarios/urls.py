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
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
	path('login/',
		LoginView.as_view(template_name='usuarios/login.html'),
		name='login'
	),
	path('logout/',logout_then_login, name='logout'),
	path('',login_required(main_mage), name="main"),
	path('listausers/',permission_required('usuarios.usuarios')(login_required(lista_usuarios_view.as_view())), name='listausers'),
	path('addpermission/<int:pk>/',permission_required('usuarios.usuarios')(login_required(permisos_view.as_view())), name='addpermission'),
	path('createuser/',permission_required('usuarios.usuarios')(login_required(create_user_view.as_view())), name='createuser'),
]
