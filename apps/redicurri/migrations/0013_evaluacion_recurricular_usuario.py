# Generated by Django 3.0.3 on 2020-02-26 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('redicurri', '0012_etapa_5_etapa_6_etapa_7'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion_recurricular',
            name='usuario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
