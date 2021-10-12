from django.db import models
from encuesta_eps_app.models.encuesta import Encuesta
from rest_framework import serializers
from encuesta_eps_app.serializers.perfilSerializer import PerfilSerializer

class EncuestaSerializer(serializers.ModelSerializer):
    #perfil = PerfilSerializer()
    class Meta:
        model = Encuesta
        fields = ['sufrio_covid', 'contacto_persona_covid', 'temperatura_mayor_37', 
        'dificultad_respirar_ult_sem', 'cansado_ult_sem', 'perfil']