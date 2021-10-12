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

    def update(self, instance, validated_data):
        perfil_data = validated_data.pop('perfil')

        perfil = Perfil.objects.get(user=instance.id)

        perfil.ciudad = perfil_data.get('ciudad', perfil.ciudad)
        perfil.direccion = perfil_data.get('direccion', perfil.direccion)
        perfil.save()
        
        return instance

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
