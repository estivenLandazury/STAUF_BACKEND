# Generated by Django 2.1.1 on 2018-11-13 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('solucionado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AppMovil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manilla',
            fields=[
                ('macId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manilla_App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
                ('appMovil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.AppMovil')),
                ('manilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Manilla')),
            ],
        ),
        migrations.CreateModel(
            name='Manilla_Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
                ('manilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Manilla')),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePermiso', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso_Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='RolUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('idTipoDocumento', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombreDocumento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('idTipo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombreRol', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
                ('appMovil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.AppMovil')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.TipoDocumento')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroDocumento', models.CharField(blank=True, max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('encargado', models.ManyToManyField(through='Usuario.Encargado', to='Usuario.Usuarios')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usuario_documento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='usuario_app',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='rolUsuario',
            field=models.ManyToManyField(through='Usuario.RolUsuario', to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='tipodocumento',
            name='usuario_Documento',
            field=models.ManyToManyField(through='Usuario.Usuario_Documento', to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='rolusuario',
            name='tipoUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.TipoUsuario'),
        ),
        migrations.AddField(
            model_name='rolusuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='permiso_usuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='permiso',
            name='Usuario',
            field=models.ManyToManyField(through='Usuario.Permiso_Usuario', to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='manilla_usuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='manilla',
            name='manilla_Usuario',
            field=models.ManyToManyField(through='Usuario.Manilla_Usuario', to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='encargado',
            name='idEncargado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idEncargado', to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='encargado',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idUsuario', to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='appmovil',
            name='manilla_App',
            field=models.ManyToManyField(through='Usuario.Manilla_App', to='Usuario.Manilla'),
        ),
        migrations.AddField(
            model_name='appmovil',
            name='usuario_App',
            field=models.ManyToManyField(through='Usuario.Usuario_App', to='Usuario.Usuarios'),
        ),
        migrations.AddField(
            model_name='alarma',
            name='appMovil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.AppMovil'),
        ),
    ]
