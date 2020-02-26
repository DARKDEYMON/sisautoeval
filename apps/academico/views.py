from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from apps.redicurri.models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

class lista_evaluacionesredigen_view(ListView):
	model = evaluacion_recurricular
	paginate_by = 10
	form_class = search_form
	template_name = 'academico/eval_redi.html'
	def get_context_data(self, **kwargs):
		context = super(lista_evaluacionesredigen_view, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		if self.request.GET:
			context['form'] = self.form_class(self.request.GET)
			form = self.form_class(self.request.GET)
			if form.is_valid():
				if form.cleaned_data['search']=='':
					context['searchdata'] = None
				else:
					context['searchdata'] = form.cleaned_data['search']
		return context
	def get_queryset(self):
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.annotate(
					search=SearchVector(
						'carrera__nombre',
						Cast('gestion', CharField()),
					)
				).filter(
					search=search,
				).order_by('id')
		else:
			return self.model.objects.all()

class activdesactiv_view(UpdateView):
	model = evaluacion_recurricular
	form_class = activdesactiv_form
	template_name = 'academico/act_desac.html'
	success_url = reverse_lazy('academico:evalredigen')

class facultad_create_view(CreateView):
	form_class = facultad_form
	template_name = 'academico/facultad_create.html'
	success_url = reverse_lazy('academico:listfacul')

class facultad_update_view(UpdateView):
	model = facultad
	form_class = facultad_form
	template_name ='academico/facultad_update.html'
	success_url = reverse_lazy('academico:listfacul')

class lista_facultada_view(ListView):
	model = facultad
	paginate_by = 10
	form_class = search_form
	template_name = 'academico/facultad_list.html'
	def get_context_data(self, **kwargs):
		context = super(lista_facultada_view, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		if self.request.GET:
			context['form'] = self.form_class(self.request.GET)
			form = self.form_class(self.request.GET)
			if form.is_valid():
				if form.cleaned_data['search']=='':
					context['searchdata'] = None
				else:
					context['searchdata'] = form.cleaned_data['search']
		return context
	def get_queryset(self):
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.annotate(
					search=SearchVector(
						'nombre',
						Cast('fecha_fundacion', CharField()),
					)
				).filter(
					search=search,
				).order_by('id')
		else:
			return self.model.objects.all()

class carrera_create_view(CreateView):
	form_class = carrera_form
	template_name = 'academico/carrera_create.html'
	success_url = reverse_lazy('academico:carrelist')

class carrera_update_view(UpdateView):
	model = carrera
	form_class = carrera_form
	template_name ='academico/carrera_update.html'
	success_url = reverse_lazy('academico:carrelist')

class lista_carrera_view(ListView):
	model = carrera
	paginate_by = 10
	form_class = search_form
	template_name = 'academico/carrera_list.html'
	def get_context_data(self, **kwargs):
		context = super(lista_carrera_view, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		if self.request.GET:
			context['form'] = self.form_class(self.request.GET)
			form = self.form_class(self.request.GET)
			if form.is_valid():
				if form.cleaned_data['search']=='':
					context['searchdata'] = None
				else:
					context['searchdata'] = form.cleaned_data['search']
		return context
	def get_queryset(self):
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.annotate(
					search=SearchVector(
						'facultad__nombre'
						'nombre',
						Cast('fecha_fundacion', CharField()),
					)
				).filter(
					search=search,
				).order_by('id')
		else:
			return self.model.objects.all()