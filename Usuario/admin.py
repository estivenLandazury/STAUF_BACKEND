from django.contrib import admin
from Usuario.models import Usuarios
from Usuario.models import TipoUsuario
from Usuario.models import Alarma
from Usuario.models import TipoDocumento
from Usuario.models import TipoUsuario
from Usuario.models import Usuario_Documento
from Usuario.models import RolUsuario
from Usuario.models import Manilla
from Usuario.models import Manilla_Usuario
from Usuario.models import Permiso_Usuario
from Usuario.models import Permiso
from Usuario.models import Encargado
from Usuario.models import AppMovil
from Usuario.models import Usuario_App
from Usuario.models import Manilla_App


# Aqui mostrará os modelos agregados    
admin.site.register(Usuarios) 
admin.site.register(TipoUsuario)
admin.site.register(Alarma)
admin.site.register(TipoDocumento)
admin.site.register(Usuario_Documento)
admin.site.register(RolUsuario)
admin.site.register(Manilla)
admin.site.register(Manilla_Usuario)
admin.site.register(Permiso_Usuario)
admin.site.register(Permiso)
admin.site.register(Encargado)
admin.site.register(AppMovil)
admin.site.register(Usuario_App)
admin.site.register(Manilla_App)












