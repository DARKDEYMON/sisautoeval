# Generated by Django 3.0.3 on 2020-02-18 13:07

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('redicurri', '0007_auto_20200218_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa_2',
            name='pregunta_12',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('pp', 'Poca predisposición de los encuestados'), ('de', 'Demora en la entrega de las encuestas'), ('pc', 'Poca comprensión de los formularios'), ('o', 'Otros')], max_length=20, verbose_name='2.13. Que dificultad tuvo al momento de hacer la recolección de información con los formularios antes mencionados. Seleccione Varias opciones'),
        ),
    ]