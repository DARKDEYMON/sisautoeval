from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(asignacion_evaluacion, SimpleHistoryAdmin)