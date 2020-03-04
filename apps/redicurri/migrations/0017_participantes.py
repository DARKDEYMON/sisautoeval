# Generated by Django 3.0.3 on 2020-03-02 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redicurri', '0016_delete_participantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='participantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('ci', models.PositiveIntegerField()),
                ('evaluacion_recurricular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redicurri.evaluacion_recurricular')),
            ],
        ),
    ]
