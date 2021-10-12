from rest_framework import status, views
from rest_framework.response import Response

from encuesta_eps_app.serializers.encuestaSerializer import EncuestaSerializer


class EncuestaCreateView(views.APIView):
    def post(self, request):
        serializer = EncuestaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)