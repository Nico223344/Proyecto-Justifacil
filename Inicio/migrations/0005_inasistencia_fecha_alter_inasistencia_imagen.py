# Generated by Django 4.2.3 on 2023-10-24 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0004_alter_inasistencia_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='inasistencia',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='inasistencia',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media/inasistencias'),
        ),
    ]
