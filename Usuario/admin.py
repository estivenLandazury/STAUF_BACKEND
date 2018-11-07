from django.contrib import admin
from Usuario.models import Usuarios
from Usuario.models import TipoUsuario


# Register your models here.

# Aqui mostrará os modelos agregados    
admin.site.register(Usuarios) 
admin.site.register(TipoUsuario) 
