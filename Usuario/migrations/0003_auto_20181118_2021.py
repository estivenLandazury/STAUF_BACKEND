# Generated by Django 2.1.1 on 2018-11-19 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_auto_20181118_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='apellido',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
