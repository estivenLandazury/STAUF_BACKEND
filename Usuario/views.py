from django.shortcuts import render
from rest_framework import generics
from Usuario.models import Usuarios
from Usuario.serializers import UsuarioSerializer
from django.shortcuts import get_object_or_404

# Create your views here.


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer
        


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer
