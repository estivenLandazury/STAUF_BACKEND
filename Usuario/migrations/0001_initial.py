# Generated by Django 2.1.1 on 2018-09-24 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('Identificador', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
