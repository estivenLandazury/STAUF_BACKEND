# Generated by Django 2.1.1 on 2018-11-05 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_auto_20181105_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppMovil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaRegistro', models.DateField()),
                ('appMovil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.AppMovil')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='appmovil',
            name='usuario_App',
            field=models.ManyToManyField(through='Usuario.Usuario_App', to='Usuario.Usuarios'),
        ),
    ]
