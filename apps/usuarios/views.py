from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.urls import reverse_lazy

from django.contrib.postgres.search import SearchVector
from django.db.models import CharField
from django.db.models.functions import Cast

from .forms import *

# Create your views here.
def main_mage(request):
	return render(request,"base/main.html",{})

class create_user_view(CreateView):
	form_class = crear_user_form
	template_name = 'usuarios/crear_usuario.html'
	success_url = reverse_lazy('academico:listausers')

class lista_usuarios_view(ListView):
	model = User
	paginate_by = 10
	form_class = search_form
	template_name = 'usuarios/lista_users.html'
	def get_context_data(self, **kwargs):
		context = super(lista_usuarios_view, self).get_context_data(**kwargs)
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
						Cast('id', CharField()),
						'username',
						'first_name',
						'last_name',
						Cast('email', CharField())
					)
				).filter(
					search=search,
					is_staff=False
				).order_by('id')
		else:
			return self.model.objects.all().filter(is_staff=False).order_by('id')

#estudiar esto
class permisos_view(FormView):
	model = User
	model_permissions = permisos
	form_class = add_permissions_form
	template_name = 'usuarios/permisos.html'
	success_url = reverse_lazy('usuarios:listausers')
	def get_form_kwargs(self):
		kwargs = super(permisos_view, self).get_form_kwargs()
		kwargs['model_permissions'] = self.model_permissions
		return kwargs
	def get_initial(self):
		pk = self.kwargs.get('pk',0)
		self.user = self.model.objects.get(id=pk)
		content_type = ContentType.objects.get_for_model(self.model_permissions)
		permisos_actuales = self.user.user_permissions.filter(content_type=content_type)
		perms = {}
		for p in permisos_actuales:
			perms[p.codename]= True
		return perms
		#return { 'usuarios': True, 'academico': False }
	def form_valid(self, form):
		if form.is_valid():
			data = form.cleaned_data
			for p in data:
				content_type=ContentType.objects.get_for_model(self.model_permissions)
				permission = Permission.objects.get(content_type=content_type, codename=p)
				if data[p]:
					self.user.user_permissions.add(permission)
				else:
					self.user.user_permissions.remove(permission)
		return super().form_valid(form)