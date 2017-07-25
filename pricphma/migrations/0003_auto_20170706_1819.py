# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricphma', '0002_auto_20170703_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('url_imagen', models.ImageField(default='imagenes/no-img.jpg', upload_to='imagenes/')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('etiqueta', models.CharField(max_length=50)),
                ('enlace', models.URLField()),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='estadocuenta',
            options={'verbose_name': 'Estado de Cuenta', 'verbose_name_plural': 'Estados de Cuenta'},
        ),
    ]
