# Generated by Django 3.0.3 on 2020-02-12 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_asignacion_evaluacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permisos',
            options={'permissions': (('usuarios', 'Permiso al modulo de usuarios'), ('academico', 'Permiso al modulo academico'), ('rediseño', 'Permiso al Modulo de Rediseño C.'))},
        ),
    ]