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


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer


class UserAuthList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer


# Usuario encargado----------------------------
class UsuarioEncargadoList(generics.ListCreateAPIView):
    queryset = Encargado.objects.all()
    serializer_class = UsuarioEncargadoSerializer


class UsuarioEncargadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Encargado.objects.all()
    serializer_class = UsuarioEncargadoSerializer
# Usuario encargado----------------------------


# Serialización de la clase tipo Usuario
class TipoUsuerList(generics.ListCreateAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer


class TipoUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer
# ---------------------------------------------------------


# Serilaización Rol Usuario----------------------------
class RolUsuerList(generics.ListCreateAPIView):
    #queryset = RolUsuario.objects.filter(tipoUsuario='2')
    queryset = RolUsuario.objects.all()
    serializer_class = RolUsuarioSerializer


class RolUserDetail(generics.RetrieveUpdateDestroyAPIView):
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

# UsuarioDocumento---------------------


class UsuarioDocumentoList(generics.ListCreateAPIView):
    queryset = Usuario_Documento.objects.all()
    serializer_class = Usuario_DocumentoSerializer


class UsuarioDocumentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario_Documento.objects.all()
    serializer_class = Usuario_DocumentoSerializer

# UsuarioDocumento---------------------


# Manilla----------------------
class ManillaList(generics.ListCreateAPIView):
    queryset = Manilla.objects.all()
    serializer_class = ManillaSerializer


class ManillaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manilla.objects.all()
    serializer_class = ManillaSerializer

 # Manilla----------------------

 # ManillaUsuario----------------------


class ManillaUsuarioList(generics.ListCreateAPIView):
    queryset = Manilla_Usuario.objects.all()
    serializer_class = Manilla_UsuarioSerializer


class ManillaUsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manilla_Usuario.objects.all()
    serializer_class = Manilla_UsuarioSerializer
# ManillaUsuario----------------------


# AppMovil---------------------------
class AppMovilList(generics.ListCreateAPIView):
    queryset = AppMovil.objects.all()
    serializer_class = AppMovilSerializer


class AppMovilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppMovil.objects.all()
    serializer_class = AppMovilSerializer
# AppMovil---------------------------


# UsuarioApp---------------------
class UsuarioAppMovilList(generics.ListCreateAPIView):
    queryset = Usuario_App.objects.all()
    serializer_class = Usuario_AppMovilSerializer


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
