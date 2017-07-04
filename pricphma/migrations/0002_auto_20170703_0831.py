# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricphma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCuenta',
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
        migrations.RemoveField(
            model_name='estado_cuenta',
            name='Docente',
        ),
        migrations.DeleteModel(
            name='Estado_Cuenta',
        ),
    ]
