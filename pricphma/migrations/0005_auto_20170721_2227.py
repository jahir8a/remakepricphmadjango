# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricphma', '0004_auto_20170708_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='url_imagen',
            field=models.ImageField(upload_to='img/slider/'),
        ),
    ]
