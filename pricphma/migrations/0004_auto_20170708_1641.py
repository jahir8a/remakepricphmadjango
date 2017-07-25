# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricphma', '0003_auto_20170706_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='enlace',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url_imagen',
            field=models.ImageField(upload_to='imagenes_slider/'),
        ),
    ]
