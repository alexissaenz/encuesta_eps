from django.db import models
from encuesta_eps_app.models.perfil import Perfil
from rest_framework import serializers

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id', 'num_doc', 'ciudad', 'direccion', 'is_admin']