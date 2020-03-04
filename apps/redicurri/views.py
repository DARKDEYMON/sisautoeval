from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from .forms import *
from .models import *
from apps.academico.models import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.http import Http404

from django.contrib.postgres.search import SearchVector
from django.db.models import CharField
from django.db.models.functions import Cast
from .extras import *
from constance import config

from django.forms import modelformset_factory, inlineformset_factory

# Create your views here. me falta dispachers de control
class eval_evaluacion_recurricular_view(CreateView):
	form_class = eval_evaluacion_recurricular_form
	template_name = 'redicurri/crear_evalredi.html'
	success_url = 'redicurri:evalredicur2'
	#control si no se iso nada - disparador de eliminacion - disparador de cierre de evaluacion - disparador de pertenencia
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(carrera__pk=pk, gestion=gestion())
		except Exception as e:
			raise Http404("ya existe")
		return super(eval_evaluacion_recurricular_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		if form.is_valid():
			form.instance.carrera = carrera.objects.get(pk=self.kwargs['pk'])
			form.instance.usuario = self.request.user
		return super().form_valid(form)
	def get_success_url(self):
		return reverse_lazy(self.success_url,kwargs={'pk':self.object.pk})

class eval_evaluacion_recurricular_update_view(UpdateView):
	model = evaluacion_recurricular
	form_class = eval_evaluacion_recurricular_form
	template_name = 'redicurri/crear_evalredi.html'
	success_url = 'redicurri:evalredicur2'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(eval_evaluacion_recurricular_update_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		return reverse_lazy(self.success_url,kwargs={'pk':self.object.pk})

def redirec_eval_evaluacion_recurricular(request,pk):
	if not config.ACTIVO_REDIEVAL:
		raise Http404("no esta activa la evaluacion al rediseño")
	try:
		res = evaluacion_recurricular.objects.get(carrera__pk=pk, gestion=gestion())
		return HttpResponseRedirect(reverse_lazy('redicurri:evalredicurup',kwargs={'pk':res.pk}))
	except Exception as e:
		return HttpResponseRedirect(reverse_lazy('redicurri:evalredicur',kwargs={'pk':pk}))

class eval_evaluacion_recurricular2_view(UpdateView):
	model = evaluacion_recurricular
	form_class = eval_evaluacion_recurricular_rason_form
	template_name = 'redicurri/crear_evalredi2.html'
	success_url = 'redicurri:etapa1re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		est = eliminar_al_cambiar(self.kwargs['pk'])
		if est:
			return HttpResponseRedirect(self.get_success_url())

		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(eval_evaluacion_recurricular2_view, self).dispatch(request, *args, **kwargs)
	def get_form_kwargs(self):
		kwargs = super(eval_evaluacion_recurricular2_view, self).get_form_kwargs()
		kwargs['evaluacion'] = self.model.objects.get(id=self.kwargs['pk'])
		return kwargs
	def get_success_url(self):
		if(self.object.retapa_1):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.pk})
		else:
			return reverse_lazy(self.success_url2)

#etapa 1
class etapa_1_view(CreateView):
	model_extra = evaluacion_recurricular
	form_class = etapa_1_form
	template_name = 'redicurri/crear_etapa1.html'
	success_url = 'redicurri:etapa2re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_1_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		if form.is_valid():
			form.instance.evaluacion_recurricular = self.model_extra.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_2):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

class etapa_1_update_view(UpdateView):
	model = etapa_1
	form_class = etapa_1_form
	template_name = 'redicurri/crear_etapa1.html'
	success_url = 'redicurri:etapa2re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_1_update_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_2):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

def redirec_eval_etapa_1_view(request,pk):
	if not config.ACTIVO_REDIEVAL:
		raise Http404("no esta activa la evaluacion al rediseño")
	try:
		etapa_1.objects.get(pk=pk)
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa1up',kwargs={'pk':pk}))
	except Exception as e:
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa1cr',kwargs={'pk':pk}))

#etapa 2
class etapa_2_view(CreateView):
	model_extra = evaluacion_recurricular
	form_class = etapa_2_form
	template_name = 'redicurri/crear_etapa2.html'
	success_url = 'redicurri:etapa3re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_2_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		if form.is_valid():
			form.instance.evaluacion_recurricular = self.model_extra.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_3):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

class etapa_2_update_view(UpdateView):
	model = etapa_2
	form_class = etapa_2_form
	template_name = 'redicurri/crear_etapa2.html'
	success_url = 'redicurri:etapa3re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_2_update_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_3):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

def redirec_eval_etapa_2_view(request,pk):
	if not config.ACTIVO_REDIEVAL:
		raise Http404("no esta activa la evaluacion al rediseño")
	try:
		etapa_2.objects.get(pk=pk)
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa2up',kwargs={'pk':pk}))
	except Exception as e:
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa2cr',kwargs={'pk':pk}))

#etapa 3
class etapa_3_view(CreateView):
	model_extra = evaluacion_recurricular
	form_class = etapa_3_form
	template_name = 'redicurri/crear_etapa3.html'
	success_url = 'redicurri:etapa4re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_3_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		if form.is_valid():
			form.instance.evaluacion_recurricular = self.model_extra.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_4):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

class etapa_3_update_view(UpdateView):
	model = etapa_3
	form_class = etapa_3_form
	template_name = 'redicurri/crear_etapa3.html'
	success_url = 'redicurri:etapa4re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_3_update_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_4):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

def redirec_eval_etapa_3_view(request,pk):
	if not config.ACTIVO_REDIEVAL:
		raise Http404("no esta activa la evaluacion al rediseño")
	try:
		etapa_3.objects.get(pk=pk)
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa3up',kwargs={'pk':pk}))
	except Exception as e:
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa3cr',kwargs={'pk':pk}))

#etapa 4
class etapa_4_view(CreateView):
	model_extra = evaluacion_recurricular
	form_class = etapa_4_form
	template_name = 'redicurri/crear_etapa4.html'
	success_url = 'redicurri:etapa5re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_4_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		if form.is_valid():
			form.instance.evaluacion_recurricular = self.model_extra.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_5):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

class etapa_4_update_view(UpdateView):
	model = etapa_4
	form_class = etapa_4_form
	template_name = 'redicurri/crear_etapa4.html'
	success_url = 'redicurri:etapa5re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_4_update_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_5):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

def redirec_eval_etapa_4_view(request,pk):
	if not config.ACTIVO_REDIEVAL:
		raise Http404("no esta activa la evaluacion al rediseño")
	try:
		etapa_4.objects.get(pk=pk)
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa4up',kwargs={'pk':pk}))
	except Exception as e:
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa4cr',kwargs={'pk':pk}))

#etapa5
class etapa_5_view(CreateView):
	model_extra = evaluacion_recurricular
	form_class = etapa_5_form
	template_name = 'redicurri/crear_etapa5.html'
	success_url = 'redicurri:etapa6re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_5_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		if form.is_valid():
			form.instance.evaluacion_recurricular = self.model_extra.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_6):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

class etapa_5_update_view(UpdateView):
	model = etapa_5
	form_class = etapa_5_form
	template_name = 'redicurri/crear_etapa5.html'
	success_url = 'redicurri:etapa6re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_5_update_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_6):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

def redirec_eval_etapa_5_view(request,pk):
	if not config.ACTIVO_REDIEVAL:
		raise Http404("no esta activa la evaluacion al rediseño")
	try:
		etapa_5.objects.get(pk=pk)
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa5up',kwargs={'pk':pk}))
	except Exception as e:
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa5cr',kwargs={'pk':pk}))

#etapa6
class etapa_6_view(CreateView):
	model_extra = evaluacion_recurricular
	form_class = etapa_6_form
	template_name = 'redicurri/crear_etapa6.html'
	success_url = 'redicurri:etapa7re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_6_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		if form.is_valid():
			form.instance.evaluacion_recurricular = self.model_extra.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_7):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

class etapa_6_update_view(UpdateView):
	model = etapa_6
	form_class = etapa_6_form
	template_name = 'redicurri/crear_etapa6.html'
	success_url = 'redicurri:etapa7re'
	success_url2 = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_6_update_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		if(self.object.evaluacion_recurricular.retapa_7):
			return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})
		else:
			return reverse_lazy(self.success_url2)

def redirec_eval_etapa_6_view(request,pk):
	if not config.ACTIVO_REDIEVAL:
		raise Http404("no esta activa la evaluacion al rediseño")
	try:
		etapa_6.objects.get(pk=pk)
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa6up',kwargs={'pk':pk}))
	except Exception as e:
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa6cr',kwargs={'pk':pk}))

#etapa7
class etapa_7_view(CreateView):
	model_extra = evaluacion_recurricular
	form_class = etapa_7_form
	template_name = 'redicurri/crear_etapa7.html'
	success_url = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_7_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		if form.is_valid():
			form.instance.evaluacion_recurricular = self.model_extra.objects.get(pk=self.kwargs['pk'])
		return super().form_valid(form)
	def get_success_url(self):
		return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})

class etapa_7_update_view(UpdateView):
	model = etapa_7
	form_class = etapa_7_form
	template_name = 'redicurri/crear_etapa7.html'
	success_url = 'redicurri:participantes'
	def dispatch(self, request, *args, **kwargs):
		if not config.ACTIVO_REDIEVAL:
			raise Http404("no esta activa la evaluacion al rediseño")
		try:
			evaluacion_recurricular.objects.get(pk=self.kwargs['pk'],activo=True)
		except Exception as e:
			raise Http404("La evaluaciuon esta deasactivada")
		return super(etapa_7_update_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		return reverse_lazy(self.success_url,kwargs={'pk':self.object.evaluacion_recurricular.pk})

def redirec_eval_etapa_7_view(request,pk):
	if not config.ACTIVO_REDIEVAL:
		raise Http404("no esta activa la evaluacion al rediseño")
	try:
		etapa_7.objects.get(pk=pk)
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa7up',kwargs={'pk':pk}))
	except Exception as e:
		return HttpResponseRedirect(reverse_lazy('redicurri:etapa7cr',kwargs={'pk':pk}))

class lista_evaluacionesredi_view(ListView):
	model = evaluacion_recurricular
	paginate_by = 10
	form_class = search_form
	template_name = 'redicurri/lista_evalredi.html'
	def get_context_data(self, **kwargs):
		context = super(lista_evaluacionesredi_view, self).get_context_data(**kwargs)
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
					carrera__asignacion_evaluacion__usuario=self.request.user
				).order_by('id')
		else:
			return self.model.objects.filter(carrera__asignacion_evaluacion__usuario=self.request.user)

class lista_carreras_view(ListView):
	model = carrera
	paginate_by = 10
	form_class = search_form
	template_name = 'redicurri/lista_carrera.html'
	def get_context_data(self, **kwargs):
		context = super(lista_carreras_view, self).get_context_data(**kwargs)
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
					asignacion_evaluacion__usuario=self.request.user
				).order_by('id')
		else:
			return self.model.objects.filter(asignacion_evaluacion__usuario=self.request.user)


def participantes_view(request, pk):
	if not config.ACTIVO_REDIEVAL:
		raise Http404("no esta activa la evaluacion al rediseño")
	try:
		eval_redi = evaluacion_recurricular.objects.get(pk=pk,activo=True)
	except Exception as e:
		raise Http404("La evaluaciuon esta deasactivada")
	part_fomset = participantes_inline_form#inlineformset_factory(evaluacion_recurricular,participantes, exclude=(('evaluacion_recurricular'),), can_delete=True, extra=2)
	if request.method  == 'POST':
		print(request.POST)
		formset = part_fomset(request.POST,instance=eval_redi)
		if(formset.is_valid()):
			formset.save()
			if 'envio' in request.POST:
				return HttpResponseRedirect(reverse_lazy('redicurri:participantes',kwargs={'pk':pk}))
			else:
				eval_redi.activo = False
				eval_redi.save()
				return HttpResponseRedirect(reverse_lazy('redicurri:carrerasredi'))
	formset = part_fomset(instance=eval_redi)
	return render(request, 'redicurri/participantes.html',{'formset':formset})
"""
class participantes2_view(CreateView):
	model = evaluacion_recurricular
	template_name = 'redicurri/participantes.html'
	form_class = participantes_inline_form
	success_url = '/'
	success_url2 = 'redicurri:participantes'
	def get_context_data(self, **kwargs):
		context = super(participantes2_view, self).get_context_data(**kwargs)
		eval_redi = evaluacion_recurricular.objects.get(id=self.kwargs['pk'])
		if self.request.POST:
			context['formset'] = self.form_class(self.request.POST,instance=eval_redi)
		else:
			context['formset'] = self.form_class(instance=eval_redi)
		return context
	def form_valid(self, form):
		context = self.get_context_data()
		print(form)
		if form.is_valid():
			print(form)
		return super(participantes2_view).form_valid(form)
"""