from django.contrib import admin

from .models.user import User
from .models.perfil import Perfil
from .models.encuesta import Encuesta

admin.site.register(User)
admin.site.register(Perfil)
admin.site.register(Encuesta)


