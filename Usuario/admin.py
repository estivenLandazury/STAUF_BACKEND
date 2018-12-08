from django.contrib import admin
from Usuario.models import Usuarios
from Usuario.models import TipoUsuario
from Usuario.models import Alarma

# Aqui mostrará os modelos agregados    
admin.site.register(Usuarios) 
admin.site.register(TipoUsuario)
admin.site.register(Alarma)
