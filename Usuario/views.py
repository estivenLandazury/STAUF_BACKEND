from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from Usuario.models import Usuarios, TipoUsuario, RolUsuario, Encargado,  TipoDocumento, Usuario_Documento, Manilla, Manilla_Usuario, AppMovil, Usuario_App, Manilla_App, Permiso, Permiso_Usuario, Alarma
from Usuario.serializers import UsuarioSerializer, TipoUsuarioSerializer, RolUsuarioSerializer, UsuarioEncargadoSerializer,  TipoDocumentoSerializer, Usuario_DocumentoSerializer, ManillaSerializer, Manilla_UsuarioSerializer, AppMovilSerializer, Usuario_AppMovilSerializer, Manilla_AppSerializer, Permiso_Serializer, Permiso_UsuarioSerializer, AlarmaSerializer, UserAuthSerializer
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.core import serializers
from django.db.models import Q
from django.utils import timezone
import datetime


# Create your views here.








@api_view(["POST"])
def autenticacion(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        content = {
            "token": token.key,
            "user_id": user.pk,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "email": user.email
        }
        return Response(content, 200)
    return Response("Unable to log in with ", 400)


# Crear cuenta de usuario
@api_view(["POST"])
def createUser(request):
    username = request.data['username']
    password = request.data['password']
    email = request.data['email']

    user = User.objects.create_user(username, email,password)
    
    
    if user is not None:
        user.save()

        content = {
            "user_id": user.pk,
            "username": user.username,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "email": user.email
        }
        return Response(content, 200)
    return Response("Unable to log in with ", 400)





 

#---------------Usuario--------------------------#

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuarios.objects.all()
    lookup_field= 'numeroDocumento'
    lookup_url_kward="numeroDocumento"

class UsuarioDetailId(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuarios.objects.all()
    


#obtiene la lista de usuarios que desempeñan un rol secundario: hospitalario, visitante, acompañante,ambulatorio y encargado
class ObtenerUsuariosPorRolesSecundarios(generics.ListCreateAPIView):
    queryset=Usuarios.objects.filter(Q(rolusuario__tipoUsuario__exact='4')|Q(rolusuario__tipoUsuario__exact='5')
    |Q(rolusuario__tipoUsuario__exact='6') |Q(rolusuario__tipoUsuario__exact='7'))
    serializer_class =UsuarioSerializer

#Obtiene un usuario a partir de su nombre y apellido
class UsuarioLista(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self, *args, **kwargs):
            queryset = Usuarios.objects.all()
            
            param= self.request.GET.get("q")
            param1= self.request.GET.get("l")

            if param:
              queryset= queryset.filter(nombre__exact=param, apellido__exact=param1)
            
            return queryset


# obtiene un usuario a partir del id de la cuenta creada
class ObtenerUsuarioCuenta(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self, *args, **kwargs):
            queryset = Usuarios.objects.all()
            param= self.request.GET.get("q")

            if param:
                queryset= queryset.filter(user__exact=param)
            return queryset


#--------------------------Usuario----------------------------------------


  

#------------Cuentas de usuario---------------
class UserAuthList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer

class obtenerCuentaPorUserName(generics.ListCreateAPIView):
    serializer_class = UserAuthSerializer

    def get_queryset(self, *args, **kwargs):
            queryset = User.objects.all()
            param= self.request.GET.get("q")

            if param:
                queryset=queryset.filter(username__exact=param)
            return queryset


#obtiene la cuenta a partir del nombre de usuario
class UserAuthDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer
    lookup_field= 'username'
    lookup_url_kward="username"
    

#---------------Cuentas de usuario-------------

    


# Usuario encargado----------------------------
class UsuarioEncargadoList(generics.ListCreateAPIView):
    queryset = Encargado.objects.all()
    serializer_class = UsuarioEncargadoSerializer


class UsuarioEncargadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Encargado.objects.all()
    serializer_class = UsuarioEncargadoSerializer


class FiltrarncargadoyFechaActual(generics.ListCreateAPIView):
    serializer_class = UsuarioEncargadoSerializer
    def get_queryset(self, *args, **kwargs):
            queryset = Encargado.objects.all()
            param= self.request.GET.get("q")
            param1= self.request.GET.get("j")

            if param:
                
                queryset= queryset.filter(idEncargado__exact=param,fechaIngreso__exact=param1)
            return queryset



# Usuario encargado----------------------------


# Serialización de la clase tipo Usuario
class TipoUsuerList(generics.ListCreateAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer


class TipoUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer



class FilterTipoUsuarioList(generics.ListCreateAPIView):
    queryset=TipoUsuario.objects.filter(Q(nombreRol__exact='Ambulatorio')|Q(nombreRol__exact='Hospitalario')
    |Q(nombreRol__exact='Acompañante') |Q(nombreRol__exact='Encargado'))
    serializer_class =TipoUsuarioSerializer


   
            
# ---------------------------------------------------------


# Serilaización Rol Usuario----------------------------
class RolUsuerList(generics.ListCreateAPIView):
    # queryset = RolUsuario.objects.filter(tipoUsuario='2')
    queryset = RolUsuario.objects.all()
    serializer_class = RolUsuarioSerializer

#Obtiene el rol del usuario a partir del id del usuario
class RolUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RolUsuario.objects.all()
    serializer_class = RolUsuarioSerializer
    lookup_field= 'usuario'
    lookup_url_kward="usuario"




#obtiene una lista de  roles a partir del id del usuario 
class obtenerRolPorIdUsuario(generics.RetrieveUpdateDestroyAPIView):
   queryset = RolUsuario.objects.all()
   serializer_class = RolUsuarioSerializer

# Serilaización Rol Usuario----------------------------


# Cuenta----------------------------
# class CuentaList(generics.ListCreateAPIView):
 #   queryset = Cuenta.objects.all()
  #  serializer_class = CuentaSerializer


# class CuentaDetail(generics.RetrieveUpdateDestroyAPIView):
   # queryset = Cuenta.objects.all()
   # serializer_class = CuentaSerializer


# Cuenta----------------------------


# TipoDocumento------------------
class TipoDocumentoList(generics.ListCreateAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer


class TipoDocumentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
    

# TipoDocumento------------------

# ------------------UsuarioDocumento---------------------


class UsuarioDocumentoList(generics.ListCreateAPIView):
    queryset = Usuario_Documento.objects.all()
    serializer_class = Usuario_DocumentoSerializer

#Obtiene el usuario documento a partir del id del usuario
class UsuarioDocumentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario_Documento.objects.all()
    serializer_class = Usuario_DocumentoSerializer
    lookup_field= 'usuario'
    lookup_url_kward="usuario"

# --------------------------UsuarioDocumento---------------------


# Manilla----------------------
class ManillaList(generics.ListCreateAPIView):
    queryset = Manilla.objects.all()
    serializer_class = ManillaSerializer


class ManillaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manilla.objects.all()
    serializer_class = ManillaSerializer
    lookup_field= 'macId'
    lookup_url_kward="macId"
   
    
    

 # Manilla----------------------

 # ManillaUsuario----------------------


class ManillaUsuarioList(generics.ListCreateAPIView):
    queryset = Manilla_Usuario.objects.all()
    serializer_class = Manilla_UsuarioSerializer


class ManillaUsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manilla_Usuario.objects.all()
    serializer_class = Manilla_UsuarioSerializer

#filtra la manilla por id de usuario y fecha establecida
class FiltrarManillas(generics.ListCreateAPIView):
    serializer_class = Manilla_UsuarioSerializer
    def get_queryset(self, *args, **kwargs):
            queryset = Manilla_Usuario.objects.all()
            param= self.request.GET.get("q")
            param1= self.request.GET.get("j")

            if param:
                queryset=queryset.filter(usuario__exact=param,fechaRegistro__exact=param1)
            return queryset
    
# ManillaUsuario----------------------


# AppMovil---------------------------
class AppMovilList(generics.ListCreateAPIView):
    queryset = AppMovil.objects.all()
    serializer_class = AppMovilSerializer

#obtiene la aplicación a partir del id
class AppMovilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppMovil.objects.all()
    serializer_class = AppMovilSerializer

class AppMovilDetailName(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppMovil.objects.all()
    serializer_class = AppMovilSerializer
    lookup_field= 'nombre'
    lookup_url_kward="nombre"

   
# AppMovil---------------------------


# UsuarioApp---------------------
class UsuarioAppMovilList(generics.ListCreateAPIView):
    queryset = Usuario_App.objects.all()
    serializer_class = Usuario_AppMovilSerializer

#filtra Usuario_app por id del suaurio
class filtrarUsuaripAppIdusuario(generics.ListCreateAPIView):
    
    serializer_class = Usuario_AppMovilSerializer
    def get_queryset(self, *args, **kwargs):
            queryset =Usuario_App.objects.all()
            param= self.request.GET.get("q")
            param1= self.request.GET.get("j")

            if param:
                queryset=queryset.filter(usuario__exact=param,fechaRegistro__exact=param1 )
            return queryset

#filtra Usuario_app por id de la aplicación
class filtrarUsuarioAppIdApp(generics.ListCreateAPIView):
    
    serializer_class = Usuario_AppMovilSerializer
    def get_queryset(self, *args, **kwargs):
            queryset =Usuario_App.objects.all()
            param= self.request.GET.get("q")
            param1= self.request.GET.get("j")
            if param:
                queryset=queryset.filter(appMovil__exact=param,fechaRegistro__exact=param1 )
            return queryset


class UsuarioAppMovilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario_App.objects.all()
    serializer_class = Usuario_AppMovilSerializer
# UsuarioApp--------------------------


# ManillaApp--------------------------------------
class ManillaAppList(generics.ListCreateAPIView):
    queryset = Manilla_App.objects.all()
    serializer_class = Manilla_AppSerializer


class ManillaAppDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manilla_App.objects.all()
    serializer_class = Manilla_AppSerializer

class FiltrarManillaAppPorIdApp(generics.ListCreateAPIView):
    serializer_class = Manilla_AppSerializer
    def get_queryset(self, *args, **kwargs):
            queryset =Manilla_App.objects.all()
            param= self.request.GET.get("q")
            param1= self.request.GET.get("j")

            if param:
                queryset=queryset.filter(appMovil__exact=param,fechaRegistro__excat=param1 )
            return queryset
    


# ManillaApp--------------------------------------


# Permiso-----------------------------------------
class PermisoList(generics.ListCreateAPIView):
    queryset = Permiso.objects.all()
    serializer_class = Permiso_Serializer


class PermisoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permiso.objects.all()
    serializer_class = Permiso_Serializer

# Permiso----------------------------------


# Permiso Usuario---------------------------
class PermisoUsuarioList(generics.ListCreateAPIView):
    queryset = Permiso_Usuario.objects.all()
    serializer_class = Permiso_UsuarioSerializer


class PermisoUsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permiso_Usuario.objects.all()
    serializer_class = Permiso_UsuarioSerializer

# Permiso Usuario---------------------------


class AlarmaList(generics.ListCreateAPIView):
    queryset = Alarma.objects.all()
    serializer_class = AlarmaSerializer


class AlarmaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alarma.objects.all()
    serializer_class = AlarmaSerializer

class AlarmasFalse(generics.ListCreateAPIView):    
    queryset = Alarma.objects.filter(Q(solucionado=False))
    serializer_class = AlarmaSerializer
    
class AlarmasTrue(generics.ListCreateAPIView):    
    queryset = Alarma.objects.filter(Q(solucionado=True))
    serializer_class = AlarmaSerializer


class AlarmaPorfechayIdApp(generics.ListCreateAPIView):
    serializer_class =  AlarmaSerializer
    def get_queryset(self, *args, **kwargs):
            now=datetime.datetime.now()
            queryset =Alarma.objects.all()
            param= self.request.GET.get("q")

            if param:
                queryset=queryset.filter(appMovil__exact=param,fechaRegistro__exact='django_timezone')
            return queryset
    








