from django.db import models
from .perfil import Perfil

class Encuesta(models.Model):
    sufrio_covid = models.BooleanField()
    contacto_persona_covid = models.BooleanField()
    temperatura_mayor_37 = models.BooleanField()
    dificultad_respirar_ult_sem = models.BooleanField()
    cansado_ult_sem = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, related_name='encuesta', on_delete=models.CASCADE)