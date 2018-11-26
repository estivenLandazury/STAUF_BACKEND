##Clase serializabele qe pone en formato JSON cada uno de los atributos de las clases de nuestro modelo
from rest_framework import serializers
from django.contrib.auth.models import User

from Usuario.models import Usuarios,TipoUsuario, RolUsuario,Encargado,TipoDocumento,Usuario_Documento,Manilla,Manilla_Usuario,AppMovil,Usuario_App,Manilla_App,Permiso,Permiso_Usuario,Alarma


#API que representa la cuanta de usuario 
class UserAuthSerializer(serializers.ModelSerializer):
       class Meta:
        model= User
        fields = ('id','username', 'email','password')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuarios
        fields =('id','nombre', 'apellido','numeroDocumento','fechaNacimiento', 'user','encargado')


class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= TipoUsuario
        fields =('idTipo','nombreRol','rolUsuario')


class RolUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= RolUsuario
        fields =('usuario','tipoUsuario','fechaRegistro')

class UsuarioEncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Encargado
        fields =('idEncargado','idUsuario','fechaIngreso')



class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model= TipoDocumento
        fields =('idTipoDocumento','nombreDocumento','usuario_Documento')

class Usuario_DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario_Documento
        fields =('usuario','tipoDocumento', 'id')

class ManillaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manilla
        fields =('macId','nombre','manilla_Usuario')


class Manilla_UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manilla_Usuario
        fields =('usuario','manilla','fechaRegistro')


class AppMovilSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppMovil
        fields =('nombre','usuario_App')

class Usuario_AppMovilSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario_App
        fields =('usuario','appMovil', 'fechaRegistro')


class Manilla_AppSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manilla_App
        fields =('appMovil','manilla','fechaRegistro')

class Permiso_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Permiso
        fields =('id','nombrePermiso','Usuario')


class Permiso_UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permiso_Usuario
        fields =('id','usuario','permiso')


class AlarmaSerializer(serializers.ModelSerializer):
     class Meta:
        model=Alarma
        fields =('id','fechaRegistro','appMovil','solucionado','descripcion')



       


