from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(evaluacion_recurricular, SimpleHistoryAdmin)
admin.site.register(etapa_1, SimpleHistoryAdmin)
admin.site.register(etapa_2, SimpleHistoryAdmin)
admin.site.register(etapa_3, SimpleHistoryAdmin)
admin.site.register(etapa_4, SimpleHistoryAdmin)
admin.site.register(etapa_5, SimpleHistoryAdmin)
admin.site.register(etapa_6, SimpleHistoryAdmin)
admin.site.register(etapa_7, SimpleHistoryAdmin)