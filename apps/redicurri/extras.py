import datetime
from constance import config

def gestion():
	now = datetime.datetime.now()
	return config.GESTION if (config.GESTION_ACTIVO) else now.year

def eliminar_al_cambiar(pk):
	import apps.redicurri.models as m
	from apps.redicurri.models import evaluacion_recurricular
	pasar = False
	for x in range(1,8):
		res1 = evaluacion_recurricular.objects.get(pk=pk)
		print(res1)
		eta = getattr(m,'etapa_'+str(x))
		com = getattr(res1,'retapa_'+str(x))
		print(eta)
		if not com:
			try:
				resb = eta.objects.get(evaluacion_recurricular=res1)
				print(resb)
				resb.delete()
			except Exception as e:
				pass