from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class eval_recurricular_view(CreateView):
	form_class = eval_recurricular_form
	template_name = 'redicurri/crear_eval.html'
	success_url = '/'

class eval_eval_evaluacion_recurricular_view(CreateView):
	form_class = eval_evaluacion_recurricular_form
	template_name = 'redicurri/crear_evalredi.html'
	success_url = '/'