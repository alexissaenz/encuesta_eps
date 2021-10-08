from rest_framework.settings import perform_import
from encuesta_eps_app.models.user import User
from encuesta_eps_app.models.perfil import Perfil
from rest_framework import serializers
from encuesta_eps_app.serializers.perfilSerializer import PerfilSerializer


class UserSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'email', 'perfil']

    def create(self, validated_data):
        perfilData = validated_data.pop('perfil')
        userInstance = User.objects.create(**validated_data)
        Perfil.objects.create(user=userInstance, **perfilData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        perfil = Perfil.objects.get(user=obj.id)
        return {
            'id': user.id, 
            'username': user.username, 
            'name': user.name, 
            'email': user.email, 
            'perfil': {
                'id': perfil.id,
                'numDoc': perfil.num_doc, 
                'ciudad': perfil.ciudad, 
                'direccion': perfil.direccion,
                'isAdmin': perfil.is_admin
            }
        }
