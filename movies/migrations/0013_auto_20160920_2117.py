# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=b'0'),
        ),
    ]
