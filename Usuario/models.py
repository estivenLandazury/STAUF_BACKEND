from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TIPO_USUARIO = {
    ('1', 'Enfermera Jefe'),
    ('2', 'Vigilante'),
    ('3', 'Coordinadora Jefe'),
    ('4', 'Ambulatorio'),
    ('5', 'Hospitalario'),
    ('6', 'Acompañante'),
    ('7', 'Administrador'),
}


class Usuarios(models.Model):
     # blank se refiere a un tipo del formulario y null a la base de datos
    nombre = models.CharField(max_length=100, blank=True, null=False)
    apellido = models.CharField(max_length=100, blank=True, null=False)
    numeroDocumento = models.CharField(max_length=100, blank=True, null=False)
    user = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE)
    
    encargado = models.ManyToManyField(
        'self', through='Encargado', symmetrical=False)

    def __str__(self):
        cadena = self.nombre+","+self.apellido+","+self.numeroDocumento
        return cadena


class TipoUsuario(models.Model):
    idTipo = models.CharField(max_length=100, primary_key=True)
    nombreRol = models.CharField(max_length=100, blank=False, null=False)
    rolUsuario = models.ManyToManyField(Usuarios, through='RolUsuario')
    
    def __str__(self):
        cadena = self.nombreRol + ","
        return cadena

# Rompimiento de usurio y tipo Usuario


class RolUsuario(models.Model):
    usuario = models.ForeignKey(
        Usuarios, null=False, blank=False, on_delete=models.CASCADE)
    tipoUsuario = models.ForeignKey(
        TipoUsuario, null=False, blank=False, on_delete=models.CASCADE)
    fechaRegistro = models.DateField(auto_now_add=True)

    def __str__(self):
        cadena = self.tipoUsuario+ self.usuario
        return cadena


# Rompimiento de usuario y usuario
class Encargado(models.Model):
    idEncargado = models.ForeignKey(
        Usuarios, related_name='idEncargado', null=False, blank=False, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(
        Usuarios, related_name='idUsuario', null=False, blank=False, on_delete=models.CASCADE)
    fechaIngreso = models.DateField(auto_now_add=True)

    def __str__(self):
        cadena = self.idEncargado + ","+self.idUsuario
        return cadena



class TipoDocumento(models.Model):
    idTipoDocumento = models.CharField(max_length=100, primary_key=True)
    nombreDocumento = models.CharField(max_length=100, blank=False, null=False)
    usuario_Documento = models.ManyToManyField(Usuarios, through='Usuario_Documento')

    def __str__(self):
        cadena = self.idTipoDocumento + "," +self.nombreDocumento
        return cadena

# Rompimiento de Usuario y TioDocumento


class Usuario_Documento(models.Model):
    usuario = models.ForeignKey(
        Usuarios, null=False, blank=False, on_delete=models.CASCADE)
    tipoDocumento = models.ForeignKey(
        TipoDocumento, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        cadena = self.usuario + ","+self.tipoDocumento
        return cadena


class Manilla(models.Model):
    macId = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    manilla_Usuario = models.ManyToManyField(
        Usuarios, through='Manilla_Usuario')

    def __str__(self):
        cadena = self.macId + ","+self.nombre
        return cadena

# Rompimiento entre Usuario y Manilla


class Manilla_Usuario(models.Model):
    usuario = models.ForeignKey(
        Usuarios, null=False, blank=False, on_delete=models.CASCADE)
    manilla = models.ForeignKey(
        Manilla, null=False, blank=False, on_delete=models.CASCADE)
    fechaRegistro = models.DateField(auto_now_add=True)

   
    def __str__(self):
        cadena = self.usuario + ","+self.manilla + "," + self.fechaRegistro
        return cadena


class AppMovil(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    usuario_App = models.ManyToManyField(Usuarios, through='Usuario_App')
    manilla_App = models.ManyToManyField(Manilla, through='Manilla_App')


    def __str__(self):
        cadena = self.nombre
        return cadena


# Rompimiento entre Usuario y AppMovil
class Usuario_App(models.Model):
    usuario = models.ForeignKey(Usuarios, null=False, blank=False, on_delete=models.CASCADE)
    appMovil = models.ForeignKey(AppMovil, null=False, blank=False, on_delete=models.CASCADE)
    fechaRegistro = models.DateField(auto_now_add=True)

    def __str__(self):
        cadena = self.usuario+ ","+self.appMovil+","+self.fechaRegistro
        return cadena


#Rompimiento entre Appmovil y Manilla
class Manilla_App(models.Model):
    appMovil = models.ForeignKey(AppMovil, null=False, blank=False, on_delete=models.CASCADE)
    manilla= models.ForeignKey(Manilla, null=False, blank=False, on_delete=models.CASCADE)
    fechaRegistro = models.DateField(auto_now_add=True)


    def __str__(self):
        cadena = self.appMovil + ","+self.manilla+","+self.fechaRegistro
        return cadena


class Permiso(models.Model):
    nombrePermiso = models.CharField(max_length=100, blank=False, null=False)
    Usuario = models.ManyToManyField(Usuarios, through='Permiso_Usuario')


    def __str__(self):
        cadena = self.nombrePermiso
        return cadena

#Rompimiento entre usuario y Permiso
class Permiso_Usuario(models.Model):
    usuario = models.ForeignKey(Usuarios, null=False, blank=False, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        cadena = self.usuario+ ","+ self.permiso
        return cadena


class Alarma (models.Model):
    fechaRegistro= models.DateField(auto_now_add=True)
    descripcion=models.CharField(max_length=100, blank=True, null=True)
    solucionado= models.BooleanField(default=False)
    appMovil = models.ForeignKey(AppMovil, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        cadena = self.fechaRegistro+ ","+ self.appMovil+ ","+self.solucionado+","+self.descripcion
        return cadena








    















