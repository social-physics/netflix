# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20160916_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
