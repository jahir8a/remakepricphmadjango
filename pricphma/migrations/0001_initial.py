# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('identidad', models.BigIntegerField(serialize=False, primary_key=True)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('numero_afiliacion', models.BigIntegerField()),
                ('fecha_ini_servicio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Cuenta',
            fields=[
                ('anio', models.IntegerField(serialize=False, primary_key=True)),
                ('enero', models.FloatField()),
                ('febrero', models.FloatField()),
                ('marzo', models.FloatField()),
                ('abril', models.FloatField()),
                ('mayo', models.FloatField()),
                ('junio', models.FloatField()),
                ('julio', models.FloatField()),
                ('agosto', models.FloatField()),
                ('septiembre', models.FloatField()),
                ('octubre', models.FloatField()),
                ('noviembre', models.FloatField()),
                ('diciembre', models.FloatField()),
                ('Docente', models.ForeignKey(to='pricphma.Docente')),
            ],
        ),
    ]
