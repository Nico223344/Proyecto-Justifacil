# Generated by Django 4.2.3 on 2023-10-23 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inasistencia',
            name='codigo',
        ),
    ]