from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from encuesta_eps_app.models.encuesta import Encuesta
from encuesta_eps_app.models.user import User
from encuesta_eps_app.serializers.encuestaSerializer import EncuestaSerializer
from django.http import Http404
from rest_framework.views import APIView

class EncuestaDetailView(APIView):
    #permission_classes = (IsAuthenticated,)
    
    def get_object(self, pk):
        try:
            return Encuesta.objects.get(id=pk)
        except Encuesta.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):

        
        obj = self.get_object(pk)
        
        serializer = EncuestaSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = EncuestaSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        if request.user.perfil.get().id != obj.perfil.id:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)