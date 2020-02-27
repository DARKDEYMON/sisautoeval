from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(facultad, SimpleHistoryAdmin)
admin.site.register(carrera, SimpleHistoryAdmin)