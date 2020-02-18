# Generated by Django 3.0.3 on 2020-02-18 12:38

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('redicurri', '0005_auto_20200218_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa_1',
            name='pregunta_6',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('b', 'Computadora'), ('c', 'Celular'), ('d', 'Data Display'), ('o', 'Otros')], max_length=20, verbose_name='1.6.\tQue herramienta digital utilizó para organizar la información en esta etapa. Puede elegir varias opciones:'),
        ),
    ]