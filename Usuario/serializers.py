##Clase serializabele qe pone en formato JSON cada uno de los atributos de las clases de nuestro modelo
from rest_framework import serializers

from Usuario.models import Usuarios

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Usuarios
        fields =('Identificador','nombre', 'apellido')
       


