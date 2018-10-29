from django.db import models

# Create your models here.


class Usuarios(models.Model):
     # blank se refiere a un tipo del formulario y null a la base de datos
    Identificador = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=False)
    apellido = models.CharField(max_length=100, blank=True, null=False)

    def __str__(self):
        cadena = self.nombre + "," + self.apellido
        return cadena
